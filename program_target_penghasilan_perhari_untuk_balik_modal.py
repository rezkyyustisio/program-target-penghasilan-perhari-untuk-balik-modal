print("PROGRAM TARGET PENGHASILAN PERHARI UNTUK BALIK MODAL")
print()

try:
	jumlah_modal = int(input("Masukan jumlah modal bisnis "))
	target_balik_modal_bulan = int(input("Masukan target balik modal (jumlah bulan) "))
	target_pemasukan_tiap_hari = int(jumlah_modal / (target_balik_modal_bulan * 30))
	print('Target penghasilan perhari: ', target_pemasukan_tiap_hari)
except ValueError:
	print("Yang anda inputkan bukan angka")