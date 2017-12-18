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
    _T108 = *(_T107 + 0)
    *(_T10 + 0) = _T108
    parm _T10
    _T109 = *(_T10 + 0)
    _T110 = *(_T109 + 16)
    call _T110
    *(_T10 + 0) = _T107
    parm _T10
    _T111 = *(_T10 + 0)
    _T112 = *(_T111 + 12)
    call _T112
}

FUNCTION(_B.fun) {
memo '_T11:4'
_B.fun:
    _T113 = "B"
    parm _T113
    call _PrintString
    _T114 = *(_T11 + 0)
    _T115 = *(_T114 + 0)
    *(_T11 + 0) = _T115
    parm _T11
    _T116 = *(_T11 + 0)
    _T117 = *(_T116 + 16)
    call _T117
    *(_T11 + 0) = _T114
    parm _T11
    _T118 = *(_T11 + 0)
    _T119 = *(_T118 + 12)
    call _T119
    _T120 = "\n"
    parm _T120
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T12:4 _T13:8 _T14:12'
_C.setC:
    _T121 = *(_T12 + 12)
    *(_T12 + 12) = _T13
    _T122 = *(_T12 + 16)
    *(_T12 + 16) = _T14
}

FUNCTION(_C.print) {
memo '_T15:4'
_C.print:
    _T123 = " c="
    parm _T123
    call _PrintString
    _T124 = *(_T15 + 12)
    parm _T124
    call _PrintInt
    _T125 = " c1="
    parm _T125
    call _PrintString
    _T126 = *(_T15 + 16)
    parm _T126
    call _PrintInt
    _T127 = " "
    parm _T127
    call _PrintString
}

FUNCTION(_C.allprint) {
memo '_T16:4'
_C.allprint:
    parm _T16
    _T128 = *(_T16 + 0)
    _T129 = *(_T128 + 12)
    call _T129
}

FUNCTION(_C.fun) {
memo '_T17:4'
_C.fun:
    _T130 = "C"
    parm _T130
    call _PrintString
    _T131 = *(_T17 + 0)
    _T132 = *(_T131 + 0)
    *(_T17 + 0) = _T132
    parm _T17
    _T133 = *(_T17 + 0)
    _T134 = *(_T133 + 16)
    call _T134
    *(_T17 + 0) = _T131
    parm _T17
    _T135 = *(_T17 + 0)
    _T136 = *(_T135 + 12)
    call _T136
    _T137 = "\n"
    parm _T137
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T18:4 _T19:8 _T20:12'
_D.setD:
    _T138 = *(_T18 + 20)
    *(_T18 + 20) = _T19
    _T139 = *(_T18 + 24)
    *(_T18 + 24) = _T20
}

FUNCTION(_D.print) {
memo '_T21:4'
_D.print:
    _T140 = " d="
    parm _T140
    call _PrintString
    _T141 = *(_T21 + 20)
    parm _T141
    call _PrintInt
    _T142 = " d1="
    parm _T142
    call _PrintString
    _T143 = *(_T21 + 24)
    parm _T143
    call _PrintInt
    _T144 = " "
    parm _T144
    call _PrintString
}

FUNCTION(_D.allprint) {
memo '_T22:4'
_D.allprint:
    _T145 = *(_T22 + 0)
    _T146 = *(_T145 + 0)
    *(_T22 + 0) = _T146
    parm _T22
    _T147 = *(_T22 + 0)
    _T148 = *(_T147 + 16)
    call _T148
    *(_T22 + 0) = _T145
    parm _T22
    _T149 = *(_T22 + 0)
    _T150 = *(_T149 + 12)
    call _T150
}

FUNCTION(_D.fun) {
memo '_T23:4'
_D.fun:
    _T151 = "D"
    parm _T151
    call _PrintString
    _T152 = *(_T23 + 0)
    _T153 = *(_T152 + 0)
    *(_T23 + 0) = _T153
    parm _T23
    _T154 = *(_T23 + 0)
    _T155 = *(_T154 + 16)
    call _T155
    *(_T23 + 0) = _T152
    parm _T23
    _T156 = *(_T23 + 0)
    _T157 = *(_T156 + 12)
    call _T157
    _T158 = "\n"
    parm _T158
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T24:4 _T25:8 _T26:12'
_E.setE:
    _T159 = *(_T24 + 20)
    *(_T24 + 20) = _T25
    _T160 = *(_T24 + 24)
    *(_T24 + 24) = _T26
}

FUNCTION(_E.print) {
memo '_T27:4'
_E.print:
    _T161 = " e="
    parm _T161
    call _PrintString
    _T162 = *(_T27 + 20)
    parm _T162
    call _PrintInt
    _T163 = " e1="
    parm _T163
    call _PrintString
    _T164 = *(_T27 + 24)
    parm _T164
    call _PrintInt
    _T165 = " "
    parm _T165
    call _PrintString
}

FUNCTION(_E.fun) {
memo '_T28:4'
_E.fun:
    _T166 = "E"
    parm _T166
    call _PrintString
    parm _T28
    _T167 = *(_T28 + 0)
    _T168 = *(_T167 + 16)
    call _T168
    parm _T28
    _T169 = *(_T28 + 0)
    _T170 = *(_T169 + 12)
    call _T170
    _T171 = "\n"
    parm _T171
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T29:4 _T30:8 _T31:12'
_F.setF:
    _T172 = *(_T29 + 28)
    *(_T29 + 28) = _T30
    _T173 = *(_T29 + 32)
    *(_T29 + 32) = _T31
}

FUNCTION(_F.print) {
memo '_T32:4'
_F.print:
    _T174 = " f="
    parm _T174
    call _PrintString
    _T175 = *(_T32 + 28)
    parm _T175
    call _PrintInt
    _T176 = " f1="
    parm _T176
    call _PrintString
    _T177 = *(_T32 + 32)
    parm _T177
    call _PrintInt
    _T178 = " "
    parm _T178
    call _PrintString
}

FUNCTION(_F.allprint) {
memo '_T33:4'
_F.allprint:
    _T179 = *(_T33 + 0)
    _T180 = *(_T179 + 0)
    *(_T33 + 0) = _T180
    parm _T33
    _T181 = *(_T33 + 0)
    _T182 = *(_T181 + 16)
    call _T182
    *(_T33 + 0) = _T179
    parm _T33
    _T183 = *(_T33 + 0)
    _T184 = *(_T183 + 12)
    call _T184
}

FUNCTION(_F.fun) {
memo '_T34:4'
_F.fun:
    _T185 = "F"
    parm _T185
    call _PrintString
    _T186 = *(_T34 + 0)
    _T187 = *(_T186 + 0)
    *(_T34 + 0) = _T187
    parm _T34
    _T188 = *(_T34 + 0)
    _T189 = *(_T188 + 16)
    call _T189
    *(_T34 + 0) = _T186
    parm _T34
    _T190 = *(_T34 + 0)
    _T191 = *(_T190 + 12)
    call _T191
    _T192 = "\n"
    parm _T192
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T35:4 _T36:8'
_G.setG:
    _T193 = *(_T35 + 20)
    *(_T35 + 20) = _T36
}

FUNCTION(_G.print) {
memo '_T37:4'
_G.print:
    _T194 = " g="
    parm _T194
    call _PrintString
    _T195 = *(_T37 + 20)
    parm _T195
    call _PrintInt
}

FUNCTION(_G.allprint) {
memo '_T38:4'
_G.allprint:
    _T196 = *(_T38 + 0)
    _T197 = *(_T196 + 0)
    *(_T38 + 0) = _T197
    parm _T38
    _T198 = *(_T38 + 0)
    _T199 = *(_T198 + 16)
    call _T199
    *(_T38 + 0) = _T196
    parm _T38
    _T200 = *(_T38 + 0)
    _T201 = *(_T200 + 12)
    call _T201
}

FUNCTION(_G.fun) {
memo '_T39:4'
_G.fun:
    _T202 = "G"
    parm _T202
    call _PrintString
    _T203 = *(_T39 + 0)
    _T204 = *(_T203 + 0)
    *(_T39 + 0) = _T204
    parm _T39
    _T205 = *(_T39 + 0)
    _T206 = *(_T205 + 16)
    call _T206
    *(_T39 + 0) = _T203
    parm _T39
    _T207 = *(_T39 + 0)
    _T208 = *(_T207 + 12)
    call _T208
    _T209 = "\n"
    parm _T209
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T217 =  call _A_New
    _T210 = _T217
    _T218 =  call _B_New
    _T211 = _T218
    _T219 =  call _C_New
    _T212 = _T219
    _T220 =  call _D_New
    _T213 = _T220
    _T221 =  call _E_New
    _T214 = _T221
    _T222 =  call _F_New
    _T215 = _T222
    _T223 =  call _G_New
    _T216 = _T223
    _T224 = 10
    _T225 = 11
    parm _T210
    parm _T224
    parm _T225
    _T226 = *(_T210 + 0)
    _T227 = *(_T226 + 8)
    call _T227
    _T228 = 20
    _T229 = 21
    parm _T211
    parm _T228
    parm _T229
    _T230 = *(_T211 + 0)
    _T231 = *(_T230 + 8)
    call _T231
    _T232 = 22
    _T233 = 23
    parm _T211
    parm _T232
    parm _T233
    _T234 = *(_T211 + 0)
    _T235 = *(_T234 + 24)
    call _T235
    _T236 = 30
    _T237 = 31
    parm _T212
    parm _T236
    parm _T237
    _T238 = *(_T212 + 0)
    _T239 = *(_T238 + 8)
    call _T239
    _T240 = 32
    _T241 = 33
    parm _T212
    parm _T240
    parm _T241
    _T242 = *(_T212 + 0)
    _T243 = *(_T242 + 24)
    call _T243
    _T244 = 40
    _T245 = 41
    parm _T213
    parm _T244
    parm _T245
    _T246 = *(_T213 + 0)
    _T247 = *(_T246 + 8)
    call _T247
    _T248 = 42
    _T249 = 43
    parm _T213
    parm _T248
    parm _T249
    _T250 = *(_T213 + 0)
    _T251 = *(_T250 + 24)
    call _T251
    _T252 = 44
    _T253 = 45
    parm _T213
    parm _T252
    parm _T253
    _T254 = *(_T213 + 0)
    _T255 = *(_T254 + 28)
    call _T255
    _T256 = 50
    _T257 = 51
    parm _T214
    parm _T256
    parm _T257
    _T258 = *(_T214 + 0)
    _T259 = *(_T258 + 8)
    call _T259
    _T260 = 52
    _T261 = 53
    parm _T214
    parm _T260
    parm _T261
    _T262 = *(_T214 + 0)
    _T263 = *(_T262 + 24)
    call _T263
    _T264 = 54
    _T265 = 55
    parm _T214
    parm _T264
    parm _T265
    _T266 = *(_T214 + 0)
    _T267 = *(_T266 + 28)
    call _T267
    _T268 = 60
    _T269 = 61
    parm _T215
    parm _T268
    parm _T269
    _T270 = *(_T215 + 0)
    _T271 = *(_T270 + 8)
    call _T271
    _T272 = 62
    _T273 = 63
    parm _T215
    parm _T272
    parm _T273
    _T274 = *(_T215 + 0)
    _T275 = *(_T274 + 24)
    call _T275
    _T276 = 64
    _T277 = 65
    parm _T215
    parm _T276
    parm _T277
    _T278 = *(_T215 + 0)
    _T279 = *(_T278 + 28)
    call _T279
    _T280 = 66
    _T281 = 67
    parm _T215
    parm _T280
    parm _T281
    _T282 = *(_T215 + 0)
    _T283 = *(_T282 + 32)
    call _T283
    _T284 = 70
    _T285 = 71
    parm _T216
    parm _T284
    parm _T285
    _T286 = *(_T216 + 0)
    _T287 = *(_T286 + 8)
    call _T287
    _T288 = 72
    _T289 = 73
    parm _T216
    parm _T288
    parm _T289
    _T290 = *(_T216 + 0)
    _T291 = *(_T290 + 24)
    call _T291
    _T292 = 74
    parm _T216
    parm _T292
    _T293 = *(_T216 + 0)
    _T294 = *(_T293 + 28)
    call _T294
    parm _T210
    _T295 = *(_T210 + 0)
    _T296 = *(_T295 + 20)
    call _T296
    parm _T211
    _T297 = *(_T211 + 0)
    _T298 = *(_T297 + 20)
    call _T298
    parm _T212
    _T299 = *(_T212 + 0)
    _T300 = *(_T299 + 20)
    call _T300
    parm _T213
    _T301 = *(_T213 + 0)
    _T302 = *(_T301 + 20)
    call _T302
    parm _T214
    _T303 = *(_T214 + 0)
    _T304 = *(_T303 + 20)
    call _T304
    parm _T215
    _T305 = *(_T215 + 0)
    _T306 = *(_T305 + 20)
    call _T306
    parm _T216
    _T307 = *(_T216 + 0)
    _T308 = *(_T307 + 20)
    call _T308
}

