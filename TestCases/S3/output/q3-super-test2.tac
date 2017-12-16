VTABLE(_A) {
    <empty>
    A
    _A.setA;
    _A.print;
    _A.fun;
}

VTABLE(_B) {
    _A
    B
    _A.setA;
    _B.print;
    _B.fun;
    _B.setB;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T10 = 12
    parm _T10
    _T11 =  call _Alloc
    _T12 = 0
    *(_T11 + 4) = _T12
    *(_T11 + 8) = _T12
    _T13 = VTBL <_A>
    *(_T11 + 0) = _T13
    return _T11
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T14 = 20
    parm _T14
    _T15 =  call _Alloc
    _T16 = 0
    *(_T15 + 4) = _T16
    *(_T15 + 8) = _T16
    *(_T15 + 12) = _T16
    *(_T15 + 16) = _T16
    _T17 = VTBL <_B>
    *(_T15 + 0) = _T17
    return _T15
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T18 = 4
    parm _T18
    _T19 =  call _Alloc
    _T20 = VTBL <_Main>
    *(_T19 + 0) = _T20
    return _T19
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T21 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T22 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T23 = " a="
    parm _T23
    call _PrintString
    _T24 = *(_T3 + 4)
    parm _T24
    call _PrintInt
    _T25 = " a1="
    parm _T25
    call _PrintString
    _T26 = *(_T3 + 8)
    parm _T26
    call _PrintInt
    _T27 = " "
    parm _T27
    call _PrintString
}

FUNCTION(_A.fun) {
memo '_T4:4'
_A.fun:
    _T28 = "A"
    parm _T28
    call _PrintString
    parm _T4
    _T29 = *(_T4 + 0)
    _T30 = *(_T29 + 12)
    call _T30
    _T31 = "\n"
    parm _T31
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T5:4 _T6:8 _T7:12'
_B.setB:
    _T32 = *(_T5 + 12)
    *(_T5 + 12) = _T6
    _T33 = *(_T5 + 16)
    *(_T5 + 16) = _T7
}

FUNCTION(_B.print) {
memo '_T8:4'
_B.print:
    _T34 = " b="
    parm _T34
    call _PrintString
    _T35 = *(_T8 + 12)
    parm _T35
    call _PrintInt
    _T36 = " b1="
    parm _T36
    call _PrintString
    _T37 = *(_T8 + 16)
    parm _T37
    call _PrintInt
    _T38 = " "
    parm _T38
    call _PrintString
}

FUNCTION(_B.fun) {
memo '_T9:4'
_B.fun:
    _T39 = "B"
    parm _T39
    call _PrintString
    _T40 = *(_T9 + 0)
    parm _T40
    _T41 = *(_T40 + 0)
    _T42 = *(_T41 + 12)
    call _T42
    parm _T9
    _T43 = *(_T9 + 0)
    _T44 = *(_T43 + 12)
    call _T44
    _T45 = "\n"
    parm _T45
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T48 =  call _A_New
    _T46 = _T48
    _T49 =  call _B_New
    _T47 = _T49
    _T50 = 10
    _T51 = 11
    parm _T46
    parm _T50
    parm _T51
    _T52 = *(_T46 + 0)
    _T53 = *(_T52 + 8)
    call _T53
    _T54 = 20
    _T55 = 21
    parm _T47
    parm _T54
    parm _T55
    _T56 = *(_T47 + 0)
    _T57 = *(_T56 + 8)
    call _T57
    parm _T46
    _T58 = *(_T46 + 0)
    _T59 = *(_T58 + 16)
    call _T59
    parm _T47
    _T60 = *(_T47 + 0)
    _T61 = *(_T60 + 16)
    call _T61
}

