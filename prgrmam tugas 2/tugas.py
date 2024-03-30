 # Fungsi untuk menghitung luas segiempat
def luas_segiempat(panjang, lebar):
    luas = panjang * lebar
    return luas

# Fungsi untuk menghitung luas segitiga
def luas_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi
    return luas

# Fungsi untuk menghitung luas lingkaran
def luas_lingkaran(jari_jari):
    luas = (jari_jari ** 2)
    return luas

# Input panjang dan lebar segiempat
panjang_segiempat = float(input("Masukkan panjang segiempat: "))
lebar_segiempat = float(input("Masukkan lebar segiempat: "))

# Input alas dan tinggi segitiga
alas_segitiga = float(input("Masukkan alas segitiga: "))
tinggi_segitiga = float(input("Masukkan tinggi segitiga: "))

# Input jari-jari lingkaran
jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))

# Hitung luas segiempat, segitiga, dan lingkaran
luas_segiempat_hasil = luas_segiempat(panjang_segiempat, lebar_segiempat)
luas_segitiga_hasil = luas_segitiga(alas_segitiga, tinggi_segitiga)
luas_lingkaran_hasil = luas_lingkaran(jari_jari_lingkaran)

# Cetak hasil
print("Luas segiempat:", luas_segiempat_hasil)
print("Luas segitiga:", luas_segitiga_hasil)
print("Luas lingkaran:", luas_lingkaran_hasil)