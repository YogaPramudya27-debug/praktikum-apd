Username =input("Masukkan Username: ")
Password = int(input("Masukkan Password: "))

if Username == "yoga": 
    if Password == 49:
        print("Lanjut ke kalkulator")
    else: 
        print("salah satu salah")    
else:
    print("Program berakhir")

def konversi_panjang():
            print("konversikan panjang")
            print("1. kaki (feet) -> meter")
            print("2. kilometer -> meter")
            print("3. centimeter -> meter")
            pilihan = int(input("pilih konversi: "))
            
            if pilihan == 1:
                kaki=float(input("masukkan panjang (feet): "))
                print("hasil:", kaki * 0.3048, "meter")
            elif pilihan == 2:
                km=float(input("masukkan panjang (kilometer): "))
                print("hasil:", km * 1000, "meter")
            elif pilihan == 3:
                cm=float(input("masukkan panjang (centimeter): "))
                print("hasil", cm / 100, "meter")
            else:
                print("pilihan tidak valid")    

def konversi_massa():
        print("konversikan massa")
        print("1. pon (pound) -> kilogram")
        print("2. ton -> kilogram")
        print("3. gram -> kilogram")
        pilihan = int(input("Pilih konversi: "))
        
        if pilihan == 1:
            pon = float(input("Masukkan massa (pound): "))       
            print("hasil:", pon * 0.453592, "kg")
        elif pilihan == 2:
            ton = float(input("Masukkan massa (ton): "))   
            print("hasil:", ton * 1000, "kg")
        elif pilihan == 3:
            gram = float(input("Masukkan massa (gram): "))   
            print("hasil:", gram / 1000, "kg")
        else:
            print("Pilihan tidak valid")
        

def konversi_suhu():
            print("koversikan suhu")
            print("1. Celcius ➝ Kelvin")
            print("2. Fahrenheit ➝ Kelvin")
            print("3. Reamur ➝ Kelvin")
            pilihan = int(input("Pilih konversi: "))
            
            if pilihan == 1:
                c = float(input("Masukkan suhu (°C): "))   
                print("hasil:", c + 273.15, "K")
            elif pilihan == 2:
                f = float(input("Masukkan suhu (°F): "))
                print("hasil:", (f - 32) * 5/9 + 273.15, "K")
            elif pilihan == 3:
                r = float(input("Masukkan suhu (°Re): "))       
                print("hasil:", (r * 5/4) + 273.15, "K")
            else:
                print("Pilihan tidak valid")


def konversi_waktu():
            print("konversikan waktu")
            print("1. menit ➝ detik")
            print("2. jam ➝ detik")
            pilihan = int(input("Pilih konversi: "))
            
            if pilihan == 1:
                menit = float(input("Masukkan waktu (menit): "))
                print("hasil:", menit * 60, "detik")
            elif pilihan == 2:
                jam = float(input("Masukkan waktu (jam): "))
                print("hasil:", jam * 3600, "detik")
            else:
                print("Pilihan tidak valid")



print("\n=== Kalkulator Konversi Satuan ke SI ===")
print("1. Konversikan panjang")
print("2. Konversikan massa")
print("3. Konversikan suhu")
print("4. Konversikan waktu")
print("5. Keluar")

menu = int(input("Pilih menu: "))

if menu == 1:
        konversi_panjang()
elif menu == 2:
        konversi_massa()
elif menu == 3:
        konversi_suhu()
elif menu == 4:
        konversi_waktu()
elif menu == 5:
        print("Program selesai.")
else:
        print("Menu tidak valid, coba lagi.")