username= "yoga"
password= 49

while True:
    username =input("masukkan username:")
    password =int(input("masukkan password:"))

    if username== "yoga":
        if password== 49:
            print("login berhasil")
            break
        else:
            print("username atau password tidak sesuai")
    else:
        print("gagal login!coba lagi")



while True:
    golongan =input("Masukkan golongan darah (A, B, AB, O): ") 
    if golongan =="A":
        rhesus = input("Masukkan rhesus (+ / -): ")
        if rhesus == "+":
            golongan_rh ="golongan darah = A+"
            print(golongan_rh)
        elif rhesus == "-":
            golongan_rh ="golongan darah = A-"
            print(golongan_rh)
        else:
            print("rhesus tidak valid!")
            continue

    elif golongan == "B":
        rhesus = input("Masukkan rhesus (+ / -):")
        if rhesus == "+":
            golongan_rh ="golongan darah = B+"
            print(golongan_rh)
        elif rhesus == "-":
            golongan_rh ="golongan darah = B-"
            print(golongan_rh)
        else:
            print("Rhesus tidak valid!")
            continue

    elif golongan == "AB":
        rhesus = input("Masukkan rhesus (+ / -): ")
        if rhesus == "+":
            golongan_rh ="golongan darah = AB+"
            print(golongan_rh)
        elif rhesus == "-":
            golongan_rh ="golongan darah = AB-"
            print(golongan_rh)
        else:
            print("Rhesus tidak valid")
            continue

    elif golongan == "O":
        rhesus = input("Masukkan rhesus (+ / -): ")
        if rhesus == "+":
            golongan_rh ="golongan darah = O+"
            print(golongan_rh)
        elif rhesus == "-":
            golongan_rh ="golongan darah = O-"
            print(golongan_rh)
        else:
            print("Rhesus tidak valid")
            continue

            
    jumlah_kantong_darah = int(input("Masukkan banyak kantong darah:"))
    ml = jumlah_kantong_darah * 500
    print(f"total darah = {ml} ml")

    
    ulang = input('Apakah anda ingin menginput lagi? (Y/T): ')
    if ulang == 'T':
        break
    elif ulang == 'Y':
        continue
    else:
        print("Jawaban anda tidak valid, program ini akan berhenti")
        break


print("\n===Selesaai===")
print("Terima kasih! Program telah selesai")
