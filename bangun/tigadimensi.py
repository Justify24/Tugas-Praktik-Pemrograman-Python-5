import math

# Fungsi untuk menghitung luas permukaan kubus
def luas_kubus(sisi):
    return 6 * sisi**2

# Fungsi untuk menghitung luas permukaan balok
def luas_balok(panjang, lebar, tinggi):
    return 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

# Fungsi untuk menghitung luas permukaan tabung
def luas_tabung(jari_jari, tinggi):
    return 2 * math.pi * jari_jari * (jari_jari + tinggi)

# Fungsi untuk menghitung luas permukaan kerucut
def luas_kerucut(jari_jari, sisi_miring):
    return math.pi * jari_jari * (jari_jari + sisi_miring)

# Fungsi untuk menghitung luas permukaan limas
def luas_limas(luas_alas, luas_seluruh_sisi_tegak, tinggi):
    return luas_alas + (luas_seluruh_sisi_tegak * tinggi)

# Fungsi untuk menghitung luas permukaan prisma
def luas_prisma(luas_alas, keliling_alas, tinggi):
    return (2 * luas_alas) + (keliling_alas * tinggi)

