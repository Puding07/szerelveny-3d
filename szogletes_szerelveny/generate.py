"""Szögletes szerelvény: 67x67 mm négyzetes külső, 50 mm mély,
kerek vak furat csak a hátoldalon (z=0), az elülső oldal zárt.
Futtatás: python3 generate.py  (trimesh + manifold3d kell)"""
import trimesh

MERET = 67.0       # külső oldalhossz (mm), megegyezik a 67 mm "átmérővel"
MELYSEG = 50.0     # teljes mélység (mm)
FURAT_D = 61.0     # furat átmérő (mm) -> 3 mm falvastagság
FURAT_MELY = 46.0  # furat mélysége a hátoldaltól (mm) -> 4 mm zárt elülső fal

test = trimesh.creation.box(extents=[MERET, MERET, MELYSEG])
test.apply_translation([0, 0, MELYSEG / 2])
furat = trimesh.creation.cylinder(radius=FURAT_D / 2, height=FURAT_MELY + 1, sections=180)
furat.apply_translation([0, 0, (FURAT_MELY - 1) / 2])  # túlnyúlik a hátsó síkon
kesz = test.difference(furat, engine="manifold")
assert kesz.is_watertight
kesz.export("szogletes_szerelveny_67x50.stl")
print(kesz.bounds, round(kesz.volume / 1000, 2), "cm3")
