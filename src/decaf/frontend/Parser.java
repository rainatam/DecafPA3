//### This file created by BYACC 1.8(/Java extension  1.13)
//### Java capabilities added 7 Jan 97, Bob Jamison
//### Updated : 27 Nov 97  -- Bob Jamison, Joe Nieten
//###           01 Jan 98  -- Bob Jamison -- fixed generic semantic constructor
//###           01 Jun 99  -- Bob Jamison -- added Runnable support
//###           06 Aug 00  -- Bob Jamison -- made state variables class-global
//###           03 Jan 01  -- Bob Jamison -- improved flags, tracing
//###           16 May 01  -- Bob Jamison -- added custom stack sizing
//###           04 Mar 02  -- Yuval Oren  -- improved java performance, added options
//###           14 Mar 02  -- Tomas Hurka -- -d support, static initializer workaround
//###           14 Sep 06  -- Keltin Leung-- ReduceListener support, eliminate underflow report in error recovery
//### Please send bug reports to tom@hukatronic.cz
//### static char yysccsid[] = "@(#)yaccpar	1.8 (Berkeley) 01/20/90";






//#line 11 "Parser.y"
package decaf.frontend;

import decaf.tree.Tree;
import decaf.tree.Tree.*;
import decaf.error.*;
import java.util.*;
//#line 25 "Parser.java"
interface ReduceListener {
  public boolean onReduce(String rule);
}




public class Parser
             extends BaseParser
             implements ReduceListener
{

boolean yydebug;        //do I want debug output?
int yynerrs;            //number of errors so far
int yyerrflag;          //was there an error?
int yychar;             //the current working character

ReduceListener reduceListener = null;
void yyclearin ()       {yychar = (-1);}
void yyerrok ()         {yyerrflag=0;}
void addReduceListener(ReduceListener l) {
  reduceListener = l;}


//########## MESSAGES ##########
//###############################################################
// method: debug
//###############################################################
void debug(String msg)
{
  if (yydebug)
    System.out.println(msg);
}

//########## STATE STACK ##########
final static int YYSTACKSIZE = 500;  //maximum stack size
int statestk[] = new int[YYSTACKSIZE]; //state stack
int stateptr;
int stateptrmax;                     //highest index of stackptr
int statemax;                        //state when highest index reached
//###############################################################
// methods: state stack push,pop,drop,peek
//###############################################################
final void state_push(int state)
{
  try {
		stateptr++;
		statestk[stateptr]=state;
	 }
	 catch (ArrayIndexOutOfBoundsException e) {
     int oldsize = statestk.length;
     int newsize = oldsize * 2;
     int[] newstack = new int[newsize];
     System.arraycopy(statestk,0,newstack,0,oldsize);
     statestk = newstack;
     statestk[stateptr]=state;
  }
}
final int state_pop()
{
  return statestk[stateptr--];
}
final void state_drop(int cnt)
{
  stateptr -= cnt; 
}
final int state_peek(int relative)
{
  return statestk[stateptr-relative];
}
//###############################################################
// method: init_stacks : allocate and prepare stacks
//###############################################################
final boolean init_stacks()
{
  stateptr = -1;
  val_init();
  return true;
}
//###############################################################
// method: dump_stacks : show n levels of the stacks
//###############################################################
void dump_stacks(int count)
{
int i;
  System.out.println("=index==state====value=     s:"+stateptr+"  v:"+valptr);
  for (i=0;i<count;i++)
    System.out.println(" "+i+"    "+statestk[i]+"      "+valstk[i]);
  System.out.println("======================");
}


//########## SEMANTIC VALUES ##########
//## **user defined:SemValue
String   yytext;//user variable to return contextual strings
SemValue yyval; //used to return semantic vals from action routines
SemValue yylval;//the 'lval' (result) I got from yylex()
SemValue valstk[] = new SemValue[YYSTACKSIZE];
int valptr;
//###############################################################
// methods: value stack push,pop,drop,peek.
//###############################################################
final void val_init()
{
  yyval=new SemValue();
  yylval=new SemValue();
  valptr=-1;
}
final void val_push(SemValue val)
{
  try {
    valptr++;
    valstk[valptr]=val;
  }
  catch (ArrayIndexOutOfBoundsException e) {
    int oldsize = valstk.length;
    int newsize = oldsize*2;
    SemValue[] newstack = new SemValue[newsize];
    System.arraycopy(valstk,0,newstack,0,oldsize);
    valstk = newstack;
    valstk[valptr]=val;
  }
}
final SemValue val_pop()
{
  return valstk[valptr--];
}
final void val_drop(int cnt)
{
  valptr -= cnt;
}
final SemValue val_peek(int relative)
{
  return valstk[valptr-relative];
}
//#### end semantic value section ####
public final static short VOID=257;
public final static short BOOL=258;
public final static short INT=259;
public final static short STRING=260;
public final static short CLASS=261;
public final static short COMPLEX=262;
public final static short NULL=263;
public final static short EXTENDS=264;
public final static short THIS=265;
public final static short WHILE=266;
public final static short FOR=267;
public final static short IF=268;
public final static short ELSE=269;
public final static short RETURN=270;
public final static short BREAK=271;
public final static short NEW=272;
public final static short PRINT=273;
public final static short PRINTCOMP=274;
public final static short READ_INTEGER=275;
public final static short READ_LINE=276;
public final static short LITERAL=277;
public final static short IDENTIFIER=278;
public final static short AND=279;
public final static short OR=280;
public final static short STATIC=281;
public final static short INSTANCEOF=282;
public final static short LESS_EQUAL=283;
public final static short GREATER_EQUAL=284;
public final static short EQUAL=285;
public final static short NOT_EQUAL=286;
public final static short CASE=287;
public final static short DEFAULT=288;
public final static short SUPER=289;
public final static short DCOPY=290;
public final static short SCOPY=291;
public final static short DO=292;
public final static short OD=293;
public final static short DO_SEP=294;
public final static short UMINUS=295;
public final static short EMPTY=296;
public final static short YYERRCODE=256;
final static short yylhs[] = {                           -1,
    0,    1,    1,    3,    4,    5,    5,    5,    5,    5,
    5,    5,    2,    6,    6,    7,    7,    7,    9,    9,
   10,   10,    8,    8,   11,   12,   12,   13,   13,   13,
   13,   13,   13,   13,   13,   13,   13,   13,   14,   14,
   14,   26,   26,   23,   23,   25,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   24,   24,   24,
   24,   24,   24,   24,   24,   24,   24,   24,   24,   29,
   29,   31,   30,   28,   28,   27,   27,   32,   32,   16,
   17,   21,   15,   33,   33,   18,   18,   19,   20,   22,
   34,   34,   36,   35,
};
final static short yylen[] = {                            2,
    1,    2,    1,    2,    2,    1,    1,    1,    1,    1,
    2,    3,    6,    2,    0,    2,    2,    0,    1,    0,
    3,    1,    7,    6,    3,    2,    0,    1,    2,    1,
    1,    1,    2,    2,    2,    2,    1,    2,    3,    1,
    0,    2,    0,    2,    4,    5,    1,    1,    1,    3,
    3,    3,    3,    3,    3,    3,    3,    3,    3,    3,
    3,    3,    3,    2,    2,    2,    2,    2,    3,    3,
    1,    4,    5,    6,    5,    8,    1,    2,    2,    2,
    0,    4,    4,    1,    1,    1,    0,    3,    1,    5,
    9,    1,    6,    2,    0,    2,    1,    4,    4,    4,
    2,    0,    2,    3,
};
final static short yydefred[] = {                         0,
    0,    0,    0,    3,    0,    2,    0,    0,   14,   18,
    0,    7,    8,    6,    9,    0,   10,    0,   13,   16,
    0,    0,   17,   11,    0,    4,    0,    0,    0,    0,
   12,    0,   22,    0,    0,    0,    0,    5,    0,    0,
    0,   27,   24,   21,   23,    0,   85,   71,    0,    0,
    0,    0,   92,    0,    0,    0,    0,    0,   84,    0,
    0,    0,    0,   25,    0,    0,    0,    0,   77,    0,
    0,  102,   28,   37,   26,    0,   30,   31,   32,    0,
    0,    0,    0,    0,    0,    0,    0,    0,   49,    0,
    0,    0,   47,    0,   48,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   66,   67,   68,    0,
   78,   79,    0,   29,   33,   34,   35,   36,   38,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,   42,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,   69,   70,    0,    0,   63,    0,
    0,    0,  101,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   72,    0,    0,   98,   99,    0,    0,    0,
    0,  100,  103,   45,    0,    0,   90,    0,    0,   73,
    0,    0,   75,   81,  104,   46,    0,    0,   93,   74,
    0,    0,   94,    0,    0,    0,   80,    0,    0,    0,
   76,   91,    0,    0,   83,   82,
};
final static short yydgoto[] = {                          2,
    3,    4,   73,   21,   34,    8,   11,   23,   35,   36,
   74,   46,   75,   76,   77,   78,   79,   80,   81,   82,
   83,   84,   93,   86,   95,   88,  185,   89,  201,  206,
  207,  143,  199,  113,  152,  153,
};
final static short yysindex[] = {                      -234,
 -239,    0, -234,    0, -203,    0, -200,  -44,    0,    0,
  -50,    0,    0,    0,    0, -193,    0,  -92,    0,    0,
   28,  -85,    0,    0,  -83,    0,   49,   -2,   55,  -92,
    0,  -92,    0,  -74,   60,   52,   66,    0,  -11,  -92,
  -11,    0,    0,    0,    0,    5,    0,    0,   58,   74,
   76,  116,    0, -136,   87,   93,   94,   95,    0,   98,
  116,  116,   73,    0,  116,  116,  116,   99,    0,  116,
  116,    0,    0,    0,    0,   81,    0,    0,    0,   84,
   86,   88,   91,  100,   92,  878,    0, -124,    0,  116,
  116,  116,    0,  878,    0,  117,   67,  116,  116,  121,
  122,  116,  -21,  -21, -105,  503,    0,    0,    0,  116,
    0,    0,  116,    0,    0,    0,    0,    0,    0,  116,
  116,  116,  116,  116,  116,  116,  116,  116,  116,  116,
  116,  116,  116,    0,  116,  134,  514,  118,  536,  135,
   96,  878,    3,   14,    0,    0,  564,  137,    0,  575,
  596, -271,    0,  878,   57,  931,    6,    6,  -32,  -32,
   20,   20,  -21,  -21,  -21,    6,    6,  825,  116,   41,
  116,   41,    0,  846,  116,    0,    0, -103,  116,   56,
   41,    0,    0,    0,  140,  139,    0,  704,  -84,    0,
  878,  143,    0,    0,    0,    0,  116,   41,    0,    0,
 -242,  145,    0,  129,  130,   65,    0,   41,  116,  116,
    0,    0,  765,  867,    0,    0,
};
final static short yyrindex[] = {                         0,
    0,    0,  191,    0,   71,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,  144,    0,    0,  164,
    0,  164,    0,    0,    0,  165,    0,    0,    0,    0,
    0,    0,    0,    0,    0,  -58,    0,    0,    0,    0,
    0,  -55,    0,    0,    0,    0,    0,    0,    0,    0,
  -60,  -60,  -60,    0,  -60,  -60,  -60,    0,    0,  -60,
  -60,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  904,    0,  476,    0,    0,  -60,
  -58,  -60,    0,  160,    0,    0,    0,  -60,  -60,    0,
    0,  -60,  367,  405,    0,    0,    0,    0,    0,  -60,
    0,    0,  -60,    0,    0,    0,    0,    0,    0,  -60,
  -60,  -60,  -60,  -60,  -60,  -60,  -60,  -60,  -60,  -60,
  -60,  -60,  -60,    0,  -60,  155,    0,    0,    0,    0,
  -60,   19,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,  -17,  664,  -25,  556,  773,  921,  941,
  616,  953,  414,  441,  450,  793,  912,    0,   -9,  -58,
  -60,  -58,    0,    0,  -60,    0,    0,    0,  -60,    0,
  -58,    0,    0,    0,    0,  180,    0,    0,  -33,    0,
   39,    0,    0,    0,    0,    0,   -4,  -58,    0,    0,
    0,    0,    0,    0,    0,    0,    0,  -58,  -60,  -60,
    0,    0,    0,    0,    0,    0,
};
final static short yygindex[] = {                         0,
    0,  219,  225,   24,   18,    0,    0,    0,  215,    0,
   32,    0,  -88,  -82,    0,    0,    0,    0,    0,    0,
    0,    0,  -26, 1179,  534,    0,    0,   82,    0,    0,
    0,  -81,    0,    0,    0,    0,
};
final static int YYTABLESIZE=1389;
static short yytable[];
static { yytable();}
static void yytable(){
yytable = new short[]{                         95,
   41,   95,   95,   97,  131,   28,   95,   28,  138,  129,
  127,   95,  128,  134,  130,   62,   28,  144,   62,   85,
   47,  182,  183,   39,  134,   95,    1,  133,   22,  132,
   95,   87,   62,   62,   59,   25,   41,   62,    5,   67,
   66,   39,  131,  176,   63,  204,  175,  129,  127,   61,
  128,  134,  130,   33,  177,   33,  131,  175,  135,   89,
    7,  129,   89,   44,   85,  134,  130,   62,   65,  135,
   43,   97,   45,   62,   19,   67,   66,    9,   10,   88,
   63,  187,   88,  189,   24,   61,   26,  186,   30,   95,
   31,   95,  195,  131,   32,   40,  135,   90,  129,  127,
   39,  128,  134,  130,   65,   62,   41,   67,   66,  203,
  135,   42,   63,   91,  202,   92,  133,   61,  132,  212,
   12,   13,   14,   15,   16,   17,   98,   42,   62,   64,
   67,   66,   99,  100,  101,   63,   65,  102,  110,  114,
   61,   96,  115,   85,  116,   85,  117,  135,   62,  118,
   67,   66,  120,  136,   85,   63,  140,  141,  119,   65,
   61,  145,  146,   42,   12,   13,   14,   15,   16,   17,
   85,   85,  148,  169,  192,  173,  171,  179,  194,   65,
  196,   85,  175,  200,  198,  208,  209,  210,   31,  211,
    1,   44,   27,   15,   29,   44,   44,   44,   44,   44,
   44,   44,    5,   38,   20,   19,   12,   13,   14,   15,
   16,   17,   44,   44,   44,   44,   44,   43,   96,   43,
   86,    6,   43,   95,   95,   95,   95,   95,   95,   95,
   18,   95,   95,   95,   95,   20,   95,   95,   95,   95,
   95,   95,   95,   95,   95,   44,   37,   44,   95,    0,
  123,  124,    0,   95,   62,   95,   95,   95,   95,   95,
   95,   12,   13,   14,   15,   16,   17,   47,   43,   48,
   49,   50,   51,   43,   52,   53,   54,   55,   56,   57,
   58,   59,  205,    0,    0,    0,   60,    0,    0,    0,
    0,   68,    0,   69,   70,   71,   72,   12,   13,   14,
   15,   16,   17,   47,    0,   48,   49,   50,   51,    0,
   52,   53,   54,   55,   56,   57,   58,   59,    0,    0,
    0,    0,   60,    0,    0,    0,    0,   68,    0,   69,
   70,   71,   72,  105,    0,   47,    0,   48,    0,  123,
  124,  125,  126,    0,   54,    0,    0,   57,   58,   59,
    0,    0,    0,    0,   60,    0,    0,    0,   47,   68,
   48,   69,   70,   71,    0,    0,    0,   54,    0,    0,
   57,   58,   59,    0,    0,    0,    0,   60,   47,    0,
   48,    0,   68,    0,   69,   70,   71,   54,    0,    0,
   57,   58,   59,    0,    0,    0,    0,   60,    0,    0,
    0,    0,   68,   64,   69,   70,   71,   64,   64,   64,
   64,   64,    0,   64,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,   64,   64,   64,    0,   64,    0,
    0,    0,    0,   44,   44,    0,    0,   44,   44,   44,
   44,   65,    0,    0,    0,   65,   65,   65,   65,   65,
   52,   65,    0,    0,   52,   52,   52,   52,   52,   64,
   52,    0,   65,   65,   65,    0,   65,    0,    0,    0,
    0,   52,   52,   52,    0,   52,    0,   53,    0,    0,
    0,   53,   53,   53,   53,   53,   54,   53,    0,    0,
   54,   54,   54,   54,   54,    0,   54,   65,   53,   53,
   53,    0,   53,    0,    0,    0,   52,   54,   54,   54,
    0,   54,   48,    0,    0,    0,   40,   48,   48,    0,
   48,   48,   48,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,   53,   40,   48,    0,   48,    0,  131,
    0,    0,   54,  149,  129,  127,    0,  128,  134,  130,
  131,    0,    0,    0,  170,  129,  127,    0,  128,  134,
  130,    0,  133,    0,  132,    0,   48,    0,    0,    0,
    0,    0,  131,  133,    0,  132,  172,  129,  127,   87,
  128,  134,  130,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,  135,    0,  133,   59,  132,    0,   59,
  131,    0,    0,    0,  135,  129,  127,  178,  128,  134,
  130,  131,    0,   59,   59,  180,  129,  127,    0,  128,
  134,  130,    0,  133,   87,  132,  135,    0,    0,    0,
    0,    0,  131,    0,  133,    0,  132,  129,  127,    0,
  128,  134,  130,    0,    0,   64,   64,    0,   59,   64,
   64,   64,   64,  181,  135,  133,   50,  132,   50,   50,
   50,    0,    0,    0,    0,  135,    0,    0,    0,    0,
    0,    0,    0,   50,   50,   50,    0,   50,    0,    0,
    0,    0,    0,   65,   65,    0,  135,   65,   65,   65,
   65,    0,   52,   52,    0,    0,   52,   52,   52,   52,
    0,    0,    0,   87,   61,   87,    0,   61,   50,    0,
    0,    0,    0,    0,   87,    0,    0,    0,    0,   53,
   53,   61,   61,   53,   53,   53,   53,    0,   54,   54,
   87,   87,   54,   54,   54,   54,    0,    0,    0,    0,
  131,   87,    0,    0,    0,  129,  127,    0,  128,  134,
  130,    0,    0,    0,   48,   48,   61,    0,   48,   48,
   48,   48,  197,  133,    0,  132,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,  121,  122,    0,    0,  123,  124,  125,  126,    0,
    0,    0,  121,  122,  135,    0,  123,  124,  125,  126,
    0,  131,    0,    0,    0,    0,  129,  127,    0,  128,
  134,  130,    0,   60,  121,  122,   60,    0,  123,  124,
  125,  126,    0,  215,  133,    0,  132,    0,    0,    0,
   60,   60,    0,   58,   59,   59,   58,    0,    0,    0,
   59,   59,  121,  122,    0,    0,  123,  124,  125,  126,
   58,   58,    0,  121,  122,  135,    0,  123,  124,  125,
  126,  131,    0,    0,    0,   60,  129,  127,    0,  128,
  134,  130,    0,    0,  121,  122,    0,    0,  123,  124,
  125,  126,  131,    0,  133,   58,  132,  129,  127,    0,
  128,  134,  130,    0,   50,   50,    0,    0,   50,   50,
   50,   50,    0,  131,    0,  133,    0,  132,  129,  127,
    0,  128,  134,  130,  131,  135,    0,  184,    0,  129,
  127,    0,  128,  134,  130,  216,  133,    0,  132,    0,
    0,    0,    0,    0,    0,    0,  135,  133,  190,  132,
   47,    0,   61,   61,    0,   47,   47,    0,   47,   47,
   47,    0,   57,    0,    0,   57,    0,  135,    0,    0,
    0,   55,    0,   47,   55,   47,    0,  131,  135,   57,
   57,    0,  129,  127,    0,  128,  134,  130,   55,   55,
    0,   56,  121,  122,   56,    0,  123,  124,  125,  126,
  133,    0,  132,   51,   47,   51,   51,   51,   56,   56,
    0,    0,    0,    0,   57,    0,    0,    0,    0,    0,
   51,   51,   51,   55,   51,    0,    0,    0,    0,    0,
    0,  135,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,   56,    0,    0,    0,    0,    0,    0,
    0,    0,    0,  121,  122,   51,    0,  123,  124,  125,
  126,   60,   60,    0,    0,    0,    0,   60,   60,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,   58,   58,    0,    0,    0,    0,   58,   58,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,  121,  122,    0,    0,  123,  124,  125,
  126,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,  121,  122,    0,    0,  123,  124,
  125,  126,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,  121,  122,    0,    0,  123,
  124,  125,  126,    0,    0,    0,  121,  122,    0,    0,
  123,  124,  125,  126,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,   47,   47,    0,    0,   47,   47,   47,   47,
   57,   57,    0,    0,    0,    0,   57,   57,    0,   55,
   55,    0,    0,    0,    0,    0,    0,    0,    0,  121,
    0,    0,    0,  123,  124,  125,  126,    0,    0,   56,
   56,    0,    0,    0,    0,    0,    0,    0,    0,    0,
   94,   51,   51,    0,    0,   51,   51,   51,   51,  103,
  104,  106,    0,  107,  108,  109,    0,    0,  111,  112,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,  137,    0,
  139,    0,    0,    0,    0,    0,  142,  142,    0,    0,
  147,    0,    0,    0,    0,    0,    0,    0,  150,    0,
    0,  151,    0,    0,    0,    0,    0,    0,  154,  155,
  156,  157,  158,  159,  160,  161,  162,  163,  164,  165,
  166,  167,    0,  168,    0,    0,    0,    0,    0,  174,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,  142,    0,  188,
    0,    0,    0,  191,    0,    0,    0,  193,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,  213,  214,
};
}
static short yycheck[];
static { yycheck(); }
static void yycheck() {
yycheck = new short[] {                         33,
   59,   35,   36,   59,   37,   91,   40,   91,   91,   42,
   43,   45,   45,   46,   47,   41,   91,   99,   44,   46,
  263,  293,  294,   41,   46,   59,  261,   60,   11,   62,
   64,   41,   58,   59,  277,   18,   41,   33,  278,   35,
   36,   59,   37,   41,   40,  288,   44,   42,   43,   45,
   45,   46,   47,   30,   41,   32,   37,   44,   91,   41,
  264,   42,   44,   40,   91,   46,   47,   93,   64,   91,
   39,   54,   41,   33,  125,   35,   36,  278,  123,   41,
   40,  170,   44,  172,  278,   45,   59,  169,   40,  123,
   93,  125,  181,   37,   40,   44,   91,   40,   42,   43,
   41,   45,   46,   47,   64,   33,   41,   35,   36,  198,
   91,  123,   40,   40,  197,   40,   60,   45,   62,  208,
  257,  258,  259,  260,  261,  262,   40,  123,   33,  125,
   35,   36,   40,   40,   40,   40,   64,   40,   40,   59,
   45,  278,   59,  170,   59,  172,   59,   91,   33,   59,
   35,   36,   61,  278,  181,   40,   40,   91,   59,   64,
   45,   41,   41,  123,  257,  258,  259,  260,  261,  262,
  197,  198,  278,   40,  278,   41,   59,   41,  123,   64,
   41,  208,   44,   41,  269,   41,   58,   58,   93,  125,
    0,   37,  278,  123,  278,   41,   42,   43,   44,   45,
   46,   47,   59,  278,   41,   41,  257,  258,  259,  260,
  261,  262,   58,   59,   60,   61,   62,  278,   59,  278,
   41,    3,  278,  257,  258,  259,  260,  261,  262,  263,
  281,  265,  266,  267,  268,   11,  270,  271,  272,  273,
  274,  275,  276,  277,  278,   91,   32,   93,  282,   -1,
  283,  284,   -1,  287,  280,  289,  290,  291,  292,  293,
  294,  257,  258,  259,  260,  261,  262,  263,  278,  265,
  266,  267,  268,  278,  270,  271,  272,  273,  274,  275,
  276,  277,  201,   -1,   -1,   -1,  282,   -1,   -1,   -1,
   -1,  287,   -1,  289,  290,  291,  292,  257,  258,  259,
  260,  261,  262,  263,   -1,  265,  266,  267,  268,   -1,
  270,  271,  272,  273,  274,  275,  276,  277,   -1,   -1,
   -1,   -1,  282,   -1,   -1,   -1,   -1,  287,   -1,  289,
  290,  291,  292,  261,   -1,  263,   -1,  265,   -1,  283,
  284,  285,  286,   -1,  272,   -1,   -1,  275,  276,  277,
   -1,   -1,   -1,   -1,  282,   -1,   -1,   -1,  263,  287,
  265,  289,  290,  291,   -1,   -1,   -1,  272,   -1,   -1,
  275,  276,  277,   -1,   -1,   -1,   -1,  282,  263,   -1,
  265,   -1,  287,   -1,  289,  290,  291,  272,   -1,   -1,
  275,  276,  277,   -1,   -1,   -1,   -1,  282,   -1,   -1,
   -1,   -1,  287,   37,  289,  290,  291,   41,   42,   43,
   44,   45,   -1,   47,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   58,   59,   60,   -1,   62,   -1,
   -1,   -1,   -1,  279,  280,   -1,   -1,  283,  284,  285,
  286,   37,   -1,   -1,   -1,   41,   42,   43,   44,   45,
   37,   47,   -1,   -1,   41,   42,   43,   44,   45,   93,
   47,   -1,   58,   59,   60,   -1,   62,   -1,   -1,   -1,
   -1,   58,   59,   60,   -1,   62,   -1,   37,   -1,   -1,
   -1,   41,   42,   43,   44,   45,   37,   47,   -1,   -1,
   41,   42,   43,   44,   45,   -1,   47,   93,   58,   59,
   60,   -1,   62,   -1,   -1,   -1,   93,   58,   59,   60,
   -1,   62,   37,   -1,   -1,   -1,   41,   42,   43,   -1,
   45,   46,   47,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   93,   59,   60,   -1,   62,   -1,   37,
   -1,   -1,   93,   41,   42,   43,   -1,   45,   46,   47,
   37,   -1,   -1,   -1,   41,   42,   43,   -1,   45,   46,
   47,   -1,   60,   -1,   62,   -1,   91,   -1,   -1,   -1,
   -1,   -1,   37,   60,   -1,   62,   41,   42,   43,   46,
   45,   46,   47,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   91,   -1,   60,   41,   62,   -1,   44,
   37,   -1,   -1,   -1,   91,   42,   43,   44,   45,   46,
   47,   37,   -1,   58,   59,   41,   42,   43,   -1,   45,
   46,   47,   -1,   60,   91,   62,   91,   -1,   -1,   -1,
   -1,   -1,   37,   -1,   60,   -1,   62,   42,   43,   -1,
   45,   46,   47,   -1,   -1,  279,  280,   -1,   93,  283,
  284,  285,  286,   58,   91,   60,   41,   62,   43,   44,
   45,   -1,   -1,   -1,   -1,   91,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   58,   59,   60,   -1,   62,   -1,   -1,
   -1,   -1,   -1,  279,  280,   -1,   91,  283,  284,  285,
  286,   -1,  279,  280,   -1,   -1,  283,  284,  285,  286,
   -1,   -1,   -1,  170,   41,  172,   -1,   44,   93,   -1,
   -1,   -1,   -1,   -1,  181,   -1,   -1,   -1,   -1,  279,
  280,   58,   59,  283,  284,  285,  286,   -1,  279,  280,
  197,  198,  283,  284,  285,  286,   -1,   -1,   -1,   -1,
   37,  208,   -1,   -1,   -1,   42,   43,   -1,   45,   46,
   47,   -1,   -1,   -1,  279,  280,   93,   -1,  283,  284,
  285,  286,   59,   60,   -1,   62,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,  279,  280,   -1,   -1,  283,  284,  285,  286,   -1,
   -1,   -1,  279,  280,   91,   -1,  283,  284,  285,  286,
   -1,   37,   -1,   -1,   -1,   -1,   42,   43,   -1,   45,
   46,   47,   -1,   41,  279,  280,   44,   -1,  283,  284,
  285,  286,   -1,   59,   60,   -1,   62,   -1,   -1,   -1,
   58,   59,   -1,   41,  279,  280,   44,   -1,   -1,   -1,
  285,  286,  279,  280,   -1,   -1,  283,  284,  285,  286,
   58,   59,   -1,  279,  280,   91,   -1,  283,  284,  285,
  286,   37,   -1,   -1,   -1,   93,   42,   43,   -1,   45,
   46,   47,   -1,   -1,  279,  280,   -1,   -1,  283,  284,
  285,  286,   37,   -1,   60,   93,   62,   42,   43,   -1,
   45,   46,   47,   -1,  279,  280,   -1,   -1,  283,  284,
  285,  286,   -1,   37,   -1,   60,   -1,   62,   42,   43,
   -1,   45,   46,   47,   37,   91,   -1,   93,   -1,   42,
   43,   -1,   45,   46,   47,   59,   60,   -1,   62,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   91,   60,   93,   62,
   37,   -1,  279,  280,   -1,   42,   43,   -1,   45,   46,
   47,   -1,   41,   -1,   -1,   44,   -1,   91,   -1,   -1,
   -1,   41,   -1,   60,   44,   62,   -1,   37,   91,   58,
   59,   -1,   42,   43,   -1,   45,   46,   47,   58,   59,
   -1,   41,  279,  280,   44,   -1,  283,  284,  285,  286,
   60,   -1,   62,   41,   91,   43,   44,   45,   58,   59,
   -1,   -1,   -1,   -1,   93,   -1,   -1,   -1,   -1,   -1,
   58,   59,   60,   93,   62,   -1,   -1,   -1,   -1,   -1,
   -1,   91,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   93,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,  279,  280,   93,   -1,  283,  284,  285,
  286,  279,  280,   -1,   -1,   -1,   -1,  285,  286,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,  279,  280,   -1,   -1,   -1,   -1,  285,  286,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,  279,  280,   -1,   -1,  283,  284,  285,
  286,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,  279,  280,   -1,   -1,  283,  284,
  285,  286,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,  279,  280,   -1,   -1,  283,
  284,  285,  286,   -1,   -1,   -1,  279,  280,   -1,   -1,
  283,  284,  285,  286,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,  279,  280,   -1,   -1,  283,  284,  285,  286,
  279,  280,   -1,   -1,   -1,   -1,  285,  286,   -1,  279,
  280,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  279,
   -1,   -1,   -1,  283,  284,  285,  286,   -1,   -1,  279,
  280,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   52,  279,  280,   -1,   -1,  283,  284,  285,  286,   61,
   62,   63,   -1,   65,   66,   67,   -1,   -1,   70,   71,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   90,   -1,
   92,   -1,   -1,   -1,   -1,   -1,   98,   99,   -1,   -1,
  102,   -1,   -1,   -1,   -1,   -1,   -1,   -1,  110,   -1,
   -1,  113,   -1,   -1,   -1,   -1,   -1,   -1,  120,  121,
  122,  123,  124,  125,  126,  127,  128,  129,  130,  131,
  132,  133,   -1,  135,   -1,   -1,   -1,   -1,   -1,  141,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,  169,   -1,  171,
   -1,   -1,   -1,  175,   -1,   -1,   -1,  179,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,  209,  210,
};
}
final static short YYFINAL=2;
final static short YYMAXTOKEN=296;
final static String yyname[] = {
"end-of-file",null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,"'!'",null,"'#'","'$'","'%'",null,null,"'('","')'","'*'","'+'",
"','","'-'","'.'","'/'",null,null,null,null,null,null,null,null,null,null,"':'",
"';'","'<'","'='","'>'",null,"'@'",null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,"'['",null,"']'",null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,"'{'",null,"'}'",null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,
null,null,null,null,null,null,null,null,null,"VOID","BOOL","INT","STRING",
"CLASS","COMPLEX","NULL","EXTENDS","THIS","WHILE","FOR","IF","ELSE","RETURN",
"BREAK","NEW","PRINT","PRINTCOMP","READ_INTEGER","READ_LINE","LITERAL",
"IDENTIFIER","AND","OR","STATIC","INSTANCEOF","LESS_EQUAL","GREATER_EQUAL",
"EQUAL","NOT_EQUAL","CASE","DEFAULT","SUPER","DCOPY","SCOPY","DO","OD","DO_SEP",
"UMINUS","EMPTY",
};
final static String yyrule[] = {
"$accept : Program",
"Program : ClassList",
"ClassList : ClassList ClassDef",
"ClassList : ClassDef",
"VariableDef : Variable ';'",
"Variable : Type IDENTIFIER",
"Type : INT",
"Type : VOID",
"Type : BOOL",
"Type : STRING",
"Type : COMPLEX",
"Type : CLASS IDENTIFIER",
"Type : Type '[' ']'",
"ClassDef : CLASS IDENTIFIER ExtendsClause '{' FieldList '}'",
"ExtendsClause : EXTENDS IDENTIFIER",
"ExtendsClause :",
"FieldList : FieldList VariableDef",
"FieldList : FieldList FunctionDef",
"FieldList :",
"Formals : VariableList",
"Formals :",
"VariableList : VariableList ',' Variable",
"VariableList : Variable",
"FunctionDef : STATIC Type IDENTIFIER '(' Formals ')' StmtBlock",
"FunctionDef : Type IDENTIFIER '(' Formals ')' StmtBlock",
"StmtBlock : '{' StmtList '}'",
"StmtList : StmtList Stmt",
"StmtList :",
"Stmt : VariableDef",
"Stmt : SimpleStmt ';'",
"Stmt : IfStmt",
"Stmt : WhileStmt",
"Stmt : ForStmt",
"Stmt : ReturnStmt ';'",
"Stmt : PrintStmt ';'",
"Stmt : PrintCompStmt ';'",
"Stmt : BreakStmt ';'",
"Stmt : StmtBlock",
"Stmt : DoStmt ';'",
"SimpleStmt : LValue '=' Expr",
"SimpleStmt : Call",
"SimpleStmt :",
"Receiver : Expr '.'",
"Receiver :",
"LValue : Receiver IDENTIFIER",
"LValue : Expr '[' Expr ']'",
"Call : Receiver IDENTIFIER '(' Actuals ')'",
"Expr : LValue",
"Expr : Call",
"Expr : Constant",
"Expr : Expr '+' Expr",
"Expr : Expr '-' Expr",
"Expr : Expr '*' Expr",
"Expr : Expr '/' Expr",
"Expr : Expr '%' Expr",
"Expr : Expr EQUAL Expr",
"Expr : Expr NOT_EQUAL Expr",
"Expr : Expr '<' Expr",
"Expr : Expr '>' Expr",
"Expr : Expr LESS_EQUAL Expr",
"Expr : Expr GREATER_EQUAL Expr",
"Expr : Expr AND Expr",
"Expr : Expr OR Expr",
"Expr : '(' Expr ')'",
"Expr : '-' Expr",
"Expr : '!' Expr",
"Expr : '@' Expr",
"Expr : '$' Expr",
"Expr : '#' Expr",
"Expr : READ_INTEGER '(' ')'",
"Expr : READ_LINE '(' ')'",
"Expr : THIS",
"Expr : NEW IDENTIFIER '(' ')'",
"Expr : NEW Type '[' Expr ']'",
"Expr : INSTANCEOF '(' Expr ',' IDENTIFIER ')'",
"Expr : '(' CLASS IDENTIFIER ')' Expr",
"Expr : CASE '(' Expr ')' '{' ACaseExprList DefaultExpr '}'",
"Expr : SUPER",
"Expr : DCOPY Expr",
"Expr : SCOPY Expr",
"ACaseExprList : ACaseExprList ACaseExpr",
"ACaseExprList :",
"ACaseExpr : Constant ':' Expr ';'",
"DefaultExpr : DEFAULT ':' Expr ';'",
"Constant : LITERAL",
"Constant : NULL",
"Actuals : ExprList",
"Actuals :",
"ExprList : ExprList ',' Expr",
"ExprList : Expr",
"WhileStmt : WHILE '(' Expr ')' Stmt",
"ForStmt : FOR '(' SimpleStmt ';' Expr ';' SimpleStmt ')' Stmt",
"BreakStmt : BREAK",
"IfStmt : IF '(' Expr ')' Stmt ElseClause",
"ElseClause : ELSE Stmt",
"ElseClause :",
"ReturnStmt : RETURN Expr",
"ReturnStmt : RETURN",
"PrintStmt : PRINT '(' ExprList ')'",
"PrintCompStmt : PRINTCOMP '(' ExprList ')'",
"DoStmt : DO DoBranchList DoSubStmt OD",
"DoBranchList : DoBranchList DoBranch",
"DoBranchList :",
"DoBranch : DoSubStmt DO_SEP",
"DoSubStmt : Expr ':' Stmt",
};

//#line 517 "Parser.y"
    
	/**
	 * 打印当前归约所用的语法规则<br>
	 * 请勿修改。
	 */
    public boolean onReduce(String rule) {
		if (rule.startsWith("$$"))
			return false;
		else
			rule = rule.replaceAll(" \\$\\$\\d+", "");

   	    if (rule.endsWith(":"))
    	    System.out.println(rule + " <empty>");
   	    else
			System.out.println(rule);
		return false;
    }
    
    public void diagnose() {
		addReduceListener(this);
		yyparse();
	}
//#line 703 "Parser.java"
//###############################################################
// method: yylexdebug : check lexer state
//###############################################################
void yylexdebug(int state,int ch)
{
String s=null;
  if (ch < 0) ch=0;
  if (ch <= YYMAXTOKEN) //check index bounds
     s = yyname[ch];    //now get it
  if (s==null)
    s = "illegal-symbol";
  debug("state "+state+", reading "+ch+" ("+s+")");
}





//The following are now global, to aid in error reporting
int yyn;       //next next thing to do
int yym;       //
int yystate;   //current parsing state from state table
String yys;    //current token string


//###############################################################
// method: yyparse : parse input and execute indicated items
//###############################################################
int yyparse()
{
boolean doaction;
  init_stacks();
  yynerrs = 0;
  yyerrflag = 0;
  yychar = -1;          //impossible char forces a read
  yystate=0;            //initial state
  state_push(yystate);  //save it
  while (true) //until parsing is done, either correctly, or w/error
    {
    doaction=true;
    //if (yydebug) debug("loop"); 
    //#### NEXT ACTION (from reduction table)
    for (yyn=yydefred[yystate];yyn==0;yyn=yydefred[yystate])
      {
      //if (yydebug) debug("yyn:"+yyn+"  state:"+yystate+"  yychar:"+yychar);
      if (yychar < 0)      //we want a char?
        {
        yychar = yylex();  //get next token
        //if (yydebug) debug(" next yychar:"+yychar);
        //#### ERROR CHECK ####
        //if (yychar < 0)    //it it didn't work/error
        //  {
        //  yychar = 0;      //change it to default string (no -1!)
          //if (yydebug)
          //  yylexdebug(yystate,yychar);
        //  }
        }//yychar<0
      yyn = yysindex[yystate];  //get amount to shift by (shift index)
      if ((yyn != 0) && (yyn += yychar) >= 0 &&
          yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
        {
        //if (yydebug)
          //debug("state "+yystate+", shifting to state "+yytable[yyn]);
        //#### NEXT STATE ####
        yystate = yytable[yyn];//we are in a new state
        state_push(yystate);   //save it
        val_push(yylval);      //push our lval as the input for next rule
        yychar = -1;           //since we have 'eaten' a token, say we need another
        if (yyerrflag > 0)     //have we recovered an error?
           --yyerrflag;        //give ourselves credit
        doaction=false;        //but don't process yet
        break;   //quit the yyn=0 loop
        }

    yyn = yyrindex[yystate];  //reduce
    if ((yyn !=0 ) && (yyn += yychar) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
      {   //we reduced!
      //if (yydebug) debug("reduce");
      yyn = yytable[yyn];
      doaction=true; //get ready to execute
      break;         //drop down to actions
      }
    else //ERROR RECOVERY
      {
      if (yyerrflag==0)
        {
        yyerror("syntax error");
        yynerrs++;
        }
      if (yyerrflag < 3) //low error count?
        {
        yyerrflag = 3;
        while (true)   //do until break
          {
          if (stateptr<0 || valptr<0)   //check for under & overflow here
            {
            return 1;
            }
          yyn = yysindex[state_peek(0)];
          if ((yyn != 0) && (yyn += YYERRCODE) >= 0 &&
                    yyn <= YYTABLESIZE && yycheck[yyn] == YYERRCODE)
            {
            //if (yydebug)
              //debug("state "+state_peek(0)+", error recovery shifting to state "+yytable[yyn]+" ");
            yystate = yytable[yyn];
            state_push(yystate);
            val_push(yylval);
            doaction=false;
            break;
            }
          else
            {
            //if (yydebug)
              //debug("error recovery discarding state "+state_peek(0)+" ");
            if (stateptr<0 || valptr<0)   //check for under & overflow here
              {
              return 1;
              }
            state_pop();
            val_pop();
            }
          }
        }
      else            //discard this token
        {
        if (yychar == 0)
          return 1; //yyabort
        //if (yydebug)
          //{
          //yys = null;
          //if (yychar <= YYMAXTOKEN) yys = yyname[yychar];
          //if (yys == null) yys = "illegal-symbol";
          //debug("state "+yystate+", error recovery discards token "+yychar+" ("+yys+")");
          //}
        yychar = -1;  //read another
        }
      }//end error recovery
    }//yyn=0 loop
    if (!doaction)   //any reason not to proceed?
      continue;      //skip action
    yym = yylen[yyn];          //get count of terminals on rhs
    //if (yydebug)
      //debug("state "+yystate+", reducing "+yym+" by rule "+yyn+" ("+yyrule[yyn]+")");
    if (yym>0)                 //if count of rhs not 'nil'
      yyval = val_peek(yym-1); //get current semantic value
    if (reduceListener == null || reduceListener.onReduce(yyrule[yyn])) // if intercepted!
      switch(yyn)
      {
//########## USER-SUPPLIED ACTIONS ##########
case 1:
//#line 55 "Parser.y"
{
						tree = new Tree.TopLevel(val_peek(0).clist, val_peek(0).loc);
					}
break;
case 2:
//#line 61 "Parser.y"
{
						yyval.clist.add(val_peek(0).cdef);
					}
break;
case 3:
//#line 65 "Parser.y"
{
                		yyval.clist = new ArrayList<Tree.ClassDef>();
                		yyval.clist.add(val_peek(0).cdef);
                	}
break;
case 5:
//#line 75 "Parser.y"
{
						yyval.vdef = new Tree.VarDef(val_peek(0).ident, val_peek(1).type, val_peek(0).loc);
					}
break;
case 6:
//#line 81 "Parser.y"
{
						yyval.type = new Tree.TypeIdent(Tree.INT, val_peek(0).loc);
					}
break;
case 7:
//#line 85 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.VOID, val_peek(0).loc);
                	}
break;
case 8:
//#line 89 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.BOOL, val_peek(0).loc);
                	}
break;
case 9:
//#line 93 "Parser.y"
{
                		yyval.type = new Tree.TypeIdent(Tree.STRING, val_peek(0).loc);
                	}
break;
case 10:
//#line 97 "Parser.y"
{
                        yyval.type = new Tree.TypeIdent(Tree.COMPLEX, val_peek(0).loc);
                    }
break;
case 11:
//#line 101 "Parser.y"
{
                		yyval.type = new Tree.TypeClass(val_peek(0).ident, val_peek(1).loc);
                	}
break;
case 12:
//#line 105 "Parser.y"
{
                		yyval.type = new Tree.TypeArray(val_peek(2).type, val_peek(2).loc);
                	}
break;
case 13:
//#line 111 "Parser.y"
{
						yyval.cdef = new Tree.ClassDef(val_peek(4).ident, val_peek(3).ident, val_peek(1).flist, val_peek(5).loc);
					}
break;
case 14:
//#line 117 "Parser.y"
{
						yyval.ident = val_peek(0).ident;
					}
break;
case 15:
//#line 121 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 16:
//#line 127 "Parser.y"
{
						yyval.flist.add(val_peek(0).vdef);
					}
break;
case 17:
//#line 131 "Parser.y"
{
						yyval.flist.add(val_peek(0).fdef);
					}
break;
case 18:
//#line 135 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.flist = new ArrayList<Tree>();
                	}
break;
case 20:
//#line 143 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.vlist = new ArrayList<Tree.VarDef>(); 
                	}
break;
case 21:
//#line 150 "Parser.y"
{
						yyval.vlist.add(val_peek(0).vdef);
					}
break;
case 22:
//#line 154 "Parser.y"
{
                		yyval.vlist = new ArrayList<Tree.VarDef>();
						yyval.vlist.add(val_peek(0).vdef);
                	}
break;
case 23:
//#line 161 "Parser.y"
{
						yyval.fdef = new MethodDef(true, val_peek(4).ident, val_peek(5).type, val_peek(2).vlist, (Block) val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 24:
//#line 165 "Parser.y"
{
						yyval.fdef = new MethodDef(false, val_peek(4).ident, val_peek(5).type, val_peek(2).vlist, (Block) val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 25:
//#line 171 "Parser.y"
{
						yyval.stmt = new Block(val_peek(1).slist, val_peek(2).loc);
					}
break;
case 26:
//#line 177 "Parser.y"
{
						yyval.slist.add(val_peek(0).stmt);
					}
break;
case 27:
//#line 181 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.slist = new ArrayList<Tree>();
                	}
break;
case 28:
//#line 188 "Parser.y"
{
						yyval.stmt = val_peek(0).vdef;
					}
break;
case 29:
//#line 193 "Parser.y"
{
                		if (yyval.stmt == null) {
                			yyval.stmt = new Tree.Skip(val_peek(0).loc);
                		}
                	}
break;
case 39:
//#line 210 "Parser.y"
{
						yyval.stmt = new Tree.Assign(val_peek(2).lvalue, val_peek(0).expr, val_peek(1).loc);
					}
break;
case 40:
//#line 214 "Parser.y"
{
                		yyval.stmt = new Tree.Exec(val_peek(0).expr, val_peek(0).loc);
                	}
break;
case 41:
//#line 218 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 43:
//#line 225 "Parser.y"
{
                		yyval = new SemValue();
                	}
break;
case 44:
//#line 231 "Parser.y"
{
						yyval.lvalue = new Tree.Ident(val_peek(1).expr, val_peek(0).ident, val_peek(0).loc);
						if (val_peek(1).loc == null) {
							yyval.loc = val_peek(0).loc;
						}
					}
break;
case 45:
//#line 238 "Parser.y"
{
                		yyval.lvalue = new Tree.Indexed(val_peek(3).expr, val_peek(1).expr, val_peek(3).loc);
                	}
break;
case 46:
//#line 244 "Parser.y"
{
						yyval.expr = new Tree.CallExpr(val_peek(4).expr, val_peek(3).ident, val_peek(1).elist, val_peek(3).loc);
						if (val_peek(4).loc == null) {
							yyval.loc = val_peek(3).loc;
						}
					}
break;
case 47:
//#line 253 "Parser.y"
{
						yyval.expr = val_peek(0).lvalue;
					}
break;
case 50:
//#line 259 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.PLUS, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 51:
//#line 263 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MINUS, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 52:
//#line 267 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MUL, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 53:
//#line 271 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.DIV, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 54:
//#line 275 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.MOD, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 55:
//#line 279 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.EQ, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 56:
//#line 283 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.NE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 57:
//#line 287 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.LT, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 58:
//#line 291 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.GT, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 59:
//#line 295 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.LE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 60:
//#line 299 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.GE, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 61:
//#line 303 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.AND, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 62:
//#line 307 "Parser.y"
{
                		yyval.expr = new Tree.Binary(Tree.OR, val_peek(2).expr, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 63:
//#line 311 "Parser.y"
{
                		yyval = val_peek(1);
                	}
break;
case 64:
//#line 315 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.NEG, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 65:
//#line 319 "Parser.y"
{
                		yyval.expr = new Tree.Unary(Tree.NOT, val_peek(0).expr, val_peek(1).loc);
                	}
break;
case 66:
//#line 323 "Parser.y"
{
                        yyval.expr = new Tree.Unary(Tree.RE, val_peek(0).expr, val_peek(1).loc);
                    }
break;
case 67:
//#line 327 "Parser.y"
{
                        yyval.expr = new Tree.Unary(Tree.IM, val_peek(0).expr, val_peek(1).loc);
                    }
break;
case 68:
//#line 331 "Parser.y"
{
                        yyval.expr = new Tree.Unary(Tree.COMPCAST, val_peek(0).expr, val_peek(1).loc);
                    }
break;
case 69:
//#line 335 "Parser.y"
{
                		yyval.expr = new Tree.ReadIntExpr(val_peek(2).loc);
                	}
break;
case 70:
//#line 339 "Parser.y"
{
                		yyval.expr = new Tree.ReadLineExpr(val_peek(2).loc);
                	}
break;
case 71:
//#line 343 "Parser.y"
{
                		yyval.expr = new Tree.ThisExpr(val_peek(0).loc);
                	}
break;
case 72:
//#line 347 "Parser.y"
{
                		yyval.expr = new Tree.NewClass(val_peek(2).ident, val_peek(3).loc);
                	}
break;
case 73:
//#line 351 "Parser.y"
{
                		yyval.expr = new Tree.NewArray(val_peek(3).type, val_peek(1).expr, val_peek(4).loc);
                	}
break;
case 74:
//#line 355 "Parser.y"
{
                		yyval.expr = new Tree.TypeTest(val_peek(3).expr, val_peek(1).ident, val_peek(5).loc);
                	}
break;
case 75:
//#line 359 "Parser.y"
{
                		yyval.expr = new Tree.TypeCast(val_peek(2).ident, val_peek(0).expr, val_peek(0).loc);
                	}
break;
case 76:
//#line 363 "Parser.y"
{
                        yyval.expr = new Tree.Case(val_peek(5).expr, val_peek(2).elist, val_peek(1).expr, val_peek(7).loc);
                    }
break;
case 77:
//#line 367 "Parser.y"
{
                        yyval.expr = new Tree.SuperExpr(val_peek(0).loc);
                    }
break;
case 78:
//#line 371 "Parser.y"
{
                        yyval.expr = new Tree.DCopyExpr(val_peek(0).expr, val_peek(1).loc);
                    }
break;
case 79:
//#line 375 "Parser.y"
{
                        yyval.expr = new Tree.SCopyExpr(val_peek(0).expr, val_peek(1).loc);
                    }
break;
case 80:
//#line 381 "Parser.y"
{
                    	yyval.elist.add(val_peek(0).expr);
                    }
break;
case 81:
//#line 385 "Parser.y"
{
                        yyval = new SemValue();
                        yyval.elist = new ArrayList<Expr>();
                    }
break;
case 82:
//#line 392 "Parser.y"
{
						yyval.expr = new Tree.ACaseExpr(val_peek(3).expr, val_peek(1).expr, val_peek(3).loc);
					}
break;
case 83:
//#line 398 "Parser.y"
{
                        yyval.expr = new Tree.DefaultExpr(val_peek(1).expr, val_peek(3).loc);
                    }
break;
case 84:
//#line 404 "Parser.y"
{
						yyval.expr = new Tree.Literal(val_peek(0).typeTag, val_peek(0).literal, val_peek(0).loc);
					}
break;
case 85:
//#line 408 "Parser.y"
{
						yyval.expr = new Null(val_peek(0).loc);
					}
break;
case 87:
//#line 415 "Parser.y"
{
                		yyval = new SemValue();
                		yyval.elist = new ArrayList<Tree.Expr>();
                	}
break;
case 88:
//#line 422 "Parser.y"
{
						yyval.elist.add(val_peek(0).expr);
					}
break;
case 89:
//#line 426 "Parser.y"
{
                		yyval.elist = new ArrayList<Tree.Expr>();
						yyval.elist.add(val_peek(0).expr);
                	}
break;
case 90:
//#line 433 "Parser.y"
{
						yyval.stmt = new Tree.WhileLoop(val_peek(2).expr, val_peek(0).stmt, val_peek(4).loc);
					}
break;
case 91:
//#line 439 "Parser.y"
{
						yyval.stmt = new Tree.ForLoop(val_peek(6).stmt, val_peek(4).expr, val_peek(2).stmt, val_peek(0).stmt, val_peek(8).loc);
					}
break;
case 92:
//#line 445 "Parser.y"
{
						yyval.stmt = new Tree.Break(val_peek(0).loc);
					}
break;
case 93:
//#line 451 "Parser.y"
{
						yyval.stmt = new Tree.If(val_peek(3).expr, val_peek(1).stmt, val_peek(0).stmt, val_peek(5).loc);
					}
break;
case 94:
//#line 457 "Parser.y"
{
						yyval.stmt = val_peek(0).stmt;
					}
break;
case 95:
//#line 461 "Parser.y"
{
						yyval = new SemValue();
					}
break;
case 96:
//#line 467 "Parser.y"
{
						yyval.stmt = new Tree.Return(val_peek(0).expr, val_peek(1).loc);
					}
break;
case 97:
//#line 471 "Parser.y"
{
                		yyval.stmt = new Tree.Return(null, val_peek(0).loc);
                	}
break;
case 98:
//#line 477 "Parser.y"
{
						yyval.stmt = new Print(val_peek(1).elist, val_peek(3).loc);
					}
break;
case 99:
//#line 483 "Parser.y"
{
                        yyval.stmt = new PrintComp(val_peek(1).elist, val_peek(3).loc);
                    }
break;
case 100:
//#line 489 "Parser.y"
{
                        yyval.stmt = new Do(val_peek(2).slist, val_peek(1).stmt, val_peek(3).loc);
                    }
break;
case 101:
//#line 495 "Parser.y"
{
                        yyval.slist.add(val_peek(0).stmt);
                    }
break;
case 102:
//#line 499 "Parser.y"
{
                        yyval = new SemValue();
                        yyval.slist = new ArrayList<Tree>();
                    }
break;
case 103:
//#line 506 "Parser.y"
{
                        yyval.stmt = new DoBranch(val_peek(1).stmt, val_peek(1).loc);
                    }
break;
case 104:
//#line 511 "Parser.y"
{
                        yyval.stmt = new DoSub(val_peek(2).expr, val_peek(0).stmt, val_peek(2).loc);
                    }
break;
//#line 1400 "Parser.java"
//########## END OF USER-SUPPLIED ACTIONS ##########
    }//switch
    //#### Now let's reduce... ####
    //if (yydebug) debug("reduce");
    state_drop(yym);             //we just reduced yylen states
    yystate = state_peek(0);     //get new state
    val_drop(yym);               //corresponding value drop
    yym = yylhs[yyn];            //select next TERMINAL(on lhs)
    if (yystate == 0 && yym == 0)//done? 'rest' state and at first TERMINAL
      {
      //if (yydebug) debug("After reduction, shifting from state 0 to state "+YYFINAL+"");
      yystate = YYFINAL;         //explicitly say we're done
      state_push(YYFINAL);       //and save it
      val_push(yyval);           //also save the semantic value of parsing
      if (yychar < 0)            //we want another character?
        {
        yychar = yylex();        //get next character
        //if (yychar<0) yychar=0;  //clean, if necessary
        //if (yydebug)
          //yylexdebug(yystate,yychar);
        }
      if (yychar == 0)          //Good exit (if lex returns 0 ;-)
         break;                 //quit the loop--all DONE
      }//if yystate
    else                        //else not done yet
      {                         //get next state and push, for next yydefred[]
      yyn = yygindex[yym];      //find out where to go
      if ((yyn != 0) && (yyn += yystate) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yystate)
        yystate = yytable[yyn]; //get new state
      else
        yystate = yydgoto[yym]; //else go to new defred
      //if (yydebug) debug("after reduction, shifting from state "+state_peek(0)+" to state "+yystate+"");
      state_push(yystate);     //going again, so push state & val...
      val_push(yyval);         //for next action
      }
    }//main loop
  return 0;//yyaccept!!
}
//## end of method parse() ######################################



//## run() --- for Thread #######################################
//## The -Jnorun option was used ##
//## end of method run() ########################################



//## Constructors ###############################################
//## The -Jnoconstruct option was used ##
//###############################################################



}
//################### END OF CLASS ##############################
