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
    _T11 = 1
    _T6 = _T11
    parm _T6
    call _PrintInt
    _T12 = "\n"
    parm _T12
    call _PrintString
    _T13 = 3
    _T14 = 0
    _T15 = 12
    _T16 = 8
    parm _T16
    _T17 =  call _Alloc
    *(_T17 + 0) = _T14
    *(_T17 + 4) = _T15
    _T18 = 0
    _T19 = *(_T17 + 0)
    _T20 = *(_T17 + 4)
    _T21 = 8
    parm _T21
    _T22 =  call _Alloc
    _T23 = (_T13 + _T19)
    *(_T22 + 0) = _T23
    _T24 = (_T18 + _T20)
    *(_T22 + 4) = _T24
    _T3 = _T22
    _T25 = *(_T3 + 0)
    _T26 = *(_T3 + 4)
    parm _T25
    call _PrintInt
    _T27 = "+"
    parm _T27
    call _PrintString
    parm _T26
    call _PrintInt
    _T28 = "j"
    parm _T28
    call _PrintString
    _T29 = "\n"
    parm _T29
    call _PrintString
    _T30 = 3
    _T31 = 0
    _T32 = 45
    _T33 = 8
    parm _T33
    _T34 =  call _Alloc
    *(_T34 + 0) = _T31
    *(_T34 + 4) = _T32
    _T35 = 0
    _T36 = *(_T34 + 0)
    _T37 = *(_T34 + 4)
    _T38 = 8
    parm _T38
    _T39 =  call _Alloc
    _T40 = (_T30 + _T36)
    *(_T39 + 0) = _T40
    _T41 = (_T35 + _T37)
    *(_T39 + 4) = _T41
    _T5 = _T39
    _T42 = *(_T3 + 0)
    _T7 = _T42
    _T43 = *(_T3 + 4)
    _T8 = _T43
    parm _T7
    call _PrintInt
    parm _T8
    call _PrintInt
    _T44 = "\n"
    parm _T44
    call _PrintString
    _T45 = (_T7 + _T8)
    _T46 = 8
    _T47 = 0
    parm _T46
    _T48 =  call _Alloc
    *(_T48 + 0) = _T45
    *(_T48 + 4) = _T47
    _T4 = _T48
    _T49 = *(_T4 + 0)
    _T50 = *(_T4 + 4)
    parm _T49
    call _PrintInt
    _T51 = "+"
    parm _T51
    call _PrintString
    parm _T50
    call _PrintInt
    _T52 = "j"
    parm _T52
    call _PrintString
    _T53 = "\n"
    parm _T53
    call _PrintString
    _T54 = *(_T3 + 0)
    _T55 = *(_T3 + 4)
    _T56 = *(_T4 + 0)
    _T57 = *(_T4 + 4)
    _T58 = 8
    parm _T58
    _T59 =  call _Alloc
    _T60 = (_T54 + _T56)
    *(_T59 + 0) = _T60
    _T61 = (_T55 + _T57)
    *(_T59 + 4) = _T61
    _T62 = *(_T59 + 0)
    _T63 = *(_T59 + 4)
    parm _T62
    call _PrintInt
    _T64 = "+"
    parm _T64
    call _PrintString
    parm _T63
    call _PrintInt
    _T65 = "j"
    parm _T65
    call _PrintString
    _T66 = "\n"
    parm _T66
    call _PrintString
    _T67 = *(_T3 + 0)
    _T68 = *(_T3 + 4)
    _T69 = *(_T4 + 0)
    _T70 = *(_T4 + 4)
    _T71 = 8
    parm _T71
    _T72 =  call _Alloc
    _T73 = (_T67 + _T69)
    *(_T72 + 0) = _T73
    _T74 = (_T68 + _T70)
    *(_T72 + 4) = _T74
    _T75 = *(_T72 + 0)
    _T76 = *(_T72 + 4)
    parm _T75
    call _PrintInt
    _T77 = "+"
    parm _T77
    call _PrintString
    parm _T76
    call _PrintInt
    _T78 = "j"
    parm _T78
    call _PrintString
    _T79 = *(_T5 + 0)
    _T80 = *(_T5 + 4)
    parm _T79
    call _PrintInt
    _T81 = "+"
    parm _T81
    call _PrintString
    parm _T80
    call _PrintInt
    _T82 = "j"
    parm _T82
    call _PrintString
    _T83 = "\n"
    parm _T83
    call _PrintString
    _T84 = *(_T3 + 0)
    _T85 = *(_T3 + 4)
    _T86 = *(_T4 + 0)
    _T87 = *(_T4 + 4)
    _T88 = 8
    parm _T88
    _T89 =  call _Alloc
    _T90 = (_T84 + _T86)
    *(_T89 + 0) = _T90
    _T91 = (_T85 + _T87)
    *(_T89 + 4) = _T91
    _T5 = _T89
    _T92 = *(_T3 + 0)
    _T93 = *(_T3 + 4)
    _T94 = 0
    _T95 = 8
    parm _T95
    _T96 =  call _Alloc
    _T97 = (_T92 + _T7)
    *(_T96 + 0) = _T97
    _T98 = (_T93 + _T94)
    *(_T96 + 4) = _T98
    _T5 = _T96
    _T99 = 0
    _T100 = 0
    _T101 = 8
    parm _T101
    _T102 =  call _Alloc
    *(_T102 + 0) = _T99
    *(_T102 + 4) = _T100
    _T103 = *(_T3 + 0)
    _T104 = *(_T3 + 4)
    _T105 = *(_T102 + 0)
    _T106 = *(_T102 + 4)
    _T107 = 8
    parm _T107
    _T108 =  call _Alloc
    _T109 = (_T103 + _T105)
    *(_T108 + 0) = _T109
    _T110 = (_T104 + _T106)
    *(_T108 + 4) = _T110
    _T5 = _T108
    _T111 = 0
    _T112 = 0
    _T113 = 8
    parm _T113
    _T114 =  call _Alloc
    *(_T114 + 0) = _T111
    *(_T114 + 4) = _T112
    _T115 = *(_T114 + 0)
    _T116 = *(_T114 + 4)
    _T117 = 0
    _T118 = 8
    parm _T118
    _T119 =  call _Alloc
    _T120 = (_T115 + _T7)
    *(_T119 + 0) = _T120
    _T121 = (_T116 + _T117)
    *(_T119 + 4) = _T121
    _T5 = _T119
    _T122 = 4
    _T123 = (_T122 + _T7)
    _T10 = _T123
    parm _T10
    call _PrintInt
    _T124 = "\n"
    parm _T124
    call _PrintString
    _T125 = *(_T5 + 0)
    _T126 = *(_T5 + 4)
    parm _T125
    call _PrintInt
    _T127 = "+"
    parm _T127
    call _PrintString
    parm _T126
    call _PrintInt
    _T128 = "j"
    parm _T128
    call _PrintString
    _T129 = "\n"
    parm _T129
    call _PrintString
    _T130 = *(_T3 + 0)
    _T131 = *(_T3 + 4)
    _T132 = *(_T4 + 0)
    _T133 = *(_T4 + 4)
    _T134 = 8
    parm _T134
    _T135 =  call _Alloc
    _T136 = (_T130 * _T132)
    _T137 = (_T131 * _T133)
    _T138 = (_T136 - _T137)
    *(_T135 + 0) = _T138
    _T139 = (_T130 * _T133)
    _T140 = (_T132 * _T131)
    _T141 = (_T139 - _T140)
    *(_T135 + 4) = _T141
    _T5 = _T135
    _T142 = *(_T3 + 0)
    _T143 = *(_T3 + 4)
    _T144 = 0
    _T145 = 8
    parm _T145
    _T146 =  call _Alloc
    _T147 = (_T142 * _T7)
    _T148 = (_T143 * _T144)
    _T149 = (_T147 - _T148)
    *(_T146 + 0) = _T149
    _T150 = (_T142 * _T144)
    _T151 = (_T7 * _T143)
    _T152 = (_T150 - _T151)
    *(_T146 + 4) = _T152
    _T5 = _T146
    _T153 = 0
    _T154 = 0
    _T155 = 8
    parm _T155
    _T156 =  call _Alloc
    *(_T156 + 0) = _T153
    *(_T156 + 4) = _T154
    _T157 = *(_T3 + 0)
    _T158 = *(_T3 + 4)
    _T159 = *(_T156 + 0)
    _T160 = *(_T156 + 4)
    _T161 = 8
    parm _T161
    _T162 =  call _Alloc
    _T163 = (_T157 * _T159)
    _T164 = (_T158 * _T160)
    _T165 = (_T163 - _T164)
    *(_T162 + 0) = _T165
    _T166 = (_T157 * _T160)
    _T167 = (_T159 * _T158)
    _T168 = (_T166 - _T167)
    *(_T162 + 4) = _T168
    _T5 = _T162
    _T169 = 0
    _T170 = 0
    _T171 = 8
    parm _T171
    _T172 =  call _Alloc
    *(_T172 + 0) = _T169
    *(_T172 + 4) = _T170
    _T173 = *(_T172 + 0)
    _T174 = *(_T172 + 4)
    _T175 = 0
    _T176 = 8
    parm _T176
    _T177 =  call _Alloc
    _T178 = (_T173 * _T7)
    _T179 = (_T174 * _T175)
    _T180 = (_T178 - _T179)
    *(_T177 + 0) = _T180
    _T181 = (_T173 * _T175)
    _T182 = (_T7 * _T174)
    _T183 = (_T181 - _T182)
    *(_T177 + 4) = _T183
    _T5 = _T177
    _T184 = 4
    _T185 = (_T184 * _T7)
    _T10 = _T185
    parm _T10
    call _PrintInt
    _T186 = "\n"
    parm _T186
    call _PrintString
    _T187 = *(_T5 + 0)
    _T188 = *(_T5 + 4)
    parm _T187
    call _PrintInt
    _T189 = "+"
    parm _T189
    call _PrintString
    parm _T188
    call _PrintInt
    _T190 = "j"
    parm _T190
    call _PrintString
    _T191 = "\n"
    parm _T191
    call _PrintString
}

