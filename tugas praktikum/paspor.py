# Kasus 1: Syarat Terbang ke Luar Negeri
# Penumpang bisa berangkat HANYA JIKA paspor aktif, punya visa, DAN tiket sudah lunas.
paspor_aktif = True
punya_visa = True
tiket_lunas = True
bisa_berangkat = paspor_aktif and punya_visa and tiket_lunas
print(f"1. Bisa terbang ke luar negeri? {bisa_berangkat}") 
# Hasil: True (karena ketiga syarat terpenuhi)