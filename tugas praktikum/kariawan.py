hari_minggu = False
tanggal_merah = False
sedang_cuti = True
boleh_libur = hari_minggu or tanggal_merah or sedang_cuti
print(f"4. Boleh tidak masuk kantor? {boleh_libur}") 
# Hasil: True (meski bukan hari libur umum, karyawan sedang cuti)
