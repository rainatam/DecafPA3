VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T0 = 4
    parm _T0
    _T1 =  call _Alloc
    _T2 = VTBL <_Main>
    *(_T1 + 0) = _T2
    return _T1
}

FUNCTION(main) {
memo ''
main:
    _T8 = 6
    _T3 = _T8
    _T9 = 2
    _T4 = _T9
    _T10 = 3
    _T5 = _T10
    _T11 = 3
    _T12 = (_T3 * _T11)
    _T14 = 0
    _T15 = (_T12 - _T14)
    if (_T15 == 0) branch _L12
    _T16 = 3
    _T17 = (_T12 - _T16)
    if (_T17 == 0) branch _L13
    _T18 = 9
    _T19 = (_T12 - _T18)
    if (_T19 == 0) branch _L14
    branch _L11
_L12:
    _T20 = (_T4 + _T5)
    _T13 = _T20
    branch _L10
_L13:
    _T21 = 3
    _T22 = (_T4 + _T21)
    _T13 = _T22
    branch _L10
_L14:
    _T23 = 2
    _T24 = (_T5 * _T23)
    _T25 = 6
    _T26 = (_T24 + _T25)
    _T13 = _T26
    branch _L10
_L11:
    _T27 = 100
    _T13 = _T27
_L10:
    _T4 = _T13
    parm _T4
    call _PrintInt
    _T28 = "\n"
    parm _T28
    call _PrintString
    _T29 = 3
    _T6 = _T29
    _T31 = 0
    _T32 = (_T6 - _T31)
    if (_T32 == 0) branch _L17
    _T33 = 3
    _T34 = (_T6 - _T33)
    if (_T34 == 0) branch _L18
    _T35 = 6
    _T36 = (_T6 - _T35)
    if (_T36 == 0) branch _L19
    branch _L16
_L17:
    _T37 = (_T4 + _T5)
    _T30 = _T37
    branch _L15
_L18:
    _T38 = 3
    _T39 = (_T4 + _T38)
    _T30 = _T39
    branch _L15
_L19:
    _T40 = 2
    _T41 = (_T5 * _T40)
    _T42 = 6
    _T43 = (_T41 + _T42)
    _T30 = _T43
    branch _L15
_L16:
    _T44 = 100
    _T30 = _T44
_L15:
    _T4 = _T30
    parm _T4
    call _PrintInt
    _T45 = "\n"
    parm _T45
    call _PrintString
    _T47 = 0
    _T48 = (_T3 - _T47)
    if (_T48 == 0) branch _L22
    _T49 = 3
    _T50 = (_T3 - _T49)
    if (_T50 == 0) branch _L23
    _T51 = 6
    _T52 = (_T3 - _T51)
    if (_T52 == 0) branch _L24
    branch _L21
_L22:
    _T53 = (_T4 + _T5)
    _T46 = _T53
    branch _L20
_L23:
    _T54 = 3
    _T55 = (_T4 + _T54)
    _T46 = _T55
    branch _L20
_L24:
    _T56 = 2
    _T57 = (_T5 * _T56)
    _T58 = 6
    _T59 = (_T57 + _T58)
    _T46 = _T59
    branch _L20
_L21:
    _T60 = 100
    _T46 = _T60
_L20:
    _T4 = _T46
    parm _T4
    call _PrintInt
    _T61 = "\n"
    parm _T61
    call _PrintString
    _T62 = 6
    _T63 = (_T3 - _T62)
    _T65 = 0
    _T66 = (_T63 - _T65)
    if (_T66 == 0) branch _L27
    _T67 = 3
    _T68 = (_T63 - _T67)
    if (_T68 == 0) branch _L28
    _T69 = 9
    _T70 = (_T63 - _T69)
    if (_T70 == 0) branch _L29
    branch _L26
_L27:
    _T71 = (_T4 + _T5)
    _T64 = _T71
    branch _L25
_L28:
    _T72 = 3
    _T73 = (_T4 + _T72)
    _T64 = _T73
    branch _L25
_L29:
    _T74 = 2
    _T75 = (_T5 * _T74)
    _T76 = 6
    _T77 = (_T75 + _T76)
    _T64 = _T77
    branch _L25
_L26:
    _T78 = 100
    _T64 = _T78
_L25:
    _T4 = _T64
    parm _T4
    call _PrintInt
    _T79 = "\n"
    parm _T79
    call _PrintString
    _T81 = 0
    _T82 = (_T3 - _T81)
    if (_T82 == 0) branch _L32
    _T83 = 3
    _T84 = (_T3 - _T83)
    if (_T84 == 0) branch _L33
    _T85 = 6
    _T86 = (_T3 - _T85)
    if (_T86 == 0) branch _L34
    branch _L31
_L32:
    _T87 = (_T4 + _T5)
    _T80 = _T87
    branch _L30
_L33:
    _T88 = 3
    _T89 = (_T4 + _T88)
    _T80 = _T89
    branch _L30
_L34:
    _T90 = 2
    _T91 = (_T5 * _T90)
    _T92 = 6
    _T93 = (_T91 + _T92)
    _T80 = _T93
    branch _L30
_L31:
    _T94 = 100
    _T80 = _T94
_L30:
    _T95 = 8
    _T96 = 0
    parm _T95
    _T97 =  call _Alloc
    *(_T97 + 0) = _T80
    *(_T97 + 4) = _T96
    _T7 = _T97
    _T98 = *(_T7 + 0)
    _T99 = *(_T7 + 4)
    parm _T98
    call _PrintInt
    _T100 = "+"
    parm _T100
    call _PrintString
    parm _T99
    call _PrintInt
    _T101 = "j"
    parm _T101
    call _PrintString
    _T102 = "\n"
    parm _T102
    call _PrintString
    _T104 = 8
    _T105 = (_T3 - _T104)
    if (_T105 == 0) branch _L37
    _T106 = 3
    _T107 = (_T3 - _T106)
    if (_T107 == 0) branch _L38
    _T108 = 0
    _T109 = (_T3 - _T108)
    if (_T109 == 0) branch _L39
    branch _L36
_L37:
    _T110 = (_T4 + _T5)
    _T103 = _T110
    branch _L35
_L38:
    _T111 = (_T4 + _T3)
    _T103 = _T111
    branch _L35
_L39:
    _T112 = 8
    _T103 = _T112
    branch _L35
_L36:
    _T113 = 100
    _T103 = _T113
_L35:
    _T114 = 8
    _T115 = 0
    parm _T114
    _T116 =  call _Alloc
    *(_T116 + 0) = _T103
    *(_T116 + 4) = _T115
    _T7 = _T116
    _T117 = *(_T7 + 0)
    _T118 = *(_T7 + 4)
    parm _T117
    call _PrintInt
    _T119 = "+"
    parm _T119
    call _PrintString
    parm _T118
    call _PrintInt
    _T120 = "j"
    parm _T120
    call _PrintString
    _T121 = "\n"
    parm _T121
    call _PrintString
}

