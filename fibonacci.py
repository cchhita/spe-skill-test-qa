n = int(input('Masukan angka: '))

f3 = 0
f1 = 1
f2 = 1
if (n == 0 or n == 1):
    print('Angka fibonacci')
 
else:
    while f3 < n:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == n:
        print('Angka fibonacci')
    else:
        print('Bukan Angka fibonacci')