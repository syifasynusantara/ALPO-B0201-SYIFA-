import time

class PerekamWaktu:
    def __enter__(self):
        self.mulai = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc, tb):
        self.selesai = time.perf_counter()
        self.durasi = self.selesai - self.mulai
        print(f"Blok kode selesai dieksekusi dalam {self.durasi:.6f} detik")

# Contoh penggunaan:
with PerekamWaktu():
        # Masukkan kode yang ingin di ukur di sini
        daftar_kata = [str(x) for x in range(2_000_000)]
        teks = ",".join(daftar_kata)

        pass
        pass