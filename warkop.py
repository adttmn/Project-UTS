import Modul

pesanan, nama_pesanan, harga, qty_pesanan, total_harga = Modul.pesan_menu()

print("\n")
print("============================================================================")
print("                 Warkop Siap Saji - Rincian Pesanan                       ")
print("============================================================================")
print("{:<5} {:<30} {:<15} {:<10} {:<15}".format("No.", "Pesanan", "Harga", "Qty", "Jumlah"))
print("============================================================================")

for i, (nama, hrg, qty, jumlah) in enumerate(zip(nama_pesanan, harga, qty_pesanan, [h * q for h, q in zip(harga, qty_pesanan)]), start=1):
    print("{:<5} {:<30} Rp. {:<15} {:<5} Rp. {:<8}".format(i, nama, hrg, qty, jumlah))

print("============================================================================")
print("Total Bayar              : Rp. {}".format(total_harga))
pajak = total_harga * 0.1
total_bayar = total_harga + pajak
print("Pajak 10 %               : Rp. {}".format(pajak))
print("Total Bayar              : Rp. {}".format(total_bayar))
uang_bayar = int(input("Masukkan Uang Pembayaran : Rp. "))
uang_kembalian = uang_bayar - total_bayar
print("============================================================================")
print("Kembalian                : Rp. {}".format(uang_kembalian))
print("============================================================================")