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
    _T7 = 1
    _T5 = _T7
    _T8 = "wow!"
    _T4 = _T8
    _T9 = 3
    _T3 = _T9
    _T10 = 1
    _T11 = 0
    _T12 = 3
    _T13 = 8
    parm _T13
    _T14 =  call _Alloc
    *(_T14 + 0) = _T11
    *(_T14 + 4) = _T12
    _T15 = 0
    _T16 = *(_T14 + 0)
    _T17 = *(_T14 + 4)
    _T18 = 8
    parm _T18
    _T19 =  call _Alloc
    _T20 = (_T10 + _T16)
    *(_T19 + 0) = _T20
    _T21 = (_T15 + _T17)
    *(_T19 + 4) = _T21
    _T6 = _T19
    if (_T5 == 0) branch _L10
    _T22 = 5
    _T23 = (_T3 * _T22)
    _T3 = _T23
_L10:
    parm _T5
    call _PrintBool
    _T24 = " "
    parm _T24
    call _PrintString
    parm _T3
    call _PrintInt
}

