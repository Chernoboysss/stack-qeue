from qeue import qeuee
import os


def main() :
    os.system("cls")
    data = qeuee()
    
    while True :
        print("ANTRIAN QEUE")
        print("="*12)
        print(
        """
        1.insert antrian
        2.remove antrian
        3.banyak antrian
        4.output antrian 
        0.end
        """
        )
        
        inputuser = str(input("silahkan dipilih : "))
        if inputuser == "1" :
            item = input("Masukan data : ")
            data.addrear(item)
            print("\nSUCCESS\n")
            input("\nkembali ke menu...")
            os.system("cls")
        
        elif inputuser == "2" :
            data.removerear()
            print("\nSUCCESS\n")
            input("\nkembali ke menu...")
            os.system("cls")
            
        elif inputuser == "3" :
            print(
                "\nbanyaknya antrian =",data.size()
            )
            input("\nkembali ke menu...")
            os.system("cls")
            
        elif inputuser == "4" :
            for x in range(len(data.qeue)) :
                print(x + 1,". ",data.qeue[x])   
            
            input("\nkembali ke menu...")
            os.system("cls")
            
        elif inputuser == "0" :
            break
    


if __name__ == "__main__" :
    main()