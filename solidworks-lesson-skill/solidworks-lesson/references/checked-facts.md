# Facts already checked (reuse them, do not research them again)

Checked against ISO 286, ISO 2768, ISO 492, SKF and help.solidworks.com, then reviewed twice (Session 2). Add new checked facts at the end of this file after each lesson's review.

## ISO 286 fits
- Ø10 H7 = 10.000 to 10.015. Ø20 H7 = 20.000 to 20.021. Ø35 H7 = 35.000 to 35.025. Ø8 H7 = 8.000 to 8.015. Ø32 H7 = 32.000 to 32.025. Ø12 H7 = +0.018 / 0.
- At Ø10: g6 9.986 to 9.995 (−0.005/−0.014). h6 9.991 to 10.000. k6 10.001 to 10.010. p6 10.015 to 10.024. js5 ±0.003.
- At Ø20: f7 19.959 to 19.980. g6 19.980 to 19.993. k6 20.002 to 20.015. At Ø8: m6 8.006 to 8.015.
- At Ø10: H7/g6 5 to 29 µm clearance. H7/h6 0 to 24 clearance. H7/k6 14 clearance to 10 interference. H7/p6 0 to 24 interference.
- IT widths (µm), IT6/IT7/IT8/IT9/IT11: 6 to 10 mm 9/15/22/36/90. 10 to 18: 11/18/27/43/110. 18 to 30: 13/21/33/52/130. 30 to 50: 16/25/39/62/160.
- Preferred hole-basis fits: H11/c11 loose running, H9/d9 free running, H8/f7 close running, H7/g6 sliding, H7/h6 locational clearance, H7/k6 locational transition, H7/n6 tighter transition, H7/p6 light interference, H7/s6 medium drive, H7/u6 force.
- Process capability: twist drill alone IT11 to IT13. Reaming IT6 to IT10. Grinding IT5 to IT7.

## Bearings
- 6205: 25 x 52 x 15 mm. Bore 24.990 to 25.000 (ISO 492 normal). Seat Ø25 k5 = 25.002 to 25.011, so 2 to 21 µm interference. Housing Ø52 H7 = 52.000 to 52.030. da min 30, Da max 47, corner radius 1.0 max. Bore code 04 and up x 5 = bore in mm.
- SKF short form: rotating inner ring, normal load: js5 up to 10 mm, j5 10 to 17, k5 17 to 100, m5/m6 heavy or shock. Stationary outer ring: H7, H6 high accuracy, G7 if hot. Rotating outer ring: K7, M7/N7 heavy shock. The ring that turns against the load needs the tight fit.
- Pillow block (UCP) inserts: shaft tolerance from the maker; they lock with set screw or collar.

## Pins, bushings, shafts
- Dowel pins: ISO 8734 hardened and ground m6; ISO 2338 plain m6; ISO 8735 internal thread (blind holes, extraction). Hole H7 reamed (transition with m6). Drill 0.2 to 0.5 under, then ream. Engagement 1 to 1.5 d. One round hole + one slot on the line between the pins, or a diamond pin with flats facing the first pin. Pins far apart.
- Bronze bushing: housing H7, shaft f7 (e7 fast or hot). The bore closes when pressed: use the maker's after-press size or ream after pressing.
- H7/g6 slides and locates. H8/f7 runs. Linear ball bushing: shaft g6, housing H7. LM20UU = 20 bore, 32 OD.
- Come apart: H7/h6 by hand, H7/k6 light tap. Never p6, s6, u6 on parts opened often.

## ISO 2768 and notes
- ISO 2768-1 class m: ±0.1 (0.5 to 6), ±0.2 (6 to 30), ±0.3 (30 to 120), ±0.5 (120 to 400), ±0.8 (400 to 1000). Class f and c in Session 2 table. Broken edges class m: ±0.2 up to 3, ±0.5 3 to 6, ±1.0 above 6.
- Brazil: ABNT NBR ISO 2768-1. ISO 22081:2021 replaced ISO 2768-2. Shops still write "ISO 2768-mK".
- Notes: `UNLESS OTHERWISE STATED: GENERAL TOLERANCES ISO 2768-m`, `BREAK ALL SHARP EDGES 0.3 MAX (QUEBRAR CANTOS VIVOS)`.

## SolidWorks (help.solidworks.com)
- Dimension > PropertyManager > Tolerance/Precision > Tolerance Type: Fit / Fit with tolerance / Fit (tolerance only). Classification: User Defined, Clearance, Transitional, Press (filters Hole Fit and Shaft Fit). Show parenthesis. Fit Tolerance Display: stacked with line, stacked without line, linear. SolidWorks computes the bilateral tolerances (deviations) from ISO 286; it shows the code plus deviations, not limit sizes. A 0 means out of the standard's range. Works in parts and drawings.
- Hole Wizard > Type tab > Tolerance/Precision panel (since 2019). Insert > Annotations > Hole Callout. Favorites box at the top of Hole Wizard.
- Dowel holes (since 2013): Hole Wizard > Type tab > Hole Type: Hole > Type: the dowel option.
- DimXpert (MBD Dimensions since 2019) applies a fit, cannot choose it. TolAnalyst: Premium only. Toolbox: not in Standard, included in Education Edition, Design Library tab.
- Insert > Annotations > Note for drawing notes.
- Education Edition watermark on drawings; license for learning only. (Adel's brief says a commercial seat can refuse to open its files; a reviewer doubted this. Not re-verified.)

## Free tools
SolidWorks Fit tolerance type; amesweb.info ISO fits calculator; xometry.pro ISO 286 calculator; Android app "ISO Fits" (tss.in); stefanelli.eng.br (NBR 6158 tables). Models: 3D ContentCentral, TraceParts, SKF, Schaeffler, NSK, igus, Misumi. MITCalc is paid, not needed.
