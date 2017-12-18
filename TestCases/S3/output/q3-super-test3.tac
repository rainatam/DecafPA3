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
    _E.allprint;
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
    _T41 = 12
    parm _T41
    _T42 =  call _Alloc
    _T43 = 0
    *(_T42 + 4) = _T43
    *(_T42 + 8) = _T43
    _T44 = VTBL <_A>
    *(_T42 + 0) = _T44
    return _T42
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T45 = 20
    parm _T45
    _T46 =  call _Alloc
    _T47 = 0
    *(_T46 + 4) = _T47
    *(_T46 + 8) = _T47
    *(_T46 + 12) = _T47
    *(_T46 + 16) = _T47
    _T48 = VTBL <_B>
    *(_T46 + 0) = _T48
    return _T46
}

FUNCTION(_C_New) {
memo ''
_C_New:
    _T49 = 20
    parm _T49
    _T50 =  call _Alloc
    _T51 = 0
    *(_T50 + 4) = _T51
    *(_T50 + 8) = _T51
    *(_T50 + 12) = _T51
    *(_T50 + 16) = _T51
    _T52 = VTBL <_C>
    *(_T50 + 0) = _T52
    return _T50
}

FUNCTION(_D_New) {
memo ''
_D_New:
    _T53 = 28
    parm _T53
    _T54 =  call _Alloc
    _T55 = 0
    _T56 = 4
    _T57 = (_T54 + _T53)
_L41:
    _T58 = (_T57 - _T56)
    _T57 = _T58
    _T59 = (_T53 - _T56)
    _T53 = _T59
    if (_T53 == 0) branch _L42
    *(_T57 + 0) = _T55
    branch _L41
_L42:
    _T60 = VTBL <_D>
    *(_T57 + 0) = _T60
    return _T57
}

FUNCTION(_E_New) {
memo ''
_E_New:
    _T61 = 28
    parm _T61
    _T62 =  call _Alloc
    _T63 = 0
    _T64 = 4
    _T65 = (_T62 + _T61)
_L44:
    _T66 = (_T65 - _T64)
    _T65 = _T66
    _T67 = (_T61 - _T64)
    _T61 = _T67
    if (_T61 == 0) branch _L45
    *(_T65 + 0) = _T63
    branch _L44
_L45:
    _T68 = VTBL <_E>
    *(_T65 + 0) = _T68
    return _T65
}

FUNCTION(_F_New) {
memo ''
_F_New:
    _T69 = 36
    parm _T69
    _T70 =  call _Alloc
    _T71 = 0
    _T72 = 4
    _T73 = (_T70 + _T69)
_L47:
    _T74 = (_T73 - _T72)
    _T73 = _T74
    _T75 = (_T69 - _T72)
    _T69 = _T75
    if (_T69 == 0) branch _L48
    *(_T73 + 0) = _T71
    branch _L47
_L48:
    _T76 = VTBL <_F>
    *(_T73 + 0) = _T76
    return _T73
}

FUNCTION(_G_New) {
memo ''
_G_New:
    _T77 = 24
    parm _T77
    _T78 =  call _Alloc
    _T79 = 0
    _T80 = 4
    _T81 = (_T78 + _T77)
_L50:
    _T82 = (_T81 - _T80)
    _T81 = _T82
    _T83 = (_T77 - _T80)
    _T77 = _T83
    if (_T77 == 0) branch _L51
    *(_T81 + 0) = _T79
    branch _L50
_L51:
    _T84 = VTBL <_G>
    *(_T81 + 0) = _T84
    return _T81
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T85 = 4
    parm _T85
    _T86 =  call _Alloc
    _T87 = VTBL <_Main>
    *(_T86 + 0) = _T87
    return _T86
}

FUNCTION(_A.setA) {
memo '_T0:4 _T1:8 _T2:12'
_A.setA:
    _T88 = *(_T0 + 4)
    *(_T0 + 4) = _T1
    _T89 = *(_T0 + 8)
    *(_T0 + 8) = _T2
}

FUNCTION(_A.print) {
memo '_T3:4'
_A.print:
    _T90 = " a="
    parm _T90
    call _PrintString
    _T91 = *(_T3 + 4)
    parm _T91
    call _PrintInt
    _T92 = " a1="
    parm _T92
    call _PrintString
    _T93 = *(_T3 + 8)
    parm _T93
    call _PrintInt
    _T94 = " "
    parm _T94
    call _PrintString
}

FUNCTION(_A.allprint) {
memo '_T4:4'
_A.allprint:
    parm _T4
    _T95 = *(_T4 + 0)
    _T96 = *(_T95 + 12)
    call _T96
}

FUNCTION(_A.fun) {
memo '_T5:4'
_A.fun:
    _T97 = "A"
    parm _T97
    call _PrintString
    parm _T5
    _T98 = *(_T5 + 0)
    _T99 = *(_T98 + 12)
    call _T99
    _T100 = "\n"
    parm _T100
    call _PrintString
}

FUNCTION(_B.setB) {
memo '_T6:4 _T7:8 _T8:12'
_B.setB:
    _T101 = *(_T6 + 12)
    *(_T6 + 12) = _T7
    _T102 = *(_T6 + 16)
    *(_T6 + 16) = _T8
}

FUNCTION(_B.print) {
memo '_T9:4'
_B.print:
    _T103 = " b="
    parm _T103
    call _PrintString
    _T104 = *(_T9 + 12)
    parm _T104
    call _PrintInt
    _T105 = " b1="
    parm _T105
    call _PrintString
    _T106 = *(_T9 + 16)
    parm _T106
    call _PrintInt
    _T107 = " "
    parm _T107
    call _PrintString
}

FUNCTION(_B.allprint) {
memo '_T10:4'
_B.allprint:
    _T108 = *(_T10 + 0)
    _T109 = *(_T108 + 0)
    *(_T10 + 0) = _T109
    parm _T10
    _T110 = *(_T10 + 0)
    _T111 = *(_T110 + 16)
    call _T111
    *(_T10 + 0) = _T108
    parm _T10
    _T112 = *(_T10 + 0)
    _T113 = *(_T112 + 12)
    call _T113
}

FUNCTION(_B.fun) {
memo '_T11:4'
_B.fun:
    _T114 = "B"
    parm _T114
    call _PrintString
    _T115 = *(_T11 + 0)
    _T116 = *(_T115 + 0)
    *(_T11 + 0) = _T116
    parm _T11
    _T117 = *(_T11 + 0)
    _T118 = *(_T117 + 16)
    call _T118
    *(_T11 + 0) = _T115
    parm _T11
    _T119 = *(_T11 + 0)
    _T120 = *(_T119 + 12)
    call _T120
    _T121 = "\n"
    parm _T121
    call _PrintString
}

FUNCTION(_C.setC) {
memo '_T12:4 _T13:8 _T14:12'
_C.setC:
    _T122 = *(_T12 + 12)
    *(_T12 + 12) = _T13
    _T123 = *(_T12 + 16)
    *(_T12 + 16) = _T14
}

FUNCTION(_C.print) {
memo '_T15:4'
_C.print:
    _T124 = " c="
    parm _T124
    call _PrintString
    _T125 = *(_T15 + 12)
    parm _T125
    call _PrintInt
    _T126 = " c1="
    parm _T126
    call _PrintString
    _T127 = *(_T15 + 16)
    parm _T127
    call _PrintInt
    _T128 = " "
    parm _T128
    call _PrintString
}

FUNCTION(_C.allprint) {
memo '_T16:4'
_C.allprint:
    _T129 = *(_T16 + 0)
    _T130 = *(_T129 + 0)
    *(_T16 + 0) = _T130
    parm _T16
    _T131 = *(_T16 + 0)
    _T132 = *(_T131 + 16)
    call _T132
    *(_T16 + 0) = _T129
    parm _T16
    _T133 = *(_T16 + 0)
    _T134 = *(_T133 + 12)
    call _T134
}

FUNCTION(_C.fun) {
memo '_T17:4'
_C.fun:
    _T135 = "C"
    parm _T135
    call _PrintString
    _T136 = *(_T17 + 0)
    _T137 = *(_T136 + 0)
    *(_T17 + 0) = _T137
    parm _T17
    _T138 = *(_T17 + 0)
    _T139 = *(_T138 + 16)
    call _T139
    *(_T17 + 0) = _T136
    parm _T17
    _T140 = *(_T17 + 0)
    _T141 = *(_T140 + 12)
    call _T141
    _T142 = "\n"
    parm _T142
    call _PrintString
}

FUNCTION(_D.setD) {
memo '_T18:4 _T19:8 _T20:12'
_D.setD:
    _T143 = *(_T18 + 20)
    *(_T18 + 20) = _T19
    _T144 = *(_T18 + 24)
    *(_T18 + 24) = _T20
}

FUNCTION(_D.print) {
memo '_T21:4'
_D.print:
    _T145 = " d="
    parm _T145
    call _PrintString
    _T146 = *(_T21 + 20)
    parm _T146
    call _PrintInt
    _T147 = " d1="
    parm _T147
    call _PrintString
    _T148 = *(_T21 + 24)
    parm _T148
    call _PrintInt
    _T149 = " "
    parm _T149
    call _PrintString
}

FUNCTION(_D.allprint) {
memo '_T22:4'
_D.allprint:
    _T150 = *(_T22 + 0)
    _T151 = *(_T150 + 0)
    *(_T22 + 0) = _T151
    parm _T22
    _T152 = *(_T22 + 0)
    _T153 = *(_T152 + 16)
    call _T153
    *(_T22 + 0) = _T150
    parm _T22
    _T154 = *(_T22 + 0)
    _T155 = *(_T154 + 12)
    call _T155
}

FUNCTION(_D.fun) {
memo '_T23:4'
_D.fun:
    _T156 = "D"
    parm _T156
    call _PrintString
    _T157 = *(_T23 + 0)
    _T158 = *(_T157 + 0)
    *(_T23 + 0) = _T158
    parm _T23
    _T159 = *(_T23 + 0)
    _T160 = *(_T159 + 16)
    call _T160
    *(_T23 + 0) = _T157
    parm _T23
    _T161 = *(_T23 + 0)
    _T162 = *(_T161 + 12)
    call _T162
    _T163 = "\n"
    parm _T163
    call _PrintString
}

FUNCTION(_E.setE) {
memo '_T24:4 _T25:8 _T26:12'
_E.setE:
    _T164 = *(_T24 + 20)
    *(_T24 + 20) = _T25
    _T165 = *(_T24 + 24)
    *(_T24 + 24) = _T26
}

FUNCTION(_E.print) {
memo '_T27:4'
_E.print:
    _T166 = " e="
    parm _T166
    call _PrintString
    _T167 = *(_T27 + 20)
    parm _T167
    call _PrintInt
    _T168 = " e1="
    parm _T168
    call _PrintString
    _T169 = *(_T27 + 24)
    parm _T169
    call _PrintInt
    _T170 = " "
    parm _T170
    call _PrintString
}

FUNCTION(_E.allprint) {
memo '_T28:4'
_E.allprint:
    _T171 = *(_T28 + 0)
    _T172 = *(_T171 + 0)
    *(_T28 + 0) = _T172
    parm _T28
    _T173 = *(_T28 + 0)
    _T174 = *(_T173 + 16)
    call _T174
    *(_T28 + 0) = _T171
    parm _T28
    _T175 = *(_T28 + 0)
    _T176 = *(_T175 + 12)
    call _T176
}

FUNCTION(_E.fun) {
memo '_T29:4'
_E.fun:
    _T177 = "E"
    parm _T177
    call _PrintString
    _T178 = *(_T29 + 0)
    _T179 = *(_T178 + 0)
    *(_T29 + 0) = _T179
    parm _T29
    _T180 = *(_T29 + 0)
    _T181 = *(_T180 + 16)
    call _T181
    *(_T29 + 0) = _T178
    parm _T29
    _T182 = *(_T29 + 0)
    _T183 = *(_T182 + 12)
    call _T183
    _T184 = "\n"
    parm _T184
    call _PrintString
}

FUNCTION(_F.setF) {
memo '_T30:4 _T31:8 _T32:12'
_F.setF:
    _T185 = *(_T30 + 28)
    *(_T30 + 28) = _T31
    _T186 = *(_T30 + 32)
    *(_T30 + 32) = _T32
}

FUNCTION(_F.print) {
memo '_T33:4'
_F.print:
    _T187 = " f="
    parm _T187
    call _PrintString
    _T188 = *(_T33 + 28)
    parm _T188
    call _PrintInt
    _T189 = " f1="
    parm _T189
    call _PrintString
    _T190 = *(_T33 + 32)
    parm _T190
    call _PrintInt
    _T191 = " "
    parm _T191
    call _PrintString
}

FUNCTION(_F.allprint) {
memo '_T34:4'
_F.allprint:
    _T192 = *(_T34 + 0)
    _T193 = *(_T192 + 0)
    *(_T34 + 0) = _T193
    parm _T34
    _T194 = *(_T34 + 0)
    _T195 = *(_T194 + 16)
    call _T195
    *(_T34 + 0) = _T192
    parm _T34
    _T196 = *(_T34 + 0)
    _T197 = *(_T196 + 12)
    call _T197
}

FUNCTION(_F.fun) {
memo '_T35:4'
_F.fun:
    _T198 = "F"
    parm _T198
    call _PrintString
    _T199 = *(_T35 + 0)
    _T200 = *(_T199 + 0)
    *(_T35 + 0) = _T200
    parm _T35
    _T201 = *(_T35 + 0)
    _T202 = *(_T201 + 16)
    call _T202
    *(_T35 + 0) = _T199
    parm _T35
    _T203 = *(_T35 + 0)
    _T204 = *(_T203 + 12)
    call _T204
    _T205 = "\n"
    parm _T205
    call _PrintString
}

FUNCTION(_G.setG) {
memo '_T36:4 _T37:8'
_G.setG:
    _T206 = *(_T36 + 20)
    *(_T36 + 20) = _T37
}

FUNCTION(_G.print) {
memo '_T38:4'
_G.print:
    _T207 = " g="
    parm _T207
    call _PrintString
    _T208 = *(_T38 + 20)
    parm _T208
    call _PrintInt
}

FUNCTION(_G.allprint) {
memo '_T39:4'
_G.allprint:
    _T209 = *(_T39 + 0)
    _T210 = *(_T209 + 0)
    *(_T39 + 0) = _T210
    parm _T39
    _T211 = *(_T39 + 0)
    _T212 = *(_T211 + 16)
    call _T212
    *(_T39 + 0) = _T209
    parm _T39
    _T213 = *(_T39 + 0)
    _T214 = *(_T213 + 12)
    call _T214
}

FUNCTION(_G.fun) {
memo '_T40:4'
_G.fun:
    _T215 = "G"
    parm _T215
    call _PrintString
    _T216 = *(_T40 + 0)
    _T217 = *(_T216 + 0)
    *(_T40 + 0) = _T217
    parm _T40
    _T218 = *(_T40 + 0)
    _T219 = *(_T218 + 16)
    call _T219
    *(_T40 + 0) = _T216
    parm _T40
    _T220 = *(_T40 + 0)
    _T221 = *(_T220 + 12)
    call _T221
    _T222 = "\n"
    parm _T222
    call _PrintString
}

FUNCTION(main) {
memo ''
main:
    _T230 =  call _A_New
    _T223 = _T230
    _T231 =  call _B_New
    _T224 = _T231
    _T232 =  call _C_New
    _T225 = _T232
    _T233 =  call _D_New
    _T226 = _T233
    _T234 =  call _E_New
    _T227 = _T234
    _T235 =  call _F_New
    _T228 = _T235
    _T236 =  call _G_New
    _T229 = _T236
    _T237 = 10
    _T238 = 11
    parm _T223
    parm _T237
    parm _T238
    _T239 = *(_T223 + 0)
    _T240 = *(_T239 + 8)
    call _T240
    _T241 = 20
    _T242 = 21
    parm _T224
    parm _T241
    parm _T242
    _T243 = *(_T224 + 0)
    _T244 = *(_T243 + 8)
    call _T244
    _T245 = 22
    _T246 = 23
    parm _T224
    parm _T245
    parm _T246
    _T247 = *(_T224 + 0)
    _T248 = *(_T247 + 24)
    call _T248
    _T249 = 30
    _T250 = 31
    parm _T225
    parm _T249
    parm _T250
    _T251 = *(_T225 + 0)
    _T252 = *(_T251 + 8)
    call _T252
    _T253 = 32
    _T254 = 33
    parm _T225
    parm _T253
    parm _T254
    _T255 = *(_T225 + 0)
    _T256 = *(_T255 + 24)
    call _T256
    _T257 = 40
    _T258 = 41
    parm _T226
    parm _T257
    parm _T258
    _T259 = *(_T226 + 0)
    _T260 = *(_T259 + 8)
    call _T260
    _T261 = 42
    _T262 = 43
    parm _T226
    parm _T261
    parm _T262
    _T263 = *(_T226 + 0)
    _T264 = *(_T263 + 24)
    call _T264
    _T265 = 44
    _T266 = 45
    parm _T226
    parm _T265
    parm _T266
    _T267 = *(_T226 + 0)
    _T268 = *(_T267 + 28)
    call _T268
    _T269 = 50
    _T270 = 51
    parm _T227
    parm _T269
    parm _T270
    _T271 = *(_T227 + 0)
    _T272 = *(_T271 + 8)
    call _T272
    _T273 = 52
    _T274 = 53
    parm _T227
    parm _T273
    parm _T274
    _T275 = *(_T227 + 0)
    _T276 = *(_T275 + 24)
    call _T276
    _T277 = 54
    _T278 = 55
    parm _T227
    parm _T277
    parm _T278
    _T279 = *(_T227 + 0)
    _T280 = *(_T279 + 28)
    call _T280
    _T281 = 60
    _T282 = 61
    parm _T228
    parm _T281
    parm _T282
    _T283 = *(_T228 + 0)
    _T284 = *(_T283 + 8)
    call _T284
    _T285 = 62
    _T286 = 63
    parm _T228
    parm _T285
    parm _T286
    _T287 = *(_T228 + 0)
    _T288 = *(_T287 + 24)
    call _T288
    _T289 = 64
    _T290 = 65
    parm _T228
    parm _T289
    parm _T290
    _T291 = *(_T228 + 0)
    _T292 = *(_T291 + 28)
    call _T292
    _T293 = 66
    _T294 = 67
    parm _T228
    parm _T293
    parm _T294
    _T295 = *(_T228 + 0)
    _T296 = *(_T295 + 32)
    call _T296
    _T297 = 70
    _T298 = 71
    parm _T229
    parm _T297
    parm _T298
    _T299 = *(_T229 + 0)
    _T300 = *(_T299 + 8)
    call _T300
    _T301 = 72
    _T302 = 73
    parm _T229
    parm _T301
    parm _T302
    _T303 = *(_T229 + 0)
    _T304 = *(_T303 + 24)
    call _T304
    _T305 = 74
    parm _T229
    parm _T305
    _T306 = *(_T229 + 0)
    _T307 = *(_T306 + 28)
    call _T307
    parm _T223
    _T308 = *(_T223 + 0)
    _T309 = *(_T308 + 20)
    call _T309
    parm _T224
    _T310 = *(_T224 + 0)
    _T311 = *(_T310 + 20)
    call _T311
    parm _T225
    _T312 = *(_T225 + 0)
    _T313 = *(_T312 + 20)
    call _T313
    parm _T226
    _T314 = *(_T226 + 0)
    _T315 = *(_T314 + 20)
    call _T315
    parm _T227
    _T316 = *(_T227 + 0)
    _T317 = *(_T316 + 20)
    call _T317
    parm _T228
    _T318 = *(_T228 + 0)
    _T319 = *(_T318 + 20)
    call _T319
    parm _T229
    _T320 = *(_T229 + 0)
    _T321 = *(_T320 + 20)
    call _T321
}

