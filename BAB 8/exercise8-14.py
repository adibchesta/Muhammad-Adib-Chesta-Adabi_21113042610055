def make_car(pabrikan, model, **informasi):
    mobil = {
        "pabrikan": pabrikan,
        "model": model
    }

    mobil.update(informasi)

    return mobil


mobil = make_car(
    "Toyota",
    "Avanza",
    warna="Hitam",
    transmisi="Manual",
    tahun=2025
)

print(mobil)