import secret_hashing as sh
import secret_crypting as sc

def main():
    print('------(SHEDM)essage------')
    while True:
        print('1.Hash \n2.Encode/Decode')
        choice = input('[1,2]: ')

        if choice == '1':
            sh.main()

        elif choice == '2':
            print(' \nSelect encode or decode')

        else:
            pass

if __name__ == '__main__':
    main()