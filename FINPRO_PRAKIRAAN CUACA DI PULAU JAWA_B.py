from requests_html import HTMLSession
from datetime import date
import datetime
s = HTMLSession()
import time
waktu = time.localtime()
hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
daftar_kota = ['Surabaya','Madiun','Kediri','Blitar','Malang','Batu',
               'Tangerang','Serang','Jakarta','Kembangan','Bandung','Banjar',
               'Bekasi','Cimahi','Cirebon','Tasikmalaya','Sukabumi','Sumedang'
               ,'Purwokerto','Jepara','Kudus','Klaten','Sragen','Magelang',
               'Semarang','Tegal','Kediri','Yogyakarta','Sleman','Bangkalan',
               'Banyuwangi','Gresik','Jember','Jombang','Lamongan','Lumajang',
               'Sidoarjo','Ngawi','Nganjuk','Mojokerto','Probolinggo','Sampang',
               'Sumenep','Bangkalan']

print("=====================================================")
print("PROGRAM MENENTUKAN CUACA PADA KOTA DI PULAU JAWA")
print("=====================================================")

def question():
    print("\nMenu yang tersedia:\n")
    print("___________________________________")
    print("[1] Lihat daftar kota yang tersedia")
    print("[2] Lihat Cuaca saat ini")
    print("[3] Ramalan cuaca")
    print("[4] Hentikan sistem")
    print("___________________________________")








def ambildatasaatini():
    query = str(input("Inputkan nama kota yang tersedia \n"))
    while True:
        if query in daftar_kota:
            date_object = datetime.date.today()
            url = f'https://www.google.com/search?q=cuaca+{query}'
            r = s.get(url, headers={
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})
            print("\n•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*•*´¨`*•.")
            print("Cuaca sekarang di", (query),(date_object))
            print(("Waktu"),r.html.find('div.VQF4g', first=True).find('div.wob_dts', first=True).text)
            print("•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*´¨`*•.¸¸.•*•*´¨`*•.")
            print(("\n🌡️  Suhu"),r.html.find('span#wob_tm',first=True).text,("°Celcius"))
            print(("🛫 Endapan air di awan"),r.html.find('div.wtsRwe', first=True).find('span#wob_pp', first=True).text)
            print(("🌬  Kelembapan"), r.html.find('div.wtsRwe', first=True).find('span#wob_hm', first=True).text)
            print(("🍃 Angin"), r.html.find('div.wtsRwe', first=True).find('span#wob_ws', first=True).text)
            print((" ☁ Hasil cuaca"),r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text)
            print("Selesai")
            break
        else:
            print("Nama kota tidak tersedia,Silahkan lihat daftar kota\n")
            ambildatasaatini()
            break

def ramalan():
    print("Tanggal saat ini :")
    import datetime
    tanggal_saat_ini = datetime.date.today()
    print(tanggal_saat_ini)
    query = str(input("Inputkan nama kota yang tersedia \n"))
    while True:
        if query in daftar_kota:
            print("\n")
            break
        else:
            print("Nama kota tidak tersedia,Silahkan lihat daftar kota\n")
            ramalan()
            break


def cekramalan():
    query3 = str(input("Inputkan hari yang ingin diramal  \n"))
    hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']
    while True:
        if query3 == hari[waktu[6]]:
            print("Cuaca gagal diramal")
            print("Inputkan ulang\n")
            cekramalan()
            break
        elif query3 in hari:
            print("\nMemulai Peramalan 🔎")
            url2 = f'https://www.google.com/search?q=cuaca+sidoarjo+{query3}'
            r2 = s.get(url2, headers={'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"})
            print(".·:*¨¨*:·. .·:*¨¨*:·..·:*¨¨*:·. .·:*¨¨*:·.")
            print("Ramalan cuaca")
            print(("Hari"), r2.html.find('div.VQF4g', first=True).find('div.wob_dts', first=True).text, ("besok"))
            print(".·:*¨¨*:·. .·:*¨¨*:·..·:*¨¨*:·. .·:*¨¨*:·.")
            print(("\n🌡️  Suhu"), r2.html.find('span#wob_tm', first=True).text, ("°Celcius"))
            print(("🛫 Endapan air di awan"), r2.html.find('div.wtsRwe', first=True).find('span#wob_pp', first=True).text)
            print(("🌬  Kelembapan"), r2.html.find('div.wtsRwe', first=True).find('span#wob_hm', first=True).text)
            print(("🍃 Angin"), r2.html.find('div.wtsRwe', first=True).find('span#wob_ws', first=True).text)
            print((" ☁ Hasil ramalan cuaca"), r2.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text)
            print("Selesai")
            break
        else:
            print("Kesalahan penulisan ")
            print("Inputkan ulang")
            cekramalan()
            break

def alur_ramalan():
    ramalan()
    cekramalan()




def alur3():
    while True:
        kembali = str(input("\n0 untuk Kembali\n"))
        if kembali == "0":
            alur2()
            break
        else:
            print("\nInputan tidak sesuai,gagal dijalankan")
            print("Inputkan ulang")
            alur3()
            break

def alur2():
    question()
    menu = str(input("\nInputkan menu pilihan\n"))
    while True:
        if menu == "4":
            print("Sistem dihentikan")
            break
        elif menu == "1":
            print("\nKota yang tersedia")
            print(daftar_kota)
            print("\n-----------------------------")
            print("[0] Untuk kembali")
            print("-----------------------------")
            alur3()
            break
        elif menu == "2":
            ambildatasaatini()
            print("\n-----------------------------")
            print("[0] Untuk kembali")
            print("-----------------------------")
            alur3()
            break
        elif menu == "3":
            alur_ramalan()
            print("\n-----------------------------")
            print("[0] Untuk kembali")
            print("-----------------------------")
            alur3()
            break
        else:
            print("Inputan tidak sesuai,sistem berulang")
            alur2()
            break


alur2()