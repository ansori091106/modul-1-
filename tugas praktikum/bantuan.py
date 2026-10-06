warga_miskin = False
korban_bencana = True
lansia_sebatangkara = False
dapat_bansos = warga_miskin or korban_bencana or lansia_sebatangkara
print(f"6. Berhak mendapat bansos? {dapat_bansos}") 
# Hasil: True (karena warga tersebut adalah korban bencana alam)