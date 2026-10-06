baterai_kritis = False
suhu_overheat = False
tombol_sos = False
mode_darurat = baterai_kritis or suhu_overheat or tombol_sos
print(f"5. HP masuk mode darurat? {mode_darurat}") 
# Hasil: False (karena tidak ada satupun kondisi darurat yang terjadi)