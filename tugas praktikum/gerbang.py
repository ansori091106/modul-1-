tap_kartu_etoll = True
sensor_rfid_terbaca = True
pembayaran_valid = tap_kartu_etoll ^ sensor_rfid_terbaca
print(f"7. Transaksi tol valid (tidak double)? {pembayaran_valid}") 
# Hasil: False (sistem mendeteksi dua input sekaligus, transaksi ditahan/XOR menolak)