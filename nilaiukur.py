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
    
    
#auiwgqr
#input
player1 = int(input("masukan nilai player 1 : "))
player2 = int(input("masukan nilai player 2 : "))
player3 = int(input("masukan nilai player 3 : "))

#proses and output
if player1 == player2 == player3:
    print("tidak ada yang pemenang ")
elif player1 > 21 and player2 >21 and player3 > 21:
    print("tidak ada yang pemenang")
elif player1 <= 21 and player1 > player2 and player1 > player2:
    print("pemenangnya adalah p1")
elif player2 <= 21 and player2 > player1 and player2 > player3: 
    print("pemenangnya p2")
elif player1 > 21 and player2 <= 21 and player3 > 21:
    print("pemenangnya p2")
elif player3 <= 21 and player3 > player1 and player3 > player2:
    print("pemenangnya pemain 3")
elif player1 <= 21 and abs(21 - player2) and abs(21-player1) and abs (21 - player3):
    print("maka tidak ada pemenang")
else:
    print('input anda salah')

