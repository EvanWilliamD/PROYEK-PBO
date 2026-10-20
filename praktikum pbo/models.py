class Reservasi:

    def __init__(self, nama, nomor_booking, tipe_lapangan, durasi):
        self.nama = nama
        self.nomor_booking = nomor_booking
        self.tipe_lapangan = tipe_lapangan
        self.durasi = durasi

    def to_list(self):
        return [self.nama, self.nomor_booking, self.tipe_lapangan, self.durasi]

    def __str__(self):
        return f"{self.nama} dengan nomor reservasi {self.nomor_booking} (Tipe Lapangan: {self.tipe_lapangan}) disewa selama {self.durasi} jam"

