import csv
import os
from models import Reservasi

def simpan_reservasi():
    print("\n=== TAMBAH DATA BUKU ===")

    nama = input("Nama   : ").strip()
    nomor_booking = input("Nomor Booking : ").strip()
    tipe_lapangan = input("Tipe Lapangan    : ").strip()
    durasi = input("Durasi  :  ").strip()

    if not nama or not nomor_booking or not tipe_lapangan or not durasi:
        print("\n[PERINGATAN] Semua kolom harus diisi!\n")
        return

    reservasi = Reservasi(nama, nomor_booking, tipe_lapangan, durasi)

    file_exists = os.path.exists("reservasifutsal.csv")

    with open("reservasifutsal.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Nama", "Nomor Reservasi", "Tipe Lapangan", "Durasi"])

        writer.writerow(reservasi.to_list())

    print("\n[BERHASIL] Telah dimasukkan ke data.\n")

def main():
    while True:
        print("=== MENU TAMBAH RESERVASI  ===")
        print("1. Tambah Reservasi")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            simpan_reservasi()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    main()
