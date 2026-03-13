# membuat kalkulator sederhana dengan python 
# serta logika dasar aritmatika 
# berisi penjumlahan, pengurangan, perkalian, pembagian, perpangkatan, modulus, dan keluar dari program

# Kumpulan list operator
ListOperator = ["Penjumlahan (+)","Pengurangan (-)","Perkalian (*)","Pembagian (/)","Perpangkatan (**)","Modulus (%)","Keluar"]

# fungsi untuk tampilan Banner calculator
def banner():
    print("""

         ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ 
        ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
        ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝
        ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗
        ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║
         ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    """)
# fungsi dari kumpulan list operator
def listoperator():
    print("="*5,"Program Simple Calculator","="*5,"\n")
    for index, item in enumerate(ListOperator, start=1): # 
        print(f"{index}.{item}")
        
        
# fungsi untuk Program utama 
def main():
     # pengulangan kalkulator jika kondisinya benar (true)
    while True:
        try:
            # input operator
            print("\n",15*"=","Operator :",15*"=")
            operator = int(input("Masukkan operator dan pilih(1,2,..6,7) : ")) # masukkan operator berupa angka
            

            # validasi operator
            # nilai range 1-8, kerena angka di dalam bahasa pemrograman dimulai dari 0,
            # maka kita buat range 1-8 untuk operator 1-7
            if operator not in range(1, 8):
                print(f"Maaf, {operator} tidak ada dalam operator. Pilih 1-7.")
                continue
            
            # keputusan untuk akhir program atau keluar dari program
            if operator == 7 :
                print(" Terima kasih sudah menggunakan program ini ")
                break # break untuk berhenti dari program/keluar
            
            # input angka 
            angka1 = float(input("Masukkan Angka1 : ")) # masukkan angka 1
            angka2 = float(input("Masukkan Angka2 : ")) # masukkan angka 2
            
            # jika operator memilih pembagian dan angka 2 adalah nol, 
            # maka akan muncul pesan error dan program akan kembali ke awal untuk memilih operator lagi
            # penanganan khusus untuk pembagian nol
            if operator == 4 and angka2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                continue
            
            ## kondisi dan keputusan yang kita input
            if operator == 1: 
                print("Penjumlahan")
                result = angka1 + angka2
                print(round(result, 3))
            elif operator == 2:
                result = angka1 - angka2
                print(round(result, 3))
            elif operator == 3:
                result = angka1 * angka2
                print(round(result, 3))
            elif operator == 4:
                result = angka1 / angka2
                print(round(result, 3))
            elif operator == 5:
                result = angka1 ** angka2
                print(round(result, 3))
            elif operator == 6:
                result = angka1 % angka2
                print(round(result, 3))
            else:
                print(f"Maaf,{operator} tidak ada dalam operator")
            
        except ValueError: # memastikan nilai input program benar dan solusi agar program tidak error
            print("Pastikan input benar: operator harus angka 1-7, dan angka harus numerik!")       

# ...existing code...

banner() # tampilan Ascii calculator
listoperator() # daftar isi list operator matematika
main() # Memanggil fungsi main() untuk menjalankan program utama
