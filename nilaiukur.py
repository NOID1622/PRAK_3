#input
jarak=int(input('Jarak : '))
batas_untukA=int(input('Batas : '))
nilai=int(input('Nilai : '))
#proses
nilai_amin=batas_untukA-jarak
nilai_bpls=nilai_amin-jarak
nilai_b=nilai_bpls-jarak
nilai_bmin=nilai_b-jarak
nilai_cplus=nilai_bmin-jarak
nilai_c=nilai_cplus-jarak
nilai_d=nilai_c-jarak
nilai_e=nilai_d-jarak

if nilai>=batas_untukA:
    print('A')
elif nilai>=nilai_amin:
    print('A-')
elif nilai>=nilai_bpls:
    print('B+')
elif nilai>=nilai_b:
    print('B')
elif nilai>=nilai_bmin:
    print('B-')
elif nilai>=nilai_cplus:
    print('C+')
elif nilai>=nilai_c:
    print('C')
elif nilai>=nilai_d:
    print('D')
else :
    print('E')
