#NAMA   = Muhammad Farhan
#NIM    = V3922033
#Kelas  = TIE 22

import bangun.tigadimensi
import bangun.duadimensi

def main_menu():
    print("Selamat datang!")
    print("Silakan pilih bangun ruang yang akan di cari luasnya:")
    print("1. Bangun 3D")
    print("2. Bangun 2D")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan Anda (1 atau 2): ")
    
    if pilihan == "1":
        menu_option_3d()
    elif pilihan == "2":
        menu_option_2d()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program kami.")
        exit()

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        main_menu()

def menu_option_3d():
    print("Mencari Luas Bangun 3D.")
    print("")
    print("Silakan pilih bangun 3D yang akan dicari luasnya:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Limas")
    print("6. Prisma")
    print("7. Kembali(Main Menu)")
    print("8. Keluar")
    sub_pilihan = input("Masukkan pilihan Anda (1 - 8): ")
    
    if sub_pilihan == "1":
        print("Menghitung Hasil Luas Kubus")
        print("-------------------------------------------------------")
        sisi = int(input("Masukkan panjang sisi (cm): "))
        hasil_luas = bangun.tigadimensi.luas_kubus(sisi)
        print("hasil dari Luas Kubus tersebut adalah = {}".format(hasil_luas))
        menu_option_3d()

    elif sub_pilihan == "2":
        print("Menghitung Hasil Luas Balok")
        print("-------------------------------------------------------")
        panjang = int(input("Masukkan panjang sisi (cm): "))
        lebar = int(input("Masukkan lebar sisi (cm): "))
        tinggi = int(input("Masukkan tinggi sisi (cm): "))
        hasil_luas = bangun.tigadimensi.luas_balok(panjang, lebar, tinggi)
        print("hasil dari Luas Balok tersebut adalah = {}".format(hasil_luas))
        menu_option_3d()

    elif sub_pilihan == "3":
        print("Menghitung Hasil Luas Tabung")
        print("-------------------------------------------------------")
        jari_jari = int(input("Masukkan jari-jari (cm): "))
        tinggi = int(input("Masukkan tinggi (cm): "))
        hasil_luas = bangun.tigadimensi.luas_tabung(jari_jari, tinggi)
        print("Hasil dari luas Tabung tersebut adalah = {}".format(hasil_luas))
        menu_option_3d()

    elif sub_pilihan == "4":
        print("Menghitung Hasil Luas Kubus")
        print("-------------------------------------------------------")
        jari_jari = int(input("Masukkan panjang jari-jari (cm): "))
        sisi_miring = int(input("Masukkan panjang sisi miring (cm): "))
        hasil_luas = bangun.tigadimensi.luas_kerucut(jari_jari, sisi_miring)
        print("hasil dari Luas Kerucut tersebut adalah = {}".format(hasil_luas))
        menu_option_3d()

    elif sub_pilihan == "5":
        print("Menghitung Hasil Luas Kubus")
        print("-------------------------------------------------------")
        luas_alas = int(input("Masukkan luas alas (cm): "))
        luas_seluruh_sisi_tegak = int(input("Masukkan luas seluruh sisi tegak (cm): "))
        tinggi = int(input("Masukkan tinggi (cm): "))
        hasil_luas = bangun.tigadimensi.luas_limas(luas_alas, luas_seluruh_sisi_tegak, tinggi)
        print("hasil dari Luas Limas tersebut adalah = {}".format(hasil_luas))
        menu_option_3d()

    elif sub_pilihan == "6":
        print("Menghitung Hasil Luas Kubus")
        print("-------------------------------------------------------")
        luas_alas = int(input("Masukkan luas alas (cm): "))
        keliling_alas = int(input("Masukkan keliling alas (cm): "))
        tinggi = int(input("Masukkan tinggi (cm): "))
        hasil_luas = bangun.tigadimensi.luas_prisma(luas_alas, keliling_alas, tinggi)
        print("hasil dari Luas Prisma tersebut adalah = {}".format(hasil_luas))
        menu_option_3d()

    elif sub_pilihan == "7":
        main_menu()

    elif sub_pilihan == "8":
        print("Terima kasih telah menggunakan program kami.")
        exit() 

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        menu_option_3d()

def menu_option_2d():
    print("Mencari Luas Bangun 2D.")
    print("")
    print("Silakan pilih bangun 2D yang akan dicari luasnya:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Limas")
    print("6. Trapesium")
    print("7. Kembali(Main Menu)")
    print("8. Keluar")
    sub_pilihan = input("Masukkan pilihan Anda (1 - 8): ")
    
    if sub_pilihan == "1":
        print("Menghitung Hasil Luas Kubus")
        print("-------------------------------------------------------")
        sisi = int(input("Masukkan panjang sisi (cm): "))
        hasil_luas = bangun.duadimensi.luas_persegi(sisi)
        print("hasil dari Luas Kubus tersebut adalah = {}".format(hasil_luas))
        menu_option_2d()

    elif sub_pilihan == "2":
        print("Menghitung Hasil Luas Persegi Panjang")
        print("-------------------------------------------------------")
        panjang = int(input("Masukkan panjang (cm): "))
        lebar = int(input("Masukkan lebar (cm): "))
        hasil_luas = bangun.duadimensi.luas_persegi_panjang(panjang, lebar)
        print("hasil dari Luas Kubus tersebut adalah = {}".format(hasil_luas))
        menu_option_2d()

    elif sub_pilihan == "3":
        print("Menghitung Hasil Luas Segitiga")
        print("-------------------------------------------------------")
        alas = int(input("Masukkan alas (cm): "))
        tinggi = int(input("Masukkan tinggi (cm): "))
        hasil_luas = bangun.duadimensi.luas_segitiga(alas, tinggi)
        print("hasil dari Luas Segitiga tersebut adalah = {}".format(hasil_luas))
        menu_option_2d()

    elif sub_pilihan == "4":
        print("Menghitung Hasil Luas Lingkaran")
        print("-------------------------------------------------------")
        jari_jari = int(input("Masukkan jari-jari (cm): "))
        hasil_luas = bangun.duadimensi.luas_lingkaran(jari_jari)
        print("hasil dari Luas Kubus tersebut adalah = {}".format(hasil_luas))
        menu_option_2d()        

    elif sub_pilihan == "5":
        print("Menghitung Hasil Luas Jajar Genjang")
        print("-------------------------------------------------------")
        alas = int(input("Masukkan alas (cm): "))
        tinggi = int(input("Masukkan tinggi (cm): "))
        hasil_luas = bangun.duadimensi.luas_jajar_genjang(alas, tinggi)
        print("hasil dari Luas Jajar Genjang tersebut adalah = {}".format(hasil_luas))
        menu_option_2d()        

    elif sub_pilihan == "6":
        print("Menghitung Hasil Luas Trapesium")
        print("-------------------------------------------------------")
        sisi_sejajar_1 = int(input("Masukkan Sisi sejajar 1 (cm): "))
        sisi_sejajar_2 = int(input("Masukkan Sisi Sejajar 2 (cm): "))
        tinggi = int(input("Masukkan Tinggi (cm): "))
        hasil_luas = bangun.duadimensi.luas_trapesium(sisi_sejajar_1, sisi_sejajar_2, tinggi)
        print("hasil dari Luas Trapesium tersebut adalah = {}".format(hasil_luas))
        menu_option_2d()    

    elif sub_pilihan == "7":
        main_menu()

    elif sub_pilihan == "8":
        print("Terima kasih telah menggunakan program kami.")
        exit()    

    else:
        print("Pilihan tidak valid, silakan coba lagi.")
        menu_option_2d()

main_menu()