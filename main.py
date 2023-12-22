import sys
import time
import random

class Pahlawan:

    def __init__(self, nama, kesehatan, serangan, kekuatan, armor, skill):
        self.nama = nama
        self.kesehatan = kesehatan
        self.serangan = serangan
        self.kekuatan = kekuatan
        self.armor = armor
        self.skill = skill

    @staticmethod
    def loading_spinner():
        chars = "/-\|"
        for char in chars:
            sys.stdout.write('\r' + f'Memuat... {char}')
            sys.stdout.flush()
            time.sleep(0.1)

    def permainan(self):
        self.loading_spinner()
        print("\nPemuatan selesai")
        print(f"Selamat datang, {self.nama}! Pilih aksi:")
        print("[1] Serang Musuh")
        print("[2] Bertahan")
        print("[3] Percakapan dengan NPC")
        pilihan = int(input("Pilihan: "))

        if pilihan == 1:
            self.serang_musuh()
        elif pilihan == 2:
            self.bertahan()
        elif pilihan == 3:
            self.percakapan_npc()
        else:
            print("Pilihan tidak valid. Coba lagi.")

    def faksi(self):
        print("Daftar Faksi:")
        print("[1] Menhoutte")
        print("[2] Houbenne")
        print("[3] Elenor")
        print("[4] Kembali menu")
        pilfaksi = int(input("Pilih faksi: "))

        if pilfaksi == 1:
            self.deskripsi_faksi("Menhoutte")
        elif pilfaksi == 2:
            self.deskripsi_faksi("Houbenne")
        elif pilfaksi == 3:
            self.deskripsi_faksi("Elenor")
        elif pilfaksi == 4:
            self.menu()
        else:
            print("Pilihan tidak valid. Coba lagi.")
            self.faksi()

    def deskripsi_faksi(self, faksi):
        if faksi == "Menhoutte":
            print("Menhoutte adalah faksi yang terkenal dengan keberanian dan keadilan mereka. Mereka mendiami hutan yang subur.")
        elif faksi == "Houbenne":
            print("Houbenne adalah faksi yang ahli dalam seni bela diri dan teknologi. Mereka mendiami kota megah yang modern.")
        elif faksi == "Elenor":
            print("Elenor adalah faksi yang memiliki keahlian dalam sihir dan ilmu pengetahuan. Mereka tinggal di kastil yang megah dan misterius.")
        else:
            print("Faksi tidak dikenal.")

    def pahlawan(self):
        print("Daftar Pahlawan:")
        print("[1] Pahlawan 1 - Nama: Kaenzi, Kekuatan: 100, Armor: 50, Kesehatan: 200, Skill: Fireball")
        print("[2] Pahlawan 2 - Nama: Hanzo, Kekuatan: 80, Armor: 60, Kesehatan: 180, Skill: Ice Shield")
        print("[3] Pahlawan 3 - Nama: Elebra, Kekuatan: 120, Armor: 40, Kesehatan: 220, Skill: Thunder Strike")

    def serang_musuh(self):
        print("Anda menyerang musuh!")
        musuh_kesehatan = random.randint(50, 100)
        musuh_serangan = random.randint(10, 30)
        print(f"Musuh memiliki Kesehatan: {musuh_kesehatan}")
        print("Pertarungan dimulai!")

        while musuh_kesehatan > 0 and self.kesehatan > 0:
            print("\nPilih aksi:")
            print("[1] Serang dengan kekuatan penuh")
            print("[2] Gunakan skill khusus")
            print("[3] Bertahan")
            pilihan_serang = int(input("Aksi: "))

            if pilihan_serang == 1:
                print("Anda menyerang musuh dengan kekuatan penuh!")
                musuh_kesehatan -= self.serangan * 2
            elif pilihan_serang == 2:
                print(f"Anda menggunakan skill khusus {self.skill}!")
                musuh_kesehatan -= self.kekuatan + random.randint(10, 20)
            elif pilihan_serang == 3:
                print("Anda memilih untuk bertahan. Anda mendapatkan bonus Armor.")
                self.kesehatan += self.armor

            self.kesehatan -= musuh_serangan
            print(f"Kesehatan Musuh: {musuh_kesehatan} | Kesehatan Anda: {self.kesehatan}")

        if self.kesehatan <= 0:
            print("Anda kalah! Game Over.")
        else:
            print("Anda menang! Selamat!")

    def bertahan(self):
        print("Anda memilih untuk bertahan.")
        print("\nPilih cara bertahan:")
        print("[1] Bertahan dengan Armor")
        print("[2] Hindari serangan")
        pilihan_bertahan = int(input("Aksi: "))

        if pilihan_bertahan == 1:
            print("Anda bertahan dengan Armor. Anda mendapatkan bonus Armor.")
            self.kesehatan += self.armor
        elif pilihan_bertahan == 2:
            print("Anda berhasil menghindari serangan musuh.")
        else:
            print("Pilihan tidak valid. Coba lagi.")

    def percakapan_npc(self):
        print("Anda memulai percakapan dengan NPC. NPC: 'Selamat datang, petualang!'")
        time.sleep(0.1)
        print("NPC: 'Saya membutuhkan bantuanmu, petualang! Apakah kamu bersedia membantu? [Y/N]'")
        pilQuest = input("Jawaban: ")

        if pilQuest.upper() == "Y":
            print("Petualang: Apa kabar?")
            time.sleep(0.1)
            print("Petualang: Semoga baik-baik saja. Saya siap membantu Anda.")

    def info_permainan(self):
        print("\n=== INFO PERMAINAN ===")
        print("BARATA WAR GAMES by Azhar")
        print("Selamat datang di Dunia Fantasi!")
        print("Dalam permainan ini, Anda akan memimpin seorang pahlawan untuk menjelajahi dunia yang penuh petualangan.")
        print("Bertemu dengan berbagai faksi, lawan musuh, dan temukan kekuatan pahlawan Anda.")
        print("Setiap pilihan Anda akan mempengaruhi perkembangan cerita dan hasil pertempuran.")
        print("Selamat bersenang-senang!")

    def deskripsi_panjang(self):
        print("\n=== DESKRIPSI DETAIL ===")
        print("Dunia Fantasi adalah sebuah dunia yang dipenuhi dengan misteri dan keajaiban.")
        print("Di sini, tiga faksi kuat bersaing untuk memperebutkan kekuasaan dan sumber daya.")
        print("Menhoutte, dengan keberanian dan keadilan, mendiami hutan yang subur.")
        print("Houbenne, ahli dalam seni bela diri dan teknologi, membanggakan kota megah yang modern.")
        print("Elenor, faksi yang mahir dalam sihir dan ilmu pengetahuan, bersemayam di kastil megah dan misterius.")
        print("Pahlawan-pahlawan seperti Kaenzi, Hanzo, dan Elebra akan menjadi pion utama dalam perjalanan Anda.")
        print("Anda memiliki kekuatan untuk memilih faksi, mengelola pahlawan, dan menentukan nasib dunia ini.")
        print("Program ini dibuat oleh Azhar. Selamat bermain!")

    def menu(self):
        print("BARATA WAR GAMES by Azhar")
        print("Menu Permainan:")
        print("\n")
        print("[1] Mulai Permainan")
        print("\n")
        print("[2] Faksi")
        print("\n")
        print("[3] Pahlawan")
        print("\n")
        print("[4] Info Permainan")
        print("\n")
        print("="*20)
        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            self.permainan()
        elif pilihan == 2:
            self.faksi()
        elif pilihan == 3:
            self.pahlawan()
        elif pilihan == 4:
            self.info_permainan()
            self.deskripsi_panjang()
        else:
            print("Pilihan tidak valid. Coba lagi.")

# Contoh penggunaan:
pahlawan_saya = Pahlawan("Pahlawan1", 200, 30, 100, 50, "Fireball")
pahlawan_saya.menu()
