# Input jumlah mahasiswa
jumlah_orang = int(input("Masukkan jumlah orang: "))
pensiun = int(input("Masukkan usia pensiun: "))

# List untuk menyimpan data mahasiswa
data_orang = []

# Loop untuk mengisi data mahasiswa
for i in range(1, jumlah_orang + 1):
    print(f"Data orang ke-{i}:")
    n = input("Masukkan nama: ")
    if n.isalpha():
        nama = n.replace('a', '').replace('i', '').replace('u', '').replace('e', '').replace('o', '*')
    else:
        print("Nama harus berupa huruf")
    usia = int(input("Masukkan usia sekarang ini: "))
    
    # Menentukan sisa nilai
    sisa_umur = pensiun - usia if usia < pensiun else 0
    
    # Menambahkan ke list data_mahasiswa
    data_orang.append((nama, usia, sisa_umur))

# Output daftar mahasiswa
print("\nDaftar Mahasiswa:")
for i in range(len(data_orang)):
    nama, usia, sisa_umur = data_orang[i]
    status = (f"{int(sisa_umur)} lagi untuk ke umur {pensiun} tahun" if sisa_umur > 0 else "Sudah pensiun")
    print(f"{i+1}. {nama} (Umur: {usia}) {status}")

# Menentukan orang dengan usia paling tua
orang_tua = max(data_orang, key=lambda x: x[1])
nama_tertua, usia_tertua, _ = orang_tua
print(f"\nOrang dengan usia paling tua: {nama_tertua} (Umur: {usia_tertua})")