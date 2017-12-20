VTABLE(_Mac) {
    <empty>
    Mac
    _Mac.Crash;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Mac_New) {
memo ''
_Mac_New:
    _T4 = 12
    parm _T4
    _T5 =  call _Alloc
    _T6 = 0
    *(_T5 + 4) = _T6
    *(_T5 + 8) = _T6
    _T7 = VTBL <_Mac>
    *(_T5 + 0) = _T7
    return _T5
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T8 = 4
    parm _T8
    _T9 =  call _Alloc
    _T10 = VTBL <_Main>
    *(_T9 + 0) = _T10
    return _T9
}

FUNCTION(_Mac.Crash) {
memo '_T0:4 _T1:8 _T2:12 _T3:16'
_Mac.Crash:
    _T11 = *(_T0 + 8)
    *(_T0 + 8) = _T1
    _T12 = *(_T0 + 4)
    *(_T0 + 4) = _T2
    _T13 = *(_T0 + 8)
    parm _T13
    call _PrintInt
    _T14 = "\n"
    parm _T14
    call _PrintString
    parm _T3
    call _PrintInt
    _T15 = "\n"
    parm _T15
    call _PrintString
    _T16 = *(_T0 + 4)
    _T17 = *(_T16 + 0)
    _T18 = *(_T16 + 4)
    parm _T17
    call _PrintInt
    _T19 = "+"
    parm _T19
    call _PrintString
    parm _T18
    call _PrintInt
    _T20 = "j"
    parm _T20
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T22 =  call _Mac_New
    _T21 = _T22
    _T23 = 2
    _T24 = 3
    _T25 = 0
    _T26 = 4
    _T27 = 8
    parm _T27
    _T28 =  call _Alloc
    *(_T28 + 0) = _T25
    *(_T28 + 4) = _T26
    _T29 = 0
    _T30 = *(_T28 + 0)
    _T31 = *(_T28 + 4)
    _T32 = 8
    parm _T32
    _T33 =  call _Alloc
    _T34 = (_T24 + _T30)
    *(_T33 + 0) = _T34
    _T35 = (_T29 + _T31)
    *(_T33 + 4) = _T35
    _T36 = 5
    parm _T21
    parm _T23
    parm _T33
    parm _T36
    _T37 = VTBL <_Mac>
    _T38 = *(_T37 + 8)
    call _T38
}

