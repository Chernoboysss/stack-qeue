from stack import stack
import os




def main() :
    os.system("cls")
    data = stack()
    
    while True :
        print("REVERSE STRING")
        print("="*12)
        print(
        """
        1.insert string
        2.reverse string
        0.end
        """
        )
        
        inputuser = str(input("silahkan dipilih : "))
        if inputuser == "1" :
            if data.isempty() == True :
                item = input("Masukan data : ")
                data.addrear(item)
                print("\nSUCCESS\n")
                input("\nkembali ke menu...")
                os.system("cls")
            
            else :
                data.removefront()
                item = input("Masukan data : ")
                data.addrear(item)
                print("\nSUCCESS\n")
                input("\nkembali ke menu...")
                os.system("cls")
                
        
        elif inputuser == "2" :
            print("\n")
            data_reverse = data.reverse()
            if data_reverse == False :
                print("MASUKAN DULU STRINGNYA!!!!")
                input("\nkembali ke menu...")
                os.system("cls")
                
            
            else:
                print(*data.reverse())
                print("\nSUCCESS\n")
                input("\nkembali ke menu...")
                os.system("cls")
                    
        elif inputuser == "0" :
            break

        
        else :
            print("INPUT SALAH")
            input("\nkembali ke menu...")
            os.system("cls")


if __name__ == "__main__" :
    main()