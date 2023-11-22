print("\n")
print("="*50)
print("                 Warkop Siap Saji         ")
print("="*50)
print("                     Minuman              ")
print("-"*50)
print("             Minuman            Harga     ")
print("-"*50)
print("             Americano          Rp. 15000 ")
print("             Mocca              Rp. 15000 ")
print("             Cappucino          Rp. 10000 ")
print("             Thai Tea           Rp. 5000  ")
print("             Matcha             Rp. 8000  ")
print("             Susu Soda          Rp. 8000  ")
print("-"*50)
print("                     Makanan              ")
print("-"*50)
print("             Makanan            Harga     ")
print("-"*50)
print("             Roti Bakar         Rp. 10000 ")
print("             Indomie            Rp. 10000 ")
print("             Seblak             Rp. 10000 ")
print("             Bakso Aci          Rp. 10000 ")
print("             Pancong            Rp. 10000 ")
print("             Kentang Goreng     Rp. 5000  ")
print("             Pisang Goreng      Rp. 5000  ")
print("="*50)
print('\n')

menu_makanan = {
    "roti bakar": 10000,
    "indomie": 10000,
    "seblak": 10000,
    "bakso aci": 10000,
    "pancong": 10000,
    "kentang goreng": 5000,
    "pisang goreng": 5000
}

menu_minuman = {
    "americano": 15000,
    "mocca": 15000,
    "cappucino": 10000,
    "thai tea": 5000,
    "matcha": 8000,
    "susu soda": 8000
}


pesanan = []
nama_pesanan = []
harga = []
qty_pesanan = []
total_harga = 0

while True:
    pesanan_input = input('Masukkan Nama Menu (ketik "selesai" untuk selesai): ')

    if pesanan_input.lower() == "selesai":
        break

    if pesanan_input.lower() in menu_makanan or pesanan_input.lower() in menu_minuman:
        qty_input = int(input('Masukkan Qty: '))
        
        if pesanan_input.lower() in menu_makanan:
            pesanan.append(pesanan_input)
            nama_pesanan.append(pesanan_input)
            harga.append(menu_makanan[pesanan_input])
            qty_pesanan.append(qty_input)
            total_harga += menu_makanan[pesanan_input] * qty_input
        elif pesanan_input.lower() in menu_minuman:
            pesanan.append(pesanan_input)
            nama_pesanan.append(pesanan_input)
            harga.append(menu_minuman[pesanan_input])
            qty_pesanan.append(qty_input)
            total_harga += menu_minuman[pesanan_input] * qty_input
    else:
        print("Menu tidak valid.")