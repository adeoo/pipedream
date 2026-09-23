# Adel's learning map: SolidWorks, ISO drawing norms and design for the shop

This file is the menu of things to learn. It is **not** part of the skill. When you want a lesson, say for example: *"Make the lesson 3.4 Exploded views"* or *"I want to learn hole callouts"*. The `solidworks-lesson` skill reads this file, finds the chapter, and builds one real project around it.

How to read each lesson entry:
- **Learn:** the topics the lesson must cover.
- **Project idea:** the one real project the lesson is built around.
- **Real source:** where the real data or drawing comes from (you only need a computer).
- **Norms:** the standards to use. Always check the current edition before teaching a number.
- **Leave out:** what belongs to another lesson.
- **Status:** planned or done.

---

## Suggested order

1. 2.1 to 2.4 Fits and tolerances **(done, Session 2)**
2. 3.1 to 3.3 Your first drawing the shop can read (was planned as Session 3)
3. 4.1 to 4.3 First GD&T: flatness, datums, position
4. 5.1 to 5.3 Threads (was planned as Session 4)
5. 7.1 to 7.4 Sheet metal (was planned as Session 5)
6. 3.4 to 3.7 Assembly drawings, BOM, balloons, exploded views
7. 6.x Design for machining
8. 1.x SolidWorks power tools, when you need them
9. 8.x Machine elements, 9.x Welded frames, 10.x Model based definition

Change the order when your work needs something first.

---

## Chapter 1. SolidWorks modeling habits that save time

### 1.1 Design intent: sketches that do not break
- **Learn:** fully defined sketches, relations before dimensions, dimensioning from the functional faces, origin and planes, feature order, naming features.
- **Project idea:** a fixture base plate from a real Misumi or norelem plate drawing, modeled so that changing the length does not break the holes.
- **Real source:** misumi-ec.com or norelem.com, a standard fixture base plate with a CAD drawing.
- **Leave out:** tolerances (Chapter 2), drawings (Chapter 3).
- **Status:** planned.

### 1.2 Configurations and design tables
- **Learn:** configurations, design tables in Excel, configuration-specific dimensions, suppressing features, custom properties per configuration.
- **Project idea:** a family of shaft collars or spacers (5 sizes) from one model, with a design table.
- **Real source:** a shaft collar catalog page (Misumi, Ruland) with its size table.
- **Leave out:** drawings of each configuration (show only one).
- **Status:** planned.

### 1.3 Custom properties, file names and the title block link
- **Learn:** custom properties (part number, material, description, drawn by), property tab builder, how the title block reads them, a simple file naming rule.
- **Project idea:** set up the properties for the fixture plate of 1.1 so the drawing title block fills itself.
- **Real source:** your own template, plus ISO 7200 fields.
- **Norms:** ISO 7200 (title block data fields).
- **Status:** planned.

### 1.4 Toolbox and the Design Library
- **Learn:** Toolbox (ISO bolts, nuts, washers, pins, bearings), Smart Fasteners, Hole Wizard link, adding your own parts to the Design Library.
- **Project idea:** fasten a real bearing unit to a frame plate with correct ISO 4762 screws and washers.
- **Real source:** a UCP pillow block datasheet (bolt size and spacing).
- **Norms:** ISO 4762 (socket head cap screws), ISO 7089 (washers), ISO 273 (clearance holes).
- **Status:** planned.

### 1.5 Top-down and in-context design
- **Learn:** designing a part inside an assembly, external references, when to use them and when to break them, layout sketches.
- **Project idea:** a small guard around a belt drive, sized from the assembly.
- **Leave out:** sheet metal rules (Chapter 7).
- **Status:** planned.

### 1.6 Sending files to the shop
- **Learn:** Pack and Go, PDF of drawings, STEP for 3D, DXF for laser cutting, eDrawings, what each shop wants.
- **Project idea:** prepare a complete "shop package" for one part: PDF + STEP + DXF.
- **Status:** planned.

---

## Chapter 2. Tolerances and fits

### 2.1 Reading ISO fit codes (H7, g6...)
### 2.2 The three families of fits
### 2.3 The SolidWorks Fit tool and Hole Wizard tolerances
### 2.4 Bearings, dowel pins, bushings and the ISO 2768-m note
- **Status:** **done** in Session 2, version 2. Facts are in the skill's checked-facts file.
- **Possible follow-up:** 2.5 Tolerance stack-up by hand (a simple 1D chain: why 5 parts at ±0.1 do not give ±0.1). Project: the height of a stack of plates and a bearing block. Norms: none beyond ISO 286 / ISO 2768.

---

## Chapter 3. Drawings the shop can read

### 3.1 The drawing sheet: template, sheet format, title block
- **Learn:** drawing template vs sheet format, sheet sizes, the title block fields, scale, projection symbol (first angle, used in Brazil), the general notes block (ISO 2768-m, edge breaks).
- **Project idea:** make your own A4 and A3 drawing template with a correct title block, and use it for the fixture plate.
- **Real source:** your company's current title block, and ISO 7200 fields.
- **Norms:** ISO 5457 (sheet sizes and layout), ISO 7200 (title block), ISO 5455 (scales), ISO 5456-2 (projection methods), ISO 3098 (lettering). Brazil: ABNT NBR 10068 (sheet layout), NBR 8196 (scales), NBR 10067 (views).
- **Status:** planned.

### 3.2 Views: which ones, and how many
- **Learn:** first angle projection, choosing the front view, how many views are enough, auxiliary views, section views, detail views, broken views, half sections, hidden lines (when to show them).
- **Project idea:** the full drawing of a real bearing block (housing) from a maker drawing.
- **Real source:** a plummer block or bearing housing drawing from SKF, Schaeffler or a Brazilian maker catalog.
- **Norms:** ISO 128 series (lines, views, sections; restructured 2020 to 2022, older shops still cite ISO 128-20, -30, -40, -50), ISO 5456-2. Brazil: NBR 10067, NBR 8403 (lines), NBR 12298 (hatching).
- **Status:** planned.

### 3.3 Dimensioning for the machinist
- **Learn:** dimensioning from a datum face, chain vs baseline vs ordinate dimensions, no double dimensions, reference dimensions, where tolerances go, hole callouts from Hole Wizard, chamfer dimensions, what "missing dimension" means for the shop.
- **Project idea:** dimension the bearing block from 3.2 so a machinist could make it without calling you.
- **Real source:** the same maker drawing; compare your version with theirs.
- **Norms:** ISO 129-1 (dimensioning), ISO 2768-1 (general tolerances), ISO 13715 (edges, edge break symbol). Brazil: NBR 10126.
- **Leave out:** GD&T frames (Chapter 4).
- **Status:** planned.

### 3.4 Assembly drawings, BOM and balloons
- **Learn:** the assembly drawing, the Bill of Materials (BOM, *lista de materiais*) table, balloons (item numbers), part numbers from custom properties, stacked balloons.
- **Project idea:** the assembly drawing of a conveyor idler roller (tube, 2 bearings, axle, circlips).
- **Real source:** a conveyor roller catalog (for example Interroll or a Brazilian roller maker) with dimensions.
- **Norms:** ISO 7573 (parts lists), ISO 6433 (item references / balloons).
- **Status:** planned.

### 3.5 Exploded views
- **Learn:** Exploded View tool in assemblies, explode steps, radial explode, explode lines (*linhas de explosão*), showing the exploded view on a drawing with BOM and balloons, animating it.
- **Project idea:** an exploded view of a real pillow block unit or a small linear axis carriage, used as an assembly instruction sheet.
- **Real source:** a maker's free CAD model (SKF, igus, Misumi) and its datasheet.
- **Status:** planned.

### 3.6 Revision control on drawings
- **Learn:** revision table, revision symbols, what to change and how to tell the shop, drawing states (draft, released).
- **Project idea:** change a hole size on the bearing block drawing and release revision B properly.
- **Status:** planned.

### 3.7 Reading a real drawing from someone else
- **Learn:** how to read an unknown drawing: title block first, projection symbol, views, datums, notes, tolerances, surface marks.
- **Project idea:** read a real public drawing and rebuild the part in SolidWorks from it.
- **Real source:** a public domain drawing (NASA technical reports, old patents on Google Patents) or a maker PDF drawing.
- **Status:** planned.

---

## Chapter 4. GD&T: geometric tolerances the shop understands

### 4.1 Why size tolerances are not enough; flatness and the feature control frame
- **Learn:** the feature control frame, form tolerances (flatness, straightness, roundness, cylindricity), when a plate needs flatness.
- **Project idea:** the mounting face of a linear guide base plate.
- **Real source:** a linear guide maker's mounting requirements (THK, Hiwin, Bosch Rexroth: flatness and parallelism of the mounting surface).
- **Norms:** ISO 1101 (geometrical tolerancing), ISO 8015 (fundamental rules, independence principle), ISO 22081 (general geometrical specifications).
- **Status:** planned.

### 4.2 Datums (*referências*)
- **Learn:** datum features, datum letters, primary, secondary, tertiary datum, how the part sits in the machine or fixture.
- **Project idea:** add datums to the linear guide base plate.
- **Norms:** ISO 5459 (datums and datum systems).
- **Status:** planned.

### 4.3 Position, perpendicularity, parallelism, runout
- **Learn:** position of holes (vs ± coordinates), perpendicularity, parallelism, circular and total runout for shafts and bearing seats, maximum material condition (Ⓜ) basics.
- **Project idea:** the bolt and dowel hole pattern of the base plate, and the runout of a conveyor shaft.
- **Norms:** ISO 1101, ISO 5458 (pattern and combined tolerances), ISO 2692 (maximum material requirement).
- **Leave out:** tolerance analysis software.
- **Status:** planned.

### 4.4 Surface texture (roughness)
- **Learn:** Ra and Rz, the surface texture symbol, what each process can give, what it costs, typical values for seats, sliding faces and plain faces.
- **Project idea:** add surface marks to the bearing block drawing.
- **Norms:** ISO 21920-1 (indication of surface texture, replaced ISO 1302). Brazil: NBR 8404 (older, still seen).
- **Status:** planned.

---

## Chapter 5. Threads

### 5.1 Cosmetic threads vs modeled threads
- **Learn:** why modeled helix threads are slow and not needed, cosmetic threads, Hole Wizard tapped holes, how threads show on drawings.
- **Project idea:** re-model a real threaded part (a leveling foot or a clamp) with cosmetic threads and draw it.
- **Real source:** a leveling foot or toggle clamp datasheet (norelem, Kipp, Misumi).
- **Norms:** ISO 6410-1 (representation of threads).
- **Status:** planned (was Session 4).

### 5.2 Pitch, coarse and fine, thread classes 6H and 6g
- **Learn:** metric thread designation (M8, M8x1), coarse vs fine pitch, thread tolerance classes 6H (nut) and 6g (bolt), tap drill size.
- **Norms:** ISO 261 (general plan), ISO 965-1 (tolerances), ISO 68-1 (basic profile).
- **Status:** planned.

### 5.3 Thread depth, engagement and callouts
- **Learn:** tapped hole depth vs drill depth, minimum engagement in steel and aluminium, thread callouts the shop reads without asking, helical inserts.
- **Project idea:** the tapped holes of the bearing block or the base plate.
- **Status:** planned.

---

## Chapter 6. Design for machining (*projeto para usinagem*)

### 6.1 Materials and stock sizes
- **Learn:** common materials in Brazilian shops (SAE 1020, SAE 1045, SAE 4140, aluminium 6351 and 6061, stainless 304), stock bar and plate sizes, why the part should fit the stock.
- **Project idea:** choose material and stock for the bearing block and the shaft.
- **Real source:** a Brazilian steel and aluminium distributor size table.
- **Status:** planned.

### 6.2 Milling-friendly parts
- **Learn:** internal corner radii (the tool is round), pocket depth vs tool length, hole depth vs diameter, setups and why fewer is cheaper, deburring.
- **Project idea:** redesign a real fixture block so it needs one less setup.
- **Status:** planned.

### 6.3 Turning-friendly parts
- **Learn:** shafts: shoulders, undercuts, centre holes, keyways, retaining ring grooves, chamfers, what a lathe does easily.
- **Project idea:** a conveyor drive shaft drawing, ready for the lathe.
- **Norms:** DIN 509 (undercuts, common in Brazil), DIN 471 / DIN 472 (retaining rings), ISO/DIN keyway standards (DIN 6885 is common in Brazil).
- **Status:** planned.

### 6.4 Heat treatment and surface finishing
- **Learn:** hardening, case hardening, what to write on the drawing (hardness HRC), black oxide (*oxidação negra*), zinc plating, anodizing.
- **Status:** planned.

### 6.5 What makes a part expensive
- **Learn:** the cost drivers: tight tolerances, fine surfaces, special tools, many setups, hard materials, small quantities. How to ask the shop.
- **Project idea:** make a "cheap" and an "expensive" version of the same part and compare.
- **Status:** planned.

---

## Chapter 7. Sheet metal (*chapa*)

### 7.1 Base flange, edge flange, bend radius
- **Learn:** SolidWorks sheet metal features, material thickness, inside bend radius, minimum flange length.
- **Project idea:** a real sheet metal bracket or electrical box cover from a catalog.
- **Real source:** a sheet metal enclosure or bracket catalog with drawings.
- **Status:** planned (was Session 5).

### 7.2 K-factor and flat patterns that come out right
- **Learn:** K-factor, bend allowance and bend deduction, why the default K-factor gives the wrong flat size, getting the right value from your shop, gauge tables.
- **Project idea:** the flat pattern of the 7.1 part, checked against a bend table.
- **Norms:** DIN 6935 (cold bending of flat steel, often used), ISO 2768 for sheet sizes.
- **Status:** planned.

### 7.3 Reliefs, holes near bends, hardware
- **Learn:** bend relief, corner relief, minimum hole-to-bend distance, press-in hardware (PEM style nuts and studs).
- **Status:** planned.

### 7.4 Sheet metal drawings and DXF for laser
- **Learn:** flat pattern view, bend lines and bend notes, exporting DXF for laser cutting.
- **Status:** planned.

---

## Chapter 8. Machine elements for your machines

### 8.1 Shafts, keys and retaining rings
- **Learn:** shaft diameters, key and keyway sizes, circlips, where each goes.
- **Norms:** DIN 6885 / ISO 2491 keys, DIN 471 / DIN 472 rings.
- **Status:** planned.

### 8.2 Belt and pulley drives
- **Learn:** timing belts, pulley bores, center distance, tensioning.
- **Real source:** a timing belt pulley catalog (Gates, Misumi).
- **Status:** planned.

### 8.3 Linear guides and ball screws
- **Learn:** profile rail guides, mounting surfaces, preload, ball screw end supports.
- **Real source:** THK, Hiwin or Bosch Rexroth catalogs.
- **Status:** planned.

### 8.4 Couplings and motor mounts
- **Learn:** rigid vs flexible couplings, alignment, motor flange mounts.
- **Status:** planned.

### 8.5 Bolted joints
- **Learn:** screw size choice, clearance holes, counterbores, thread engagement, washers, tightening torque basics.
- **Norms:** ISO 4762, ISO 273, ISO 898-1 (property classes 8.8, 10.9, 12.9).
- **Status:** planned.

---

## Chapter 9. Welded frames (*estruturas soldadas*)

### 9.1 Weldments in SolidWorks
- **Learn:** structural members, profiles (tube, angle, U), trim and extend, cut list.
- **Project idea:** a real conveyor frame from standard square tube.
- **Status:** planned.

### 9.2 Welding symbols on drawings
- **Learn:** weld symbols, fillet weld size, where to weld and where not, machining after welding.
- **Norms:** ISO 2553 (welding symbols). Brazil: AWS style is also seen; know both.
- **Status:** planned.

---

## Chapter 10. 3D annotations and Model Based Definition (MBD)

### 10.1 3D annotations instead of a drawing
- **Learn:** MBD Dimensions (DimXpert), 3D PMI, 3D PDF, when a shop can work from a 3D model.
- **Norms:** ISO 16792 (digital product definition data practices).
- **Status:** planned.

---

## Words and norms reference

- **ISO 10209:** vocabulary of technical product documentation. Useful when a word is not clear.
- **ABNT (Brazil) equivalents often seen in shops:** NBR 10067 (views), NBR 8403 (lines), NBR 10126 (dimensioning), NBR 10068 (sheet layout), NBR 8196 (scales), NBR 12298 (hatching), NBR 8404 (surface texture), NBR 6158 (fits, old ISO 286 equivalent), ABNT NBR ISO 2768-1.
- **Rule for every lesson:** check the current edition of each ISO standard before teaching a number from it. Editions change (for example ISO 1302 became ISO 21920-1, and ISO 2768-2 became ISO 22081).
