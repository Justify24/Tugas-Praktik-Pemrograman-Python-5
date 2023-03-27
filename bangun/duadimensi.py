import math

# Fungsi untuk menghitung luas persegi
def luas_persegi(sisi):
    hasil = sisi ** 2
    return hasil

# Fungsi untuk menghitung luas persegi panjang
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

# Fungsi untuk menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

# Fungsi untuk menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    return math.pi * (jari_jari ** 2)

# Fungsi untuk menghitung luas jajar genjang
def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

# Fungsi untuk menghitung luas trapesium
def luas_trapesium(sisi_sejajar_1, sisi_sejajar_2, tinggi):
    return 0.5 * (sisi_sejajar_1 + sisi_sejajar_2) * tinggi