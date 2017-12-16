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

VTABLE(_E) {
    _C
    E
    _A.setA;
    _E.print;
    _C.allprint;
    _E.fun;
    _C.setC;
    _E.setE;
}

VTABLE(_F) {
    _E
    F
    _A.setA;
    _F.print;
    _F.allprint;
    _F.fun;
    _C.setC;
    _E.setE;
    _F.setF;
}

VTABLE(_G) {
    _C
    G
    _A.setA;
    _G.print;
    _G.allprint;
    _G.fun;
    _C.setC;
    _G.setG;
}

VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T40 = 12
    parm _T40
    _T41 =  call _Alloc
    _T42 = 0
    *(_T41 + 4) = _T42
    *(_T41 + 8) = _T42
    _T43 = VTBL <_A>
    *(_T41 + 0) = _T43
    return _T41
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T44 = 20
    parm _T44
    _T45 =  call _Alloc
    _T46 = 0
    *(_T45 + 4) = _T46
    *(_T45 + 8) = _T46
    *(_T45 + 12) = _T46
    *(_T45 + 16) = _T46
    _T47 = VTBL <_B>
    *(_T45 + 0) = _T47
    return _T45
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T48 = 20
    parm _T48
    _T49 =  call _Alloc
    _T50 = 0
    *(_T49 + 4) = _T50
    *(_T49 + 8) = _T50
    *(_T49 + 12) = _T50
    *(_T49 + 16) = _T50
    _T51 = VTBL <_C>
    *(_T49 + 0) = _T51
    return _T49
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T52 = 28
    parm _T52
    _T53 =  call _Alloc
    _T54 = 0
    _T55 = 4
    _T56 = (_T53 + _T52)
_L40:
    _T57 = (_T56 - _T55)
    _T56 = _T57
    _T58 = (_T52 - _T55)
    _T52 = _T58
    if (_T52 == 0) branch _L41
    *(_T56 + 0) = _T54
    branch _L40
_L41:
    _T59 = VTBL <_D>
    *(_T56 + 0) = _T59
    return _T56
}

FUNCTION(_E_New) {
memo ''
_E_New:
    _T60 = 28
    parm _T60
    _T61 =  call _Alloc
    _T62 = 0
    _T63 = 4
    _T64 = (_T61 + _T60)
_L43:
    _T65 = (_T64 - _T63)
    _T64 = _T65
    _T66 = (_T60 - _T63)
    _T60 = _T66
    if (_T60 == 0) branch _L44
    *(_T64 + 0) = _T62
    branch _L43
_L44:
    _T67 = VTBL <_E>
    *(_T64 + 0) = _T67
    return _T64
}

FUNCTION(_F_New) {
memo ''
_F_New:
    _T68 = 36
    parm _T68
    _T69 =  call _Alloc
    _T70 = 0
    _T71 = 4
    _T72 = (_T69 + _T68)
_L46:
    _T73 = (_T72 - _T71)
    _T72 = _T73
    _T74 = (_T68 - _T71)
    _T68 = _T74
    if (_T68 == 0) branch _L47
    *(_T72 + 0) = _T70
    branch _L46
_L47:
    _T75 = VTBL <_F>
    *(_T72 + 0) = _T75
    return _T72
}

FUNCTION(_G_New) {
memo ''
_G_New:
    _T76 = 24
    parm _T76
    _T77 =  call _Alloc
    _T78 = 0
    _T79 = 4
    _T80 = (_T77 + _T76)
_L49:
    _T81 = (_T80 - _T79)
    _T80 = _T81
    _T82 = (_T76 - _T79)
    _T76 = _T82
    if (_T76 == 0) branch _L50
    *(_T80 + 0) = _T78
    branch _L49
_L50:
    _T83 = VTBL <_G>
    *(_T80 + 0) = _T83
    return _T80
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T84 = 4
    parm _T84
    _T85 =  call _Alloc
    _T86 = VTBL <_Main>
    *(_T85 + 0) = _T86
    return _T85
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T87 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T88 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T89 = " a="
    parm _T89
    call _PrintString
    _T90 = *(_T3 + 4)
    parm _T90
    call _PrintInt
    _T91 = " a1="
    parm _T91
    call _PrintString
    _T92 = *(_T3 + 8)
    parm _T92
    call _PrintInt
    _T93 = " "
    parm _T93
    call _PrintString
}

FUNCTION(_A.allprint) {
memo '_T4:4'
_A.allprint:
    parm _T4
    _T94 = *(_T4 + 0)
    _T95 = *(_T94 + 12)
    call _T95
}

FUNCTION(_A.fun) {
memo '_T5:4'
_A.fun:
    _T96 = "A"
    parm _T96
    call _PrintString
    parm _T5
    _T97 = *(_T5 + 0)
    _T98 = *(_T97 + 12)
    call _T98
    _T99 = "\n"
    parm _T99
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T6:4 _T7:8 _T8:12'
_B.setB:
    _T100 = *(_T6 + 12)
    *(_T6 + 12) = _T7
    _T101 = *(_T6 + 16)
    *(_T6 + 16) = _T8
}

FUNCTION(_B.print) {
memo '_T9:4'
_B.print:
    _T102 = " b="
    parm _T102
    call _PrintString
    _T103 = *(_T9 + 12)
    parm _T103
    call _PrintInt
    _T104 = " b1="
    parm _T104
    call _PrintString
    _T105 = *(_T9 + 16)
    parm _T105
    call _PrintInt
    _T106 = " "
    parm _T106
    call _PrintString
}

FUNCTION(_B.allprint) {
memo '_T10:4'
_B.allprint:
    _T107 = *(_T10 + 0)
    parm _T107
    _T108 = *(_T107 + 0)
    _T109 = *(_T108 + 16)
    call _T109
    parm _T10
    _T110 = *(_T10 + 0)
    _T111 = *(_T110 + 12)
    call _T111
}

FUNCTION(_B.fun) {
memo '_T11:4'
_B.fun:
    _T112 = "B"
    parm _T112
    call _PrintString
    _T113 = *(_T11 + 0)
    parm _T113
    _T114 = *(_T113 + 0)
    _T115 = *(_T114 + 16)
    call _T115
    parm _T11
    _T116 = *(_T11 + 0)
    _T117 = *(_T116 + 12)
    call _T117
    _T118 = "\n"
    parm _T118
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T12:4 _T13:8 _T14:12'
_C.setC:
    _T119 = *(_T12 + 12)
    *(_T12 + 12) = _T13
    _T120 = *(_T12 + 16)
    *(_T12 + 16) = _T14
}

FUNCTION(_C.print) {
memo '_T15:4'
_C.print:
    _T121 = " c="
    parm _T121
    call _PrintString
    _T122 = *(_T15 + 12)
    parm _T122
    call _PrintInt
    _T123 = " c1="
    parm _T123
    call _PrintString
    _T124 = *(_T15 + 16)
    parm _T124
    call _PrintInt
    _T125 = " "
    parm _T125
    call _PrintString
}

FUNCTION(_C.allprint) {
memo '_T16:4'
_C.allprint:
    parm _T16
    _T126 = *(_T16 + 0)
    _T127 = *(_T126 + 12)
    call _T127
}

FUNCTION(_C.fun) {
memo '_T17:4'
_C.fun:
    _T128 = "C"
    parm _T128
    call _PrintString
    _T129 = *(_T17 + 0)
    parm _T129
    _T130 = *(_T129 + 0)
    _T131 = *(_T130 + 16)
    call _T131
    parm _T17
    _T132 = *(_T17 + 0)
    _T133 = *(_T132 + 12)
    call _T133
    _T134 = "\n"
    parm _T134
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T18:4 _T19:8 _T20:12'
_D.setD:
    _T135 = *(_T18 + 20)
    *(_T18 + 20) = _T19
    _T136 = *(_T18 + 24)
    *(_T18 + 24) = _T20
}

FUNCTION(_D.print) {
memo '_T21:4'
_D.print:
    _T137 = " d="
    parm _T137
    call _PrintString
    _T138 = *(_T21 + 20)
    parm _T138
    call _PrintInt
    _T139 = " d1="
    parm _T139
    call _PrintString
    _T140 = *(_T21 + 24)
    parm _T140
    call _PrintInt
    _T141 = " "
    parm _T141
    call _PrintString
}

FUNCTION(_D.allprint) {
memo '_T22:4'
_D.allprint:
    _T142 = *(_T22 + 0)
    parm _T142
    _T143 = *(_T142 + 0)
    _T144 = *(_T143 + 16)
    call _T144
    parm _T22
    _T145 = *(_T22 + 0)
    _T146 = *(_T145 + 12)
    call _T146
}

FUNCTION(_D.fun) {
memo '_T23:4'
_D.fun:
    _T147 = "D"
    parm _T147
    call _PrintString
    _T148 = *(_T23 + 0)
    parm _T148
    _T149 = *(_T148 + 0)
    _T150 = *(_T149 + 16)
    call _T150
    parm _T23
    _T151 = *(_T23 + 0)
    _T152 = *(_T151 + 12)
    call _T152
    _T153 = "\n"
    parm _T153
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T24:4 _T25:8 _T26:12'
_E.setE:
    _T154 = *(_T24 + 20)
    *(_T24 + 20) = _T25
    _T155 = *(_T24 + 24)
    *(_T24 + 24) = _T26
}

FUNCTION(_E.print) {
memo '_T27:4'
_E.print:
    _T156 = " e="
    parm _T156
    call _PrintString
    _T157 = *(_T27 + 20)
    parm _T157
    call _PrintInt
    _T158 = " e1="
    parm _T158
    call _PrintString
    _T159 = *(_T27 + 24)
    parm _T159
    call _PrintInt
    _T160 = " "
    parm _T160
    call _PrintString
}

FUNCTION(_E.fun) {
memo '_T28:4'
_E.fun:
    _T161 = "E"
    parm _T161
    call _PrintString
    parm _T28
    _T162 = *(_T28 + 0)
    _T163 = *(_T162 + 16)
    call _T163
    parm _T28
    _T164 = *(_T28 + 0)
    _T165 = *(_T164 + 12)
    call _T165
    _T166 = "\n"
    parm _T166
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T29:4 _T30:8 _T31:12'
_F.setF:
    _T167 = *(_T29 + 28)
    *(_T29 + 28) = _T30
    _T168 = *(_T29 + 32)
    *(_T29 + 32) = _T31
}

FUNCTION(_F.print) {
memo '_T32:4'
_F.print:
    _T169 = " f="
    parm _T169
    call _PrintString
    _T170 = *(_T32 + 28)
    parm _T170
    call _PrintInt
    _T171 = " f1="
    parm _T171
    call _PrintString
    _T172 = *(_T32 + 32)
    parm _T172
    call _PrintInt
    _T173 = " "
    parm _T173
    call _PrintString
}

FUNCTION(_F.allprint) {
memo '_T33:4'
_F.allprint:
    _T174 = *(_T33 + 0)
    parm _T174
    _T175 = *(_T174 + 0)
    _T176 = *(_T175 + 16)
    call _T176
    parm _T33
    _T177 = *(_T33 + 0)
    _T178 = *(_T177 + 12)
    call _T178
}

FUNCTION(_F.fun) {
memo '_T34:4'
_F.fun:
    _T179 = "F"
    parm _T179
    call _PrintString
    _T180 = *(_T34 + 0)
    parm _T180
    _T181 = *(_T180 + 0)
    _T182 = *(_T181 + 16)
    call _T182
    parm _T34
    _T183 = *(_T34 + 0)
    _T184 = *(_T183 + 12)
    call _T184
    _T185 = "\n"
    parm _T185
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T35:4 _T36:8'
_G.setG:
    _T186 = *(_T35 + 20)
    *(_T35 + 20) = _T36
}

FUNCTION(_G.print) {
memo '_T37:4'
_G.print:
    _T187 = " g="
    parm _T187
    call _PrintString
    _T188 = *(_T37 + 20)
    parm _T188
    call _PrintInt
}

FUNCTION(_G.allprint) {
memo '_T38:4'
_G.allprint:
    _T189 = *(_T38 + 0)
    parm _T189
    _T190 = *(_T189 + 0)
    _T191 = *(_T190 + 16)
    call _T191
    parm _T38
    _T192 = *(_T38 + 0)
    _T193 = *(_T192 + 12)
    call _T193
}

FUNCTION(_G.fun) {
memo '_T39:4'
_G.fun:
    _T194 = "G"
    parm _T194
    call _PrintString
    _T195 = *(_T39 + 0)
    parm _T195
    _T196 = *(_T195 + 0)
    _T197 = *(_T196 + 16)
    call _T197
    parm _T39
    _T198 = *(_T39 + 0)
    _T199 = *(_T198 + 12)
    call _T199
    _T200 = "\n"
    parm _T200
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T208 =  call _A_New
    _T201 = _T208
    _T209 =  call _B_New
    _T202 = _T209
    _T210 =  call _C_New
    _T203 = _T210
    _T211 =  call _D_New
    _T204 = _T211
    _T212 =  call _E_New
    _T205 = _T212
    _T213 =  call _F_New
    _T206 = _T213
    _T214 =  call _G_New
    _T207 = _T214
    _T215 = 10
    _T216 = 11
    parm _T201
    parm _T215
    parm _T216
    _T217 = *(_T201 + 0)
    _T218 = *(_T217 + 8)
    call _T218
    _T219 = 20
    _T220 = 21
    parm _T202
    parm _T219
    parm _T220
    _T221 = *(_T202 + 0)
    _T222 = *(_T221 + 8)
    call _T222
    _T223 = 22
    _T224 = 23
    parm _T202
    parm _T223
    parm _T224
    _T225 = *(_T202 + 0)
    _T226 = *(_T225 + 24)
    call _T226
    _T227 = 30
    _T228 = 31
    parm _T203
    parm _T227
    parm _T228
    _T229 = *(_T203 + 0)
    _T230 = *(_T229 + 8)
    call _T230
    _T231 = 32
    _T232 = 33
    parm _T203
    parm _T231
    parm _T232
    _T233 = *(_T203 + 0)
    _T234 = *(_T233 + 24)
    call _T234
    _T235 = 40
    _T236 = 41
    parm _T204
    parm _T235
    parm _T236
    _T237 = *(_T204 + 0)
    _T238 = *(_T237 + 8)
    call _T238
    _T239 = 42
    _T240 = 43
    parm _T204
    parm _T239
    parm _T240
    _T241 = *(_T204 + 0)
    _T242 = *(_T241 + 24)
    call _T242
    _T243 = 44
    _T244 = 45
    parm _T204
    parm _T243
    parm _T244
    _T245 = *(_T204 + 0)
    _T246 = *(_T245 + 28)
    call _T246
    _T247 = 50
    _T248 = 51
    parm _T205
    parm _T247
    parm _T248
    _T249 = *(_T205 + 0)
    _T250 = *(_T249 + 8)
    call _T250
    _T251 = 52
    _T252 = 53
    parm _T205
    parm _T251
    parm _T252
    _T253 = *(_T205 + 0)
    _T254 = *(_T253 + 24)
    call _T254
    _T255 = 54
    _T256 = 55
    parm _T205
    parm _T255
    parm _T256
    _T257 = *(_T205 + 0)
    _T258 = *(_T257 + 28)
    call _T258
    _T259 = 60
    _T260 = 61
    parm _T206
    parm _T259
    parm _T260
    _T261 = *(_T206 + 0)
    _T262 = *(_T261 + 8)
    call _T262
    _T263 = 62
    _T264 = 63
    parm _T206
    parm _T263
    parm _T264
    _T265 = *(_T206 + 0)
    _T266 = *(_T265 + 24)
    call _T266
    _T267 = 64
    _T268 = 65
    parm _T206
    parm _T267
    parm _T268
    _T269 = *(_T206 + 0)
    _T270 = *(_T269 + 28)
    call _T270
    _T271 = 66
    _T272 = 67
    parm _T206
    parm _T271
    parm _T272
    _T273 = *(_T206 + 0)
    _T274 = *(_T273 + 32)
    call _T274
    _T275 = 70
    _T276 = 71
    parm _T207
    parm _T275
    parm _T276
    _T277 = *(_T207 + 0)
    _T278 = *(_T277 + 8)
    call _T278
    _T279 = 72
    _T280 = 73
    parm _T207
    parm _T279
    parm _T280
    _T281 = *(_T207 + 0)
    _T282 = *(_T281 + 24)
    call _T282
    _T283 = 74
    parm _T207
    parm _T283
    _T284 = *(_T207 + 0)
    _T285 = *(_T284 + 28)
    call _T285
    parm _T201
    _T286 = *(_T201 + 0)
    _T287 = *(_T286 + 20)
    call _T287
    parm _T202
    _T288 = *(_T202 + 0)
    _T289 = *(_T288 + 20)
    call _T289
    parm _T203
    _T290 = *(_T203 + 0)
    _T291 = *(_T290 + 20)
    call _T291
    parm _T204
    _T292 = *(_T204 + 0)
    _T293 = *(_T292 + 20)
    call _T293
    parm _T205
    _T294 = *(_T205 + 0)
    _T295 = *(_T294 + 20)
    call _T295
    parm _T206
    _T296 = *(_T206 + 0)
    _T297 = *(_T296 + 20)
    call _T297
    parm _T207
    _T298 = *(_T207 + 0)
    _T299 = *(_T298 + 20)
    call _T299
}

