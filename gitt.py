# Datpanen
data_panen = {
    'lokasi1': {
        'nama_lokasi': 'Kebun A',
        'hasil_panen': {
            'padi': 1200,
            'jagung': 800,
            'kedelai': 500
        }
    },
    'lokasi2': {
        'nama_lokasi': 'Kebun B',
        'hasil_panen': {
            'padi': 1500,
            'jagung': 900,
            'kedelai': 450
        }
    },
    'lokasi3': {
        'nama_lokasi': 'Kebun C',
        'hasil_panen': {
            'padi': 1100,
            'jagung': 750,
            'kedelai': 600
        }
    },
    'lokasi4': {
        'nama_lokasi': 'Kebun D',
        'hasil_panen': {
            'padi': 1300,
            'jagung': 850,
            'kedelai': 550
        }
    },
    'lokasi5': {
        'nama_lokasi': 'Kebun E',
        'hasil_panen': {
            'padi': 1400,
            'jagung': 950,
            'kedelai': 480
        }
    }
}

# no 1
print("Seluruh data panen:")
for lokasi, data in data_panen.items():
    print(f"Lokasi: {data['nama_lokasi']}")
    for hasil, jumlah in data['hasil_panen'].items():
        print(f"  {hasil.capitalize()}: {jumlah}")
print("\n")

# no 2
jagung_lokasi2 = data_panen['lokasi2']['hasil_panen']['jagung']
print(f"Hasil panen jagung dari lokasi2: {jagung_lokasi2}")
print("\n")

# no 3
nama_lokasi3 = data_panen['lokasi3']['nama_lokasi']
print(f"Nama lokasi dari lokasi3: {nama_lokasi3}")
print("\n")

# no 4
hasil_padi = {lokasi: data['hasil_panen']['padi'] for lokasi, data in data_panen.items()}
hasil_kedelai = {lokasi: data['hasil_panen']['kedelai'] for lokasi, data in data_panen.items()}
print("Hasil panen padi per lokasi:", hasil_padi)
print("Hasil panen kedelai per lokasi:", hasil_kedelai)
print("\n")

# no 5
total_padi = sum(hasil_padi.values())
total_kedelai = sum(hasil_kedelai.values())
print(f"Total hasil panen padi: {total_padi}")
print(f"Total hasil panen kedelai : {total_kedelai}")
print("\n")

# no 6
print("Status lokasi berdasarkan hasil panen :")
for lokasi, data in data_panen.items():
    padi = data['hasil_panen']['padi']
    jagung = data['hasil_panen']['jagung']
    if padi > 1300 or jagung > 800:
        print(f"{data['nama_lokasi']} memerlukan perhatian khusus.")
    else:
        print(f"{data['nama_lokasi']} dalam kondisi baik.")
print("\n")

print("berubah di branch Baru")