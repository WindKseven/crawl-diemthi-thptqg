import csv

sbd = input("Nhap SBD: ")
diemthi_sbd = ''

with open('diemthi.csv',mode='r', encoding='utf-8') as sbd_diemthi:
    readd = csv.reader(sbd_diemthi)
    for sbd_user in readd:
        line = ''.join(sbd_user)
        if sbd in line:
            diemthi_sbd = line
            break

if diemthi_sbd: print(diemthi_sbd)
else: print("Khong co ket qua!")
