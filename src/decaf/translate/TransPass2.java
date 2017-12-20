package decaf.translate;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Stack;

import com.sun.xml.internal.rngom.parse.host.Base;
import decaf.symbol.Symbol;
import decaf.tree.Tree;
import decaf.backend.OffsetCounter;
import decaf.machdesc.Intrinsic;
import decaf.symbol.Variable;
import decaf.tac.Label;
import decaf.tac.Temp;
import decaf.type.BaseType;
import decaf.type.ClassType;
import decaf.symbol.Class;

public class TransPass2 extends Tree.Visitor {

	private Translater tr;

	private Temp currentThis;

	private Stack<Label> loopExits;

	private Temp vtable;

	public TransPass2(Translater tr) {
		this.tr = tr;
		loopExits = new Stack<Label>();
	}

	@Override
	public void visitClassDef(Tree.ClassDef classDef) {
		for (Tree f : classDef.fields) {
			f.accept(this);
		}
	}

	@Override
	public void visitMethodDef(Tree.MethodDef funcDefn) {
		if (!funcDefn.statik) {
			currentThis = ((Variable) funcDefn.symbol.getAssociatedScope()
					.lookup("this")).getTemp();
		}
		tr.beginFunc(funcDefn.symbol);
		funcDefn.body.accept(this);
		tr.endFunc();
		currentThis = null;
	}

	@Override
	public void visitTopLevel(Tree.TopLevel program) {
		for (Tree.ClassDef cd : program.classes) {
			cd.accept(this);
		}
	}

	@Override
	public void visitVarDef(Tree.VarDef varDef) {
		if (varDef.symbol.isLocalVar()) {
			Temp t = Temp.createTempI4();
			t.sym = varDef.symbol;
			varDef.symbol.setTemp(t);
		}
	}

	@Override
	public void visitBinary(Tree.Binary expr) {
		expr.left.accept(this);
		expr.right.accept(this);
		switch (expr.tag) {
		case Tree.PLUS:
			if (expr.left.type.equal(BaseType.COMPLEX) || expr.right.type.equal(BaseType.COMPLEX)) {
				Temp lReal, lImg, rReal, rImg;
				if (expr.left.type.equal(BaseType.INT)) {
					lReal = expr.left.val;
					lImg = tr.genLoadImm4(0);
				} else {
					lReal = tr.genLoad(expr.left.val, 0);
					lImg = tr.genLoad(expr.left.val, 4);
				}
				if (expr.right.type.equal(BaseType.INT)) {
					rReal = expr.right.val;
					rImg = tr.genLoadImm4(0);
				} else {
					rReal = tr.genLoad(expr.right.val, 0);
					rImg = tr.genLoad(expr.right.val, 4);
				}
				Temp eight = tr.genLoadImm4(8);
				tr.genParm(eight);
				expr.val = tr.genIntrinsicCall(Intrinsic.ALLOCATE);
				tr.genStore(tr.genAdd(lReal, rReal), expr.val, 0);
				tr.genStore(tr.genAdd(lImg, rImg), expr.val, 4);
			} else {
				expr.val = tr.genAdd(expr.left.val, expr.right.val);
			}
			break;
		case Tree.MINUS:
			expr.val = tr.genSub(expr.left.val, expr.right.val);
			break;
		case Tree.MUL:
			if (expr.left.type.equal(BaseType.COMPLEX) || expr.right.type.equal(BaseType.COMPLEX)) {
				Temp lReal, lImg, rReal, rImg;
				if (expr.left.type.equal(BaseType.INT)) {
					lReal = expr.left.val;
					lImg = tr.genLoadImm4(0);
				} else {
					lReal = tr.genLoad(expr.left.val, 0);
					lImg = tr.genLoad(expr.left.val, 4);
				}
				if (expr.right.type.equal(BaseType.INT)) {
					rReal = expr.right.val;
					rImg = tr.genLoadImm4(0);
				} else {
					rReal = tr.genLoad(expr.right.val, 0);
					rImg = tr.genLoad(expr.right.val, 4);
				}
				Temp eight = tr.genLoadImm4(8);
				tr.genParm(eight);
				expr.val = tr.genIntrinsicCall(Intrinsic.ALLOCATE);
				tr.genStore(tr.genSub(tr.genMul(lReal, rReal), tr.genMul(lImg, rImg)), expr.val, 0);
				tr.genStore(tr.genSub(tr.genMul(lReal, rImg), tr.genMul(rReal, lImg)), expr.val, 4);
			} else {
				expr.val = tr.genMul(expr.left.val, expr.right.val);
			}
			break;
		case Tree.DIV:
			Label nohalt = Label.createLabel();
			tr.genBnez(expr.right.val, nohalt);
			Temp tmp = tr.genLoadStrConst("Decaf runtime error: Division by zero error.\n");
			tr.genParm(tmp);
			tr.genIntrinsicCall(Intrinsic.PRINT_STRING);
			tr.genIntrinsicCall(Intrinsic.HALT);
			tr.genMark(nohalt);
			expr.val = tr.genDiv(expr.left.val, expr.right.val);
			break;
		case Tree.MOD:
			nohalt = Label.createLabel();
			tr.genBnez(expr.right.val, nohalt);
			tmp = tr.genLoadStrConst("Decaf runtime error: Division by zero error.\n");
			tr.genParm(tmp);
			tr.genIntrinsicCall(Intrinsic.PRINT_STRING);
			tr.genIntrinsicCall(Intrinsic.HALT);
			tr.genMark(nohalt);
			expr.val = tr.genMod(expr.left.val, expr.right.val);
			break;
		case Tree.AND:
			expr.val = tr.genLAnd(expr.left.val, expr.right.val);
			break;
		case Tree.OR:
			expr.val = tr.genLOr(expr.left.val, expr.right.val);
			break;
		case Tree.LT:
			expr.val = tr.genLes(expr.left.val, expr.right.val);
			break;
		case Tree.LE:
			expr.val = tr.genLeq(expr.left.val, expr.right.val);
			break;
		case Tree.GT:
			expr.val = tr.genGtr(expr.left.val, expr.right.val);
			break;
		case Tree.GE:
			expr.val = tr.genGeq(expr.left.val, expr.right.val);
			break;
		case Tree.EQ:
		case Tree.NE:
			genEquNeq(expr);
			break;
		}
	}

	private void genEquNeq(Tree.Binary expr) {
		if (expr.left.type.equal(BaseType.STRING)
				|| expr.right.type.equal(BaseType.STRING)) {
			tr.genParm(expr.left.val);
			tr.genParm(expr.right.val);
			expr.val = tr.genDirectCall(Intrinsic.STRING_EQUAL.label,
					BaseType.BOOL);
			if(expr.tag == Tree.NE){
				expr.val = tr.genLNot(expr.val);
			}
		} else {
			if(expr.tag == Tree.EQ)
				expr.val = tr.genEqu(expr.left.val, expr.right.val);
			else
				expr.val = tr.genNeq(expr.left.val, expr.right.val);
		}
	}

	@Override
	public void visitAssign(Tree.Assign assign) {
		assign.left.accept(this);
		assign.expr.accept(this);
		switch (assign.left.lvKind) {
		case ARRAY_ELEMENT:
			Tree.Indexed arrayRef = (Tree.Indexed) assign.left;
			Temp esz = tr.genLoadImm4(OffsetCounter.WORD_SIZE);
			Temp t = tr.genMul(arrayRef.index.val, esz);
			Temp base = tr.genAdd(arrayRef.array.val, t);
			tr.genStore(assign.expr.val, base, 0);
			break;
		case MEMBER_VAR:
			Tree.Ident varRef = (Tree.Ident) assign.left;
			tr.genStore(assign.expr.val, varRef.owner.val, varRef.symbol
					.getOffset());
			break;
		case PARAM_VAR:
		case LOCAL_VAR:
			tr.genAssign(((Tree.Ident) assign.left).symbol.getTemp(),
					assign.expr.val);
			break;
		}
	}

	@Override
	public void visitLiteral(Tree.Literal literal) {
		switch (literal.typeTag) {
			case Tree.INT:
				literal.val = tr.genLoadImm4(((Integer)literal.value).intValue());
				break;
			case Tree.BOOL:
				literal.val = tr.genLoadImm4((Boolean)(literal.value) ? 1 : 0);
				break;
			case Tree.COMPLEX:
				String value = (String) literal.value;
				String i = value.substring(0, value.length() - 1);
				int img = Integer.decode(i);
				int real = 0;
				Temp realTemp = tr.genLoadImm4(real);
				Temp imgTemp = tr.genLoadImm4(img);
				Temp eight = tr.genLoadImm4(8);
				tr.genParm(eight);
				literal.val = tr.genIntrinsicCall(Intrinsic.ALLOCATE);
				tr.genStore(realTemp, literal.val, 0);
				tr.genStore(imgTemp, literal.val, 4);
				break;
		default:
			literal.val = tr.genLoadStrConst((String)literal.value);
		}
	}

	@Override
	public void visitExec(Tree.Exec exec) {
		exec.expr.accept(this);
	}

	@Override
	public void visitUnary(Tree.Unary expr) {
		expr.expr.accept(this);
		switch (expr.tag){
			case Tree.NEG:
				expr.val = tr.genNeg(expr.expr.val);
				break;
			case Tree.RE:
				expr.val = tr.genLoad(expr.expr.val, 0);
				break;
			case Tree.IM:
				expr.val = tr.genLoad(expr.expr.val, 4);
				break;
			case Tree.COMPCAST:
				Temp eight = tr.genLoadImm4(8);
				Temp zero = tr.genLoadImm4(0);
				tr.genParm(eight);
				expr.val = tr.genIntrinsicCall(Intrinsic.ALLOCATE);
				tr.genStore(expr.expr.val, expr.val, 0);
				tr.genStore(zero, expr.val, 4);
				break;
		default:
			expr.val = tr.genLNot(expr.expr.val);
		}
	}

	@Override
	public void visitNull(Tree.Null nullExpr) {
		nullExpr.val = tr.genLoadImm4(0);
	}

	@Override
	public void visitBlock(Tree.Block block) {
		for (Tree s : block.block) {
			s.accept(this);
		}
	}

	@Override
	public void visitThisExpr(Tree.ThisExpr thisExpr) {
		thisExpr.val = currentThis;
	}

	@Override
	public void visitReadIntExpr(Tree.ReadIntExpr readIntExpr) {
		readIntExpr.val = tr.genIntrinsicCall(Intrinsic.READ_INT);
	}

	@Override
	public void visitReadLineExpr(Tree.ReadLineExpr readStringExpr) {
		readStringExpr.val = tr.genIntrinsicCall(Intrinsic.READ_LINE);
	}

	@Override
	public void visitReturn(Tree.Return returnStmt) {
		if (returnStmt.expr != null) {
			returnStmt.expr.accept(this);
			tr.genReturn(returnStmt.expr.val);
		} else {
			tr.genReturn(null);
		}

	}

	@Override
	public void visitPrint(Tree.Print printStmt) {
		for (Tree.Expr r : printStmt.exprs) {
			r.accept(this);
			tr.genParm(r.val);
			if (r.type.equal(BaseType.BOOL)) {
				tr.genIntrinsicCall(Intrinsic.PRINT_BOOL);
			} else if (r.type.equal(BaseType.INT)) {
				tr.genIntrinsicCall(Intrinsic.PRINT_INT);
			} else if (r.type.equal(BaseType.STRING)) {
				tr.genIntrinsicCall(Intrinsic.PRINT_STRING);
			}
		}
	}

	@Override
	public void visitPrintComp(Tree.PrintComp printCompStmt) {
		for (Tree expr : printCompStmt.exprs) {
			expr.accept(this);
			Temp real = tr.genLoad(expr.val, 0);
			Temp img = tr.genLoad(expr.val, 4);
			tr.genParm(real);
			tr.genIntrinsicCall(Intrinsic.PRINT_INT);
			Temp plus = tr.genLoadStrConst("+");
			tr.genParm(plus);
			tr.genIntrinsicCall(Intrinsic.PRINT_STRING);
			tr.genParm(img);
			tr.genIntrinsicCall(Intrinsic.PRINT_INT);
			Temp j = tr.genLoadStrConst("j");
			tr.genParm(j);
			tr.genIntrinsicCall((Intrinsic.PRINT_STRING));

		}
	}

	@Override
	public void visitIndexed(Tree.Indexed indexed) {
		indexed.array.accept(this);
		indexed.index.accept(this);
		tr.genCheckArrayIndex(indexed.array.val, indexed.index.val);
		
		Temp esz = tr.genLoadImm4(OffsetCounter.WORD_SIZE);
		Temp t = tr.genMul(indexed.index.val, esz);
		Temp base = tr.genAdd(indexed.array.val, t);
		indexed.val = tr.genLoad(base, 0);
	}

	@Override
	public void visitIdent(Tree.Ident ident) {
		if(ident.lvKind == Tree.LValue.Kind.MEMBER_VAR){
			ident.owner.accept(this);
		}
		
		switch (ident.lvKind) {
		case MEMBER_VAR:
			ident.val = tr.genLoad(ident.owner.val, ident.symbol.getOffset());
			break;
		default:
			ident.val = ident.symbol.getTemp();
			break;
		}
	}
	
	@Override
	public void visitBreak(Tree.Break breakStmt) {
		tr.genBranch(loopExits.peek());
	}

	@Override
	public void visitCallExpr(Tree.CallExpr callExpr) {
		if (callExpr.isArrayLength) {
			callExpr.receiver.accept(this);
			callExpr.val = tr.genLoad(callExpr.receiver.val,
					-OffsetCounter.WORD_SIZE);
		} else {
			if (callExpr.receiver != null) {
				callExpr.receiver.accept(this);
			}
			for (Tree.Expr expr : callExpr.actuals) {
				expr.accept(this);
			}
			if (callExpr.receiver != null) {
				tr.genParm(callExpr.receiver.val);
			}
			for (Tree.Expr expr : callExpr.actuals) {
				tr.genParm(expr.val);
			}
			if (callExpr.receiver == null) {
				callExpr.val = tr.genDirectCall(
						callExpr.symbol.getFuncty().label, callExpr.symbol
								.getReturnType());
			} else {
				Temp vt = tr.genLoad(callExpr.receiver.val, 0);
				Temp func = tr.genLoad(vt, callExpr.symbol.getOffset());
				callExpr.val = tr.genIndirectCall(func, callExpr.symbol
						.getReturnType());
				if (callExpr.receiver.tag == Tree.SUPEREXPR) {
					tr.genStore(vtable, callExpr.receiver.val, 0);
				}
			}
		}

	}

	@Override
	public void visitSuperExpr(Tree.SuperExpr superExpr) {
		vtable = tr.genLoad(currentThis, 0);
		Temp parent = tr.genLoad(vtable, 0);
		tr.genStore(parent, currentThis, 0);
		superExpr.val = currentThis;
	}

	@Override
	public void visitSCopyExpr(Tree.SCopyExpr sCopyExpr) {
		sCopyExpr.expr.accept(this);
		int width = ((ClassType)(sCopyExpr.expr.type)).getSymbol().getSize();
		Temp dstAddr = tr.genDirectCall(((ClassType)(sCopyExpr.expr.type)).getSymbol().getNewFuncLabel(), BaseType.INT);
		Temp srcAddr =  sCopyExpr.expr.val;
		sCopyExpr.val = dstAddr;
		for (int i = 0; i < width; i += 4) {
			Temp temp = tr.genLoad(srcAddr, i);
			tr.genStore(temp, dstAddr, i);
		}
	}

	private void deepCopyClass(Temp dst, Temp src, Symbol classSymbol) {
		//System.out.println(classSymbol.getName() + classSymbol.getType().toString());
		int size;
		Boolean end = false;
		Iterator<Symbol> iter = ((Class)classSymbol).getAssociatedScope().iterator();
		Iterator<Symbol> next = ((Class)classSymbol).getAssociatedScope().iterator();
		if (next.hasNext()) next.next();
		while(iter.hasNext()) {
			Symbol symbol = iter.next();
			Symbol nextSymbol = symbol;
			while(next.hasNext()) {
				nextSymbol = next.next();
				if (!next.hasNext()) {
					end = true;
				}
				if(!nextSymbol.getType().isFuncType())
					break;
			}
			if (symbol.getType().isClassType()) {
				Temp newDst = tr.genDirectCall(((ClassType)(symbol.getType())).getSymbol().getNewFuncLabel(), BaseType.INT);
				tr.genStore(newDst, dst, ((Variable)symbol).getOffset());
				Temp newSrc = tr.genLoad(src, ((Variable)symbol).getOffset());
				deepCopyClass(newDst, newSrc, ((ClassType)(symbol.getType())).getSymbol());
			} else if(!symbol.getType().isFuncType()){
				//System.out.println(symbol.getName() + " " + symbol.getType().toString() + symbol.isClass() + symbol.getType().isClassType());
				if (end)
					size = ((Class) classSymbol).getSize();
				else
					size = ((Variable)nextSymbol).getOffset();
				int offset = ((Variable)symbol).getOffset();
				for (int i = offset; i < size; i += 4) {
					Temp temp = tr.genLoad(src, i);
					tr.genStore(temp, dst, i);
				}
			}
		}
	}


	@Override
	public void visitDCopyExpr(Tree.DCopyExpr dCopyExpr) {
		dCopyExpr.expr.accept(this);
		dCopyExpr.val = tr.genDirectCall(((ClassType)(dCopyExpr.expr.type)).getSymbol().getNewFuncLabel(), BaseType.INT);
		deepCopyClass(dCopyExpr.val, dCopyExpr.expr.val, ((ClassType)(dCopyExpr.expr.type)).getSymbol());
	}

	@Override
	public void visitForLoop(Tree.ForLoop forLoop) {
		if (forLoop.init != null) {
			forLoop.init.accept(this);
		}
		Label cond = Label.createLabel();
		Label loop = Label.createLabel();
		tr.genBranch(cond);
		tr.genMark(loop);
		if (forLoop.update != null) {
			forLoop.update.accept(this);
		}
		tr.genMark(cond);
		forLoop.condition.accept(this);
		Label exit = Label.createLabel();
		tr.genBeqz(forLoop.condition.val, exit);
		loopExits.push(exit);
		if (forLoop.loopBody != null) {
			forLoop.loopBody.accept(this);
		}
		tr.genBranch(loop);
		loopExits.pop();
		tr.genMark(exit);
	}

	@Override
	public void visitIf(Tree.If ifStmt) {
		ifStmt.condition.accept(this);
		if (ifStmt.falseBranch != null) {
			Label falseLabel = Label.createLabel();
			tr.genBeqz(ifStmt.condition.val, falseLabel);
			ifStmt.trueBranch.accept(this);
			Label exit = Label.createLabel();
			tr.genBranch(exit);
			tr.genMark(falseLabel);
			ifStmt.falseBranch.accept(this);
			tr.genMark(exit);
		} else if (ifStmt.trueBranch != null) {
			Label exit = Label.createLabel();
			tr.genBeqz(ifStmt.condition.val, exit);
			if (ifStmt.trueBranch != null) {
				ifStmt.trueBranch.accept(this);
			}
			tr.genMark(exit);
		}
	}

	@Override
	public void visitCase(Tree.Case caseExpr) {
		caseExpr.expr.accept(this);
		Label exit = Label.createLabel();
		Label defaultLabel = Label.createLabel();
		List<Label> labelList = new ArrayList<>();
		caseExpr.val = Temp.createTempI4();
		for (Tree.Expr aCaseExpr : caseExpr.aExprs) {
			((Tree.ACaseExpr)aCaseExpr).left.accept(this);
			Temp val = tr.genSub(caseExpr.expr.val, ((Tree.ACaseExpr)aCaseExpr).left.val);
			Label caseLabel = Label.createLabel();
			labelList.add(caseLabel);
			tr.genBeqz(val, caseLabel);
		}
		tr.genBranch(defaultLabel);
		for (int i = 0; i < caseExpr.aExprs.size(); i++) {
			tr.genMark(labelList.get(i));
			((Tree.ACaseExpr)caseExpr.aExprs.get(i)).right.accept(this);
			tr.genAssign(caseExpr.val, ((Tree.ACaseExpr) caseExpr.aExprs.get(i)).right.val);
			tr.genBranch(exit);
		}

		tr.genMark(defaultLabel);
		caseExpr.dExpr.accept(this);
		tr.genAssign(caseExpr.val, caseExpr.dExpr.val);
		tr.genMark(exit);

	}

	@Override
	public void visitDefaultExpr(Tree.DefaultExpr defaultExpr) {
		defaultExpr.expr.accept(this);
		defaultExpr.val = defaultExpr.expr.val;
	}

	@Override
	public void visitDo(Tree.Do doStmt) {
		Label start = Label.createLabel();
		tr.genMark(start);

		Label exit = Label.createLabel();
		loopExits.push(exit);

		for (Tree branch : doStmt.branches) {
			Tree.DoSub doSub = (Tree.DoSub)((Tree.DoBranch) branch).sub;
			doSub.expr.accept(this);
			Label next = Label.createLabel();
			tr.genBeqz(doSub.expr.val, next);
			((Tree.DoSub) ((Tree.DoBranch) branch).sub).stmt.accept(this);
			tr.genBranch(start);
			tr.genMark(next);
		}
		Tree.DoSub doSub = (Tree.DoSub) doStmt.sub;
		doSub.expr.accept(this);
		Label next = Label.createLabel();
		tr.genBeqz(doSub.expr.val, next);
		doSub.stmt.accept(this);
		tr.genBranch(start);
		tr.genMark(next);

		loopExits.pop();
		tr.genMark(exit);
	}


	@Override
	public void visitNewArray(Tree.NewArray newArray) {
		newArray.length.accept(this);
		newArray.val = tr.genNewArray(newArray.length.val);
	}

	@Override
	public void visitNewClass(Tree.NewClass newClass) {
		newClass.val = tr.genDirectCall(newClass.symbol.getNewFuncLabel(),
				BaseType.INT);
	}

	@Override
	public void visitWhileLoop(Tree.WhileLoop whileLoop) {
		Label loop = Label.createLabel();
		tr.genMark(loop);
		whileLoop.condition.accept(this);
		Label exit = Label.createLabel();
		tr.genBeqz(whileLoop.condition.val, exit);
		loopExits.push(exit);
		if (whileLoop.loopBody != null) {
			whileLoop.loopBody.accept(this);
		}
		tr.genBranch(loop);
		loopExits.pop();
		tr.genMark(exit);
	}

	@Override
	public void visitTypeTest(Tree.TypeTest typeTest) {
		typeTest.instance.accept(this);
		typeTest.val = tr.genInstanceof(typeTest.instance.val,
				typeTest.symbol);
	}

	@Override
	public void visitTypeCast(Tree.TypeCast typeCast) {
		typeCast.expr.accept(this);
		if (!typeCast.expr.type.compatible(typeCast.symbol.getType())) {
			tr.genClassCast(typeCast.expr.val, typeCast.symbol);
		}
		typeCast.val = typeCast.expr.val;
	}
}
