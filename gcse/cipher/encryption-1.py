#Encryption Program #1
#Sept 9th 2015
#Made by Elisabeth Morgan

import time

Key = 4

def Encryption(Key=Key):

    Ciphertext = ''
    Text = input("\nPlease enter a phrase you would like to encrypt.\n>>> ")

    for i in range(len(Text)):
        if (ord(Text[i]) in (range(91 - Key, 91))) or (ord(Text[i]) in range(123 - Key, 123)):
            Ciphertext += chr(ord(Text[i]) + Key - 26)

        elif (ord(Text[i]) not in range(65, 91)) and (ord(Text[i]) not in range(97, 123)):
            Ciphertext += chr(ord(Text[i]))

        else:
            Ciphertext += chr(ord(Text[i]) + Key)

    print("\nYour ciphertext is: ", Ciphertext)

def Decryption(Key=Key):

    Text = ''
    Ciphertext = input("\nPlease enter a phrase you would like to decrypt.\n>>> ")

    for i in range(len(Ciphertext)):
        if (ord(Ciphertext[i]) in (range(65, 65 + Key))) or (ord(Ciphertext[i]) in range(97, 97 + Key)):
            Text += chr(ord(Ciphertext[i]) - Key + 26)

        elif (ord(Ciphertext[i]) not in range(65, 91)) and (ord(Ciphertext[i]) not in range(97, 123)):
            Text += chr(ord(Ciphertext[i]))

        else:
            Text += chr(ord(Ciphertext[i]) - Key)

    print("\nYour message is: ", Text)

while True:
    Choice = input("""
=============================== ENCRYPTION ===============================

What would you like to do?

Type '1' to encrypt a message.
Type '2' to decrypt a message.
Type '3' to change the encryption key (Current: """ + str(Key) + """).
Type '0' to exit.

>>> """)
    time.sleep(0.5)

    if Choice == '1':
        Encryption()

    elif Choice == '2':
        Decryption()

    elif Choice == '3':
        Key = input("\nWhat would you like the new encryption key to be? [1-25]\n>>> ")
        time.sleep(0.5)

        if Key.isdigit() and 0 < int(Key) < 26:
            print("\nThe new encryption key is now ", Key, ".")
            Key = int(Key)

        else:
            print("\nInvalid encryption key!")
            Key = 4

    elif Choice == '0':
        print("\nThank you.")
        break

    else:
        print("\nInvalid option! Please choose again.")

    time.sleep(1.5)

#ABCDEFGHIJKLMNOPQRSTUVWXYZ ;.~:@'#>_<-+=/\|,?"£$%^&*()[]}{ abcdefghijklmnopqrstuvwxyz !!!
