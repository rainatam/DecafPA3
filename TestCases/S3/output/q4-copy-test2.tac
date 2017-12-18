VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_animal) {
    <empty>
    animal
    _animal.setage;
    _animal.getage;
}

VTABLE(_people) {
    <empty>
    people
    _people.setaniage;
    _people.getage;
    _people.setage;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T7 = 4
    parm _T7
    _T8 =  call _Alloc
    _T9 = VTBL <_Main>
    *(_T8 + 0) = _T9
    return _T8
}

FUNCTION(_animal_New) {
memo ''
_animal_New:
    _T10 = 8
    parm _T10
    _T11 =  call _Alloc
    _T12 = 0
    *(_T11 + 4) = _T12
    _T13 = VTBL <_animal>
    *(_T11 + 0) = _T13
    return _T11
}

FUNCTION(_people_New) {
memo ''
_people_New:
    _T14 = 20
    parm _T14
    _T15 =  call _Alloc
    _T16 = 0
    *(_T15 + 4) = _T16
    *(_T15 + 8) = _T16
    *(_T15 + 12) = _T16
    *(_T15 + 16) = _T16
    _T17 = VTBL <_people>
    *(_T15 + 0) = _T17
    return _T15
}

FUNCTION(main) {
memo ''
main:
    _T20 =  call _people_New
    _T18 = _T20
    parm _T18
    _T21 = *(_T18 + 0)
    _T22 = *(_T21 + 16)
    call _T22
    _T23 =  call _people_New
    _T24 = *(_T18 + 0)
    *(_T23 + 0) = _T24
    _T25 = *(_T18 + 4)
    *(_T23 + 4) = _T25
    _T26 = *(_T18 + 8)
    *(_T23 + 8) = _T26
    _T27 = *(_T18 + 12)
    *(_T23 + 12) = _T27
    _T28 = *(_T18 + 16)
    *(_T23 + 16) = _T28
    _T29 = *(_T18 + 20)
    *(_T23 + 20) = _T29
    _T30 = *(_T18 + 24)
    *(_T23 + 24) = _T30
    _T31 = *(_T18 + 28)
    *(_T23 + 28) = _T31
    _T32 = *(_T18 + 32)
    *(_T23 + 32) = _T32
    _T33 = *(_T18 + 36)
    *(_T23 + 36) = _T33
    _T19 = _T23
    _T34 = 99
    parm _T19
    parm _T34
    _T35 = *(_T19 + 0)
    _T36 = *(_T35 + 8)
    call _T36
    _T37 = "a: \n"
    parm _T37
    call _PrintString
    parm _T18
    _T38 = *(_T18 + 0)
    _T39 = *(_T38 + 12)
    call _T39
    _T40 = "b: \n"
    parm _T40
    call _PrintString
    parm _T19
    _T41 = *(_T19 + 0)
    _T42 = *(_T41 + 12)
    call _T42
}

FUNCTION(_animal.setage) {
memo '_T0:4 _T1:8'
_animal.setage:
    _T43 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_animal.getage) {
memo '_T2:4'
_animal.getage:
    _T44 = *(_T2 + 4)
    parm _T44
    call _PrintInt
    _T45 = "\n"
    parm _T45
    call _PrintString
}

FUNCTION(_people.setaniage) {
memo '_T3:4 _T4:8'
_people.setaniage:
    _T46 = *(_T3 + 12)
    parm _T46
    parm _T4
    _T47 = *(_T46 + 0)
    _T48 = *(_T47 + 8)
    call _T48
}

FUNCTION(_people.getage) {
memo '_T5:4'
_people.getage:
    _T49 = *(_T5 + 4)
    parm _T49
    call _PrintInt
    _T50 = "\n"
    parm _T50
    call _PrintString
    _T51 = *(_T5 + 8)
    _T52 = *(_T51 + 0)
    _T53 = *(_T51 + 4)
    parm _T52
    call _PrintInt
    _T54 = "+"
    parm _T54
    call _PrintString
    parm _T53
    call _PrintInt
    _T55 = "j"
    parm _T55
    call _PrintString
    _T56 = "\n"
    parm _T56
    call _PrintString
    _T57 = *(_T5 + 12)
    parm _T57
    _T58 = *(_T57 + 0)
    _T59 = *(_T58 + 12)
    call _T59
    _T60 = *(_T5 + 16)
    parm _T60
    call _PrintString
    _T61 = "\n"
    parm _T61
    call _PrintString
}

FUNCTION(_people.setage) {
memo '_T6:4'
_people.setage:
    _T62 = *(_T6 + 12)
    _T63 =  call _animal_New
    *(_T6 + 12) = _T63
    _T64 = 100
    parm _T6
    parm _T64
    _T65 = *(_T6 + 0)
    _T66 = *(_T65 + 8)
    call _T66
    _T67 = *(_T6 + 4)
    _T68 = 10
    *(_T6 + 4) = _T68
    _T69 = *(_T6 + 16)
    _T70 = "11"
    *(_T6 + 16) = _T70
    _T71 = *(_T6 + 8)
    _T72 = 89
    _T73 = 0
    _T74 = 8
    _T75 = 8
    parm _T75
    _T76 =  call _Alloc
    *(_T76 + 0) = _T73
    *(_T76 + 4) = _T74
    _T77 = 0
    _T78 = *(_T76 + 0)
    _T79 = *(_T76 + 4)
    _T80 = 8
    parm _T80
    _T81 =  call _Alloc
    _T82 = (_T72 + _T78)
    *(_T81 + 0) = _T82
    _T83 = (_T77 + _T79)
    *(_T81 + 4) = _T83
    *(_T6 + 8) = _T81
}

