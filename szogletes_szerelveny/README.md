# Szögletes egyes szerelvénydoboz – 50 mm mély

3D nyomtatható, süllyesztett (falba építhető) **egyes** szerelvénydoboz **négyzetes külsővel**.
A főágon lévő kettes/hármas dobozok kialakítását követi (csavartornyok, perem, kitörhető nyílás), de a kerek oldalfal helyett négyzetes a külseje, és kitörhető nyílás **csak a hátlapon** van.

## Fájlok

| Fájl | Leírás |
|---|---|
| `szerelvenydoboz_egyes_50_szogletes.FCMacro` | FreeCAD makró: legyártja a paraméteres `.FCStd` modellt (Parameterek táblázattal), valamint az `.stl` és `.step` fájlt |
| `szerelvenydoboz_egyes_50_szogletes.stl` | Nyomtatható háló |

## Főbb méretek

- Befoglaló méret: 74 × 74 × 50 mm (perem), a test 67 × 67 mm
- Mélység a perem tetejétől a hátlapig: **50 mm**
- Belső (kerek) üreg: Ø62 mm, hátlap: 2 mm, a falvastagság az oldalak közepén 2,5 mm
- Perem: 74 × 74 mm, 1,5 mm vastag
- Csavartávolság: 60 mm, Ø7 mm-es csavartornyok, 2,8 mm-es furat (M3/M3,5 önmetszőhöz), 15 mm mély
- Hátlapi kitörhető nyílás: Ø20 mm, 0,6 mm-es rés, 8 db 0,8 mm-es tartóhíd
- Oldalfalon nincs nyílás
- Anyagtérfogat: ~83,2 cm³

## Paraméterek

A `Parameterek` táblázat celláinak átírásával módosítható (pl. `Melyseg`, `Kulso_a`, `Belso_d`, `Perem_a`, `Csavar_tav`, `Hatso_d`), minden elem követi a változást.

## Nyomtatás

- Hátlappal lefelé nyomtatható, a perem felfelé néz. A perem 3,5 mm-rel nyúlik túl az oldalfalon.
- A kitörő rése 0,6 mm; ügyelj rá, hogy a szeletelő ne töltse ki.
- A modell FreeCAD 1.1-gyel készült.
