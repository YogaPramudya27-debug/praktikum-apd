from utils import clear_screen, pause
from prettytable import PrettyTable

rental_data = []

def lihat_data():
    clear_screen()
    print('=== DATA PENYEWAAN ===')
    if not rental_data:
        print('Belum ada data penyewaan.')
    else:
        table = PrettyTable()
        table.field_names = ['No', 'Nama', 'jenis PS', 'Durasi (jam)', 'harga', 'Total', 'Petugas']
        for i, data in enumerate(rental_data, start=1):
            table.add_row([i, data['nama'], data['ps'], data['durasi'], data['harga'], data['total'], data['petugas']])
        print(table)
    pause()

def tambah_data(petugas, role ='user'):
    clear_screen()
    print('=== TAMBAH DATA PENYEWAAN ===')
    try:
        nama = input('Nama penyewa: ')
        jenis_ps = input('Jenis PS: ')
        durasi = input('Durasi sewa (jam): ')

        if role == 'user':
            harga = 10000
            print(f'Harga sudah tercantum: Rp {harga}/jam')
        else:
            harga = input('Harga per jam: ')
            if not harga.isdigit():
                raise ValueError('Harga harus berupa digit atau angka!')
            harga = int(harga)

        if not durasi.isdigit():
            raise ValueError('Durasi harus berupa angka atau digit!')

        total = int(durasi) * int(harga)
           
        rental_data.append({
            'nama': nama,
            'ps': jenis_ps,
            'durasi': durasi,
            'harga': harga,
            'total': total,
            'petugas': petugas
        })
        print('Data berhasil ditambahkan!')
    except Exception as e:
        print('Terjadi kesalahan:', e)
    finally:
        pause()

def ubah_data():
    clear_screen()
    lihat_data()
    index = int(input('Pilih nomor data yang ingin diubah: '))
    print('=== UBAH DATA PENYEWAAN ===')
    try:
        if 1 <= index <= len(rental_data):
            durasi = input('Durasi baru (jam): ')
            harga = input('Harga baru: ')
            if durasi.isdigit() and harga.isdigit():
                total = int(durasi) * int(harga)
                rental_data[index - 1]['durasi'] = durasi
                rental_data[index - 1]['harga'] = harga
                rental_data[index - 1]['total'] = total
                print('Data berhasil diubah!')
            else:
                print('Durasi dan harga harus angka!')
        else:
            print('Nomor data tidak valid!')
    except Exception as e:
        print('Terjadi kesalahan:', e)
    pause()

def hapus_data():
    clear_screen()
    print('=== HAPUS DATA PENYEWAAN ===')
    for i, data in enumerate(rental_data, 1):
        print(f"{i}. {data['nama']}")
    try:
        hapus = int(input('Masukkan nomor data yang ingin dihapus: '))
        if 1 <= hapus <= len(rental_data):
            del rental_data[hapus - 1]
            print('Data berhasil dihapus!')
        else:
            print('Nomor data tidak valid!')
    except ValueError:
        print('Masukkan angka yang benar!')
    except Exception as e:
        print('Terjadi kesalahan:', e)
    pause()
