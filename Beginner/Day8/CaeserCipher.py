import Caeser_art

def encrypt(message,key):
    list1=list(message)
    for i in range(len(message)):
        char=message[i]
        if list1[i]==' ':
            continue
        if not list1[i].isalpha():
            print("Invalid\n")
            continue
        if list1[i].isupper():
            list1[i]=chr((ord(char)-65+key)%26 + 65)
            continue
        list1[i]=chr((ord(char)-97+key)%26 + 97)
    str1=''.join(list1)
    print(f"Your Encrypted message:{str1}\n")

def decrypt(message,key):
    list1=list(message)
    for i in range(len(message)):
        char=message[i]
        if list1[i]==' ':
            continue
        if not list1[i].isalpha():
            print("Invalid\n")
            continue
        if list1[i].isupper():
            list1[i]=chr((ord(char)-65-key)%26 + 65)
            continue
        list1[i]=chr((ord(char)-97-key)%26 + 97)
    str1=''.join(list1)
    print(f"Your Decrypted message:{str1}\n")




while True:
    Caeser_art.logo()
    print("Welcome to Caeser Cipher......\n")
    user_choice=input('To "Encrypt" a message type "encrypt".To "Decrypt" a message type "decrypt".\n').lower()

    secretMessage=input("Enter the secret message here:\n")
    shiftKey=int(input("Enter the shift value(0-25):\n"))

    if user_choice == "encrypt":
        encrypt(secretMessage,shiftKey)
    elif user_choice == "decrypt":
        decrypt(secretMessage,shiftKey)
    else:
        print("Invalid Choice\n")
        continue

    proceed=input('Enter "Yes" to keep going and "No" to exit.\n').lower()
    if proceed=="yes":
        continue
    else:
        break

print("Thank u for using Caeser Cipher.....")