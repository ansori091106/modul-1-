makan_ditempat = True
bawa_pulang = False
status_pesanan_valid = makan_ditempat ^ bawa_pulang
print(f"8. Status pesanan restoran valid? {status_pesanan_valid}") 
# Hasil: True (karena pelanggan memilih secara spesifik hanya