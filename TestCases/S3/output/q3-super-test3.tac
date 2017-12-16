VTABLE(_A) {
    <empty>
    A
    _A.setA;
    _A.print;
    _A.allprint;
    _A.fun;
}

VTABLE(_B) {
    _A
    B
    _A.setA;
    _B.print;
    _B.allprint;
    _B.fun;
    _B.setB;
}

VTABLE(_C) {
    _A
    C
    _A.setA;
    _C.print;
    _C.allprint;
    _C.fun;
    _C.setC;
}

VTABLE(_D) {
    _B
    D
    _A.setA;
    _D.print;
    _D.allprint;
    _D.fun;
    _B.setB;
    _D.setD;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T24 = 12
    parm _T24
    _T25 =  call _Alloc
    _T26 = 0
    *(_T25 + 4) = _T26
    *(_T25 + 8) = _T26
    _T27 = VTBL <_A>
    *(_T25 + 0) = _T27
    return _T25
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T28 = 20
    parm _T28
    _T29 =  call _Alloc
    _T30 = 0
    *(_T29 + 4) = _T30
    *(_T29 + 8) = _T30
    *(_T29 + 12) = _T30
    *(_T29 + 16) = _T30
    _T31 = VTBL <_B>
    *(_T29 + 0) = _T31
    return _T29
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T32 = 20
    parm _T32
    _T33 =  call _Alloc
    _T34 = 0
    *(_T33 + 4) = _T34
    *(_T33 + 8) = _T34
    *(_T33 + 12) = _T34
    *(_T33 + 16) = _T34
    _T35 = VTBL <_C>
    *(_T33 + 0) = _T35
    return _T33
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T36 = 28
    parm _T36
    _T37 =  call _Alloc
    _T38 = 0
    _T39 = 4
    _T40 = (_T37 + _T36)
_L29:
    _T41 = (_T40 - _T39)
    _T40 = _T41
    _T42 = (_T36 - _T39)
    _T36 = _T42
    if (_T36 == 0) branch _L30
    *(_T40 + 0) = _T38
    branch _L29
_L30:
    _T43 = VTBL <_D>
    *(_T40 + 0) = _T43
    return _T40
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T44 = 4
    parm _T44
    _T45 =  call _Alloc
    _T46 = VTBL <_Main>
    *(_T45 + 0) = _T46
    return _T45
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T47 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T48 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T49 = " a="
    parm _T49
    call _PrintString
    _T50 = *(_T3 + 4)
    parm _T50
    call _PrintInt
    _T51 = " a1="
    parm _T51
    call _PrintString
    _T52 = *(_T3 + 8)
    parm _T52
    call _PrintInt
    _T53 = " "
    parm _T53
    call _PrintString
}

FUNCTION(_A.allprint) {
memo '_T4:4'
_A.allprint:
    parm _T4
    _T54 = *(_T4 + 0)
    _T55 = *(_T54 + 12)
    call _T55
}

FUNCTION(_A.fun) {
memo '_T5:4'
_A.fun:
    _T56 = "A"
    parm _T56
    call _PrintString
    parm _T5
    _T57 = *(_T5 + 0)
    _T58 = *(_T57 + 12)
    call _T58
    _T59 = "\n"
    parm _T59
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T6:4 _T7:8 _T8:12'
_B.setB:
    _T60 = *(_T6 + 12)
    *(_T6 + 12) = _T7
    _T61 = *(_T6 + 16)
    *(_T6 + 16) = _T8
}

FUNCTION(_B.print) {
memo '_T9:4'
_B.print:
    _T62 = " b="
    parm _T62
    call _PrintString
    _T63 = *(_T9 + 12)
    parm _T63
    call _PrintInt
    _T64 = " b1="
    parm _T64
    call _PrintString
    _T65 = *(_T9 + 16)
    parm _T65
    call _PrintInt
    _T66 = " "
    parm _T66
    call _PrintString
}

FUNCTION(_B.allprint) {
memo '_T10:4'
_B.allprint:
    _T67 = *(_T10 + 0)
    parm _T67
    _T68 = *(_T67 + 0)
    _T69 = *(_T68 + 16)
    call _T69
    parm _T10
    _T70 = *(_T10 + 0)
    _T71 = *(_T70 + 12)
    call _T71
}

FUNCTION(_B.fun) {
memo '_T11:4'
_B.fun:
    _T72 = "B"
    parm _T72
    call _PrintString
    _T73 = *(_T11 + 0)
    parm _T73
    _T74 = *(_T73 + 0)
    _T75 = *(_T74 + 16)
    call _T75
    parm _T11
    _T76 = *(_T11 + 0)
    _T77 = *(_T76 + 12)
    call _T77
    _T78 = "\n"
    parm _T78
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T12:4 _T13:8 _T14:12'
_C.setC:
    _T79 = *(_T12 + 12)
    *(_T12 + 12) = _T13
    _T80 = *(_T12 + 16)
    *(_T12 + 16) = _T14
}

FUNCTION(_C.print) {
memo '_T15:4'
_C.print:
    _T81 = " c="
    parm _T81
    call _PrintString
    _T82 = *(_T15 + 12)
    parm _T82
    call _PrintInt
    _T83 = " c1="
    parm _T83
    call _PrintString
    _T84 = *(_T15 + 16)
    parm _T84
    call _PrintInt
    _T85 = " "
    parm _T85
    call _PrintString
}

FUNCTION(_C.allprint) {
memo '_T16:4'
_C.allprint:
    _T86 = *(_T16 + 0)
    parm _T86
    _T87 = *(_T86 + 0)
    _T88 = *(_T87 + 16)
    call _T88
    parm _T16
    _T89 = *(_T16 + 0)
    _T90 = *(_T89 + 12)
    call _T90
}

FUNCTION(_C.fun) {
memo '_T17:4'
_C.fun:
    _T91 = "C"
    parm _T91
    call _PrintString
    _T92 = *(_T17 + 0)
    parm _T92
    _T93 = *(_T92 + 0)
    _T94 = *(_T93 + 16)
    call _T94
    parm _T17
    _T95 = *(_T17 + 0)
    _T96 = *(_T95 + 12)
    call _T96
    _T97 = "\n"
    parm _T97
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T18:4 _T19:8 _T20:12'
_D.setD:
    _T98 = *(_T18 + 20)
    *(_T18 + 20) = _T19
    _T99 = *(_T18 + 24)
    *(_T18 + 24) = _T20
}

FUNCTION(_D.print) {
memo '_T21:4'
_D.print:
    _T100 = " d="
    parm _T100
    call _PrintString
    _T101 = *(_T21 + 20)
    parm _T101
    call _PrintInt
    _T102 = " d1="
    parm _T102
    call _PrintString
    _T103 = *(_T21 + 24)
    parm _T103
    call _PrintInt
    _T104 = " "
    parm _T104
    call _PrintString
}

FUNCTION(_D.allprint) {
memo '_T22:4'
_D.allprint:
    _T105 = *(_T22 + 0)
    parm _T105
    _T106 = *(_T105 + 0)
    _T107 = *(_T106 + 16)
    call _T107
    parm _T22
    _T108 = *(_T22 + 0)
    _T109 = *(_T108 + 12)
    call _T109
}

FUNCTION(_D.fun) {
memo '_T23:4'
_D.fun:
    _T110 = "D"
    parm _T110
    call _PrintString
    _T111 = *(_T23 + 0)
    parm _T111
    _T112 = *(_T111 + 0)
    _T113 = *(_T112 + 16)
    call _T113
    parm _T23
    _T114 = *(_T23 + 0)
    _T115 = *(_T114 + 12)
    call _T115
    _T116 = "\n"
    parm _T116
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T121 =  call _A_New
    _T117 = _T121
    _T122 =  call _B_New
    _T118 = _T122
    _T123 =  call _C_New
    _T119 = _T123
    _T124 =  call _D_New
    _T120 = _T124
    parm _T117
    _T125 = *(_T117 + 0)
    _T126 = *(_T125 + 20)
    call _T126
    parm _T118
    _T127 = *(_T118 + 0)
    _T128 = *(_T127 + 20)
    call _T128
    parm _T119
    _T129 = *(_T119 + 0)
    _T130 = *(_T129 + 20)
    call _T130
    parm _T120
    _T131 = *(_T120 + 0)
    _T132 = *(_T131 + 20)
    call _T132
}

