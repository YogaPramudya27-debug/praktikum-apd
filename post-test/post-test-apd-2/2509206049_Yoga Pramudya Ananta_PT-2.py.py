suhu = [27, 33, 46, 55, 67, 92]

suhu_f1 = (suhu[0] * 9/5) + 32
suhu_f2 = (suhu[1] * 9/5) + 32
suhu_k3 = (suhu[2] + 273.15) 
suhu_k4 = (suhu[3] + 273.15)        
suhu_r5 = (suhu[4] * 4/5)
suhu_r6 = (suhu[5] * 4/5)

jumlah = suhu_f1 + suhu_f2 + suhu_k3 + suhu_k4 + suhu_r5 + suhu_r6

rata2 = jumlah / len(suhu)

NIM = 49

Bool = NIM < rata2 


print(suhu_f1)
print(suhu_f2)
print(suhu_k3)
print(suhu_k4)
print(suhu_r5)
print(suhu_r6)

print(jumlah)
print(rata2)
print(NIM)

print(bool)

print(suhu[-6:])