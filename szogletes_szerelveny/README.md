# Szögletes egyes szerelvénydoboz – 50 mm mély

3D nyomtatható, süllyesztett (falba építhető) **egyes** szerelvénydoboz **négyzetes külsővel**.
A főágon lévő kettes/hármas dobozok kialakítását követi (csavartornyok, kitörhető nyílás), de a kerek oldalfal helyett négyzetes, végig 85 × 85 mm-es a külseje (nincs kiálló perem), és kitörhető nyílás **csak a hátlapon** van.

## Fájlok

| Fájl | Leírás |
|---|---|
| `szerelvenydoboz_egyes_50_szogletes.FCMacro` | FreeCAD makró: legyártja a paraméteres `.FCStd` modellt (Parameterek táblázattal), valamint az `.stl` és `.step` fájlt |
| `szerelvenydoboz_egyes_50_szogletes.stl` | Nyomtatható háló |

## Főbb méretek

- Befoglaló méret: **85 × 85 × 50 mm**, a külső végig egyenes
- Mélység az elülső síktól a hátlapig: **50 mm**
- Belső (kerek) üreg: Ø62 mm, hátlap: 2 mm, a falvastagság az oldalak közepén 11,5 mm
- Csavartávolság: 60 mm, Ø7 mm-es csavartornyok, 2,8 mm-es furat (M3/M3,5 önmetszőhöz), 15 mm mély
- Hátlapi kitörhető nyílás: Ø20 mm, 0,6 mm-es rés, 8 db 0,8 mm-es tartóhíd
- Oldalfalon nincs nyílás
- Anyagtérfogat: ~218,6 cm³

## Paraméterek

A `Parameterek` táblázat celláinak átírásával módosítható (pl. `Melyseg`, `Kulso_a`, `Belso_d`, `Csavar_tav`, `Hatso_d`). A `Perem_a` alapból `=Kulso_a`; ha nagyobbra állítod, kiálló perem lesz a doboz elején. Minden elem követi a változást.

## Nyomtatás

- Hátlappal lefelé nyomtatható, a nyitott oldal felfelé néz; túlnyúlás nincs, támasz nem kell.
- A kitörő rése 0,6 mm; ügyelj rá, hogy a szeletelő ne töltse ki.
- A modell FreeCAD 1.1-gyel készült.
