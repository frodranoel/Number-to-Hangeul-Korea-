from List import basic_sino, basic_puluhribu, basic_ratusan, basic_asli, basic_aslipuluhan

#INFORMATION!
#Bila ingin tes, silahkan ke 
#https://www.google.com/search?q=translate+bahasa+korea&oq=translate+bahasa+korea&aqs=chrome..69i57j0l9.6021j0j7&sourceid=chrome&ie=UTF-8
#lalu langsung ketikan angkanya

def sinokor(n):
    n = str(n)
    panjang_n = len(n)
    n = int(n)

    a = n%10
    b = (n%100 - a)//10
    c = (n%1000 - b*10 -a)//100
    d = (n%10000 - c*100 - b*10 - a)//1000
    ribuan = 3
    ratusan = 2
    puluhan = 1
    if a == 1:
        a = 10
    if d == 0:
        ribuan = 0
    if c == 0:
        ratusan = 0
    if b == 0:
        puluhan = 0
    jumlah = basic_sino[d] + basic_ratusan[ribuan] + basic_sino[c] + basic_ratusan[ratusan] + basic_sino[b] + basic_ratusan[puluhan] + basic_sino[a]
    return jumlah

def pengulangan_sinokor(n):
    n = int(n)
    #dibagi per 10^4
    if n > 10**16:
        print('Maaf, bilangan terlalu besar')
    else:
        a = n%10000
        b = (n//10000)%10000
        c = (n//10000**2)%10000
        d = (n//10000**3)%10000
        e = (n//10000**4)%10000
        stage_4 = 4 #10^16
        stage_3 = 3 #10^12
        stage_2 = 2 #10^8
        stage_1 = 1 #10^4
        if b == 0:
            stage_1 = 0
        if c == 0:
            stage_2 = 0
        if d == 0:
            stage_3 = 0
        if e == 0:
            stage_4 = 0

        print(sinokor(e) + basic_puluhribu[stage_4] + 
        sinokor(d) + basic_puluhribu[stage_3] + 
        sinokor(c) + basic_puluhribu[stage_2] + 
        sinokor(b) + basic_puluhribu[stage_1] + 
        sinokor(a))

def aslikor(n):
    n = int(n)
    a = n%10
    b = (n-a)//10
    if n//10 == 0:
        angka = basic_asli[n]
    elif 1 <= n//10 < 10:
        if n == 20:
            angka = '스무'
        else:
            angka = basic_aslipuluhan[b] + basic_asli[a]
    else:
        angka = 'Maaf, angka terlalu besar'
    return angka
    
def main():
    while True:
        print('-------------------------------------------------------')
        print('Silahkan pilih satuan')
        print('1. Mata uang, nomor telepon, bilangan 100 atau lebih, tanggal, tahun, bulan, tingkat(lantai)')
        print('2. Buah, helai, buku, unit, lembar, gelas, botol, umur, ekor, orang')
        print('3. Tidak jadi')
        u = int(input('>> '))
        if u == 1:
            print('Silahkan masukkan angka')
            n = str(input('>> '))
            print(pengulangan_sinokor(n))
        elif u == 2:
            print('Silahkan masukkan angka')
            n = str(input('>> '))
            print(aslikor(n))
        elif u == 3:
            print('Terima kasih')
            break
        else:
            print('Maaf, tidak ada pilihan tersebut')

main()




