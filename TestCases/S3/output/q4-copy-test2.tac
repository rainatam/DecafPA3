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
    _T21 = VTBL <_people>
    _T22 = *(_T21 + 16)
    call _T22
    _T23 =  call _people_New
    _T24 = *(_T18 + 4)
    *(_T23 + 4) = _T24
    _T25 = *(_T18 + 8)
    *(_T23 + 8) = _T25
    _T26 =  call _animal_New
    *(_T23 + 12) = _T26
    _T27 = *(_T18 + 12)
    _T28 = *(_T27 + 4)
    *(_T26 + 4) = _T28
    _T29 = *(_T18 + 16)
    *(_T23 + 16) = _T29
    _T19 = _T23
    _T30 = 99
    parm _T19
    parm _T30
    _T31 = VTBL <_people>
    _T32 = *(_T31 + 8)
    call _T32
    _T33 = "a: \n"
    parm _T33
    call _PrintString
    parm _T18
    _T34 = VTBL <_people>
    _T35 = *(_T34 + 12)
    call _T35
    _T36 = "b: \n"
    parm _T36
    call _PrintString
    parm _T19
    _T37 = VTBL <_people>
    _T38 = *(_T37 + 12)
    call _T38
}

FUNCTION(_animal.setage) {
memo '_T0:4 _T1:8'
_animal.setage:
    _T39 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_animal.getage) {
memo '_T2:4'
_animal.getage:
    _T40 = *(_T2 + 4)
    parm _T40
    call _PrintInt
    _T41 = "\n"
    parm _T41
    call _PrintString
}

FUNCTION(_people.setaniage) {
memo '_T3:4 _T4:8'
_people.setaniage:
    _T42 = *(_T3 + 12)
    parm _T42
    parm _T4
    _T43 = VTBL <_animal>
    _T44 = *(_T43 + 8)
    call _T44
}

FUNCTION(_people.getage) {
memo '_T5:4'
_people.getage:
    _T45 = *(_T5 + 4)
    parm _T45
    call _PrintInt
    _T46 = "\n"
    parm _T46
    call _PrintString
    _T47 = *(_T5 + 8)
    _T48 = *(_T47 + 0)
    _T49 = *(_T47 + 4)
    parm _T48
    call _PrintInt
    _T50 = "+"
    parm _T50
    call _PrintString
    parm _T49
    call _PrintInt
    _T51 = "j"
    parm _T51
    call _PrintString
    _T52 = "\n"
    parm _T52
    call _PrintString
    _T53 = *(_T5 + 12)
    parm _T53
    _T54 = VTBL <_animal>
    _T55 = *(_T54 + 12)
    call _T55
    _T56 = *(_T5 + 16)
    parm _T56
    call _PrintString
    _T57 = "\n"
    parm _T57
    call _PrintString
}

FUNCTION(_people.setage) {
memo '_T6:4'
_people.setage:
    _T58 = *(_T6 + 12)
    _T59 =  call _animal_New
    *(_T6 + 12) = _T59
    _T60 = 100
    parm _T6
    parm _T60
    _T61 = VTBL <_people>
    _T62 = *(_T61 + 8)
    call _T62
    _T63 = *(_T6 + 4)
    _T64 = 10
    *(_T6 + 4) = _T64
    _T65 = *(_T6 + 16)
    _T66 = "11"
    *(_T6 + 16) = _T66
    _T67 = *(_T6 + 8)
    _T68 = 89
    _T69 = 0
    _T70 = 8
    _T71 = 8
    parm _T71
    _T72 =  call _Alloc
    *(_T72 + 0) = _T69
    *(_T72 + 4) = _T70
    _T73 = 0
    _T74 = *(_T72 + 0)
    _T75 = *(_T72 + 4)
    _T76 = 8
    parm _T76
    _T77 =  call _Alloc
    _T78 = (_T68 + _T74)
    *(_T77 + 0) = _T78
    _T79 = (_T73 + _T75)
    *(_T77 + 4) = _T79
    *(_T6 + 8) = _T77
}

