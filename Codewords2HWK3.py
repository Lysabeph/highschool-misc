#Encodes a word/phrase.
def encode():
    #'codeword' is declared as a string, a word/phrase is entered and each word is entered into a list.
    codeword=''
    txt=input("Would you like to import a textfile?: ").lower()
    if txt=='y':
        file=open('plaintext.txt','r')
        list=file.read()
        print(list)
        list=list.replace('\n\n',' ')
        list=list.split(' ')
        #for i in range(0,len(list)):
            #list[i] = list[i].replace('\n',' ')
    else:
        word=input("Enter a word you would like to encode: ").lower()
        list=word.split(' ')
    #Loops through each value(word) in the list.
    for word in list:
        #If the word is even length, the word is encoded with 'egg'.
        if len(word)%2==0:
            codeword+=word[:len(word)//2]+'egg'+word[len(word)//2:len(word)]+' '
        #If the word is odd length, the word is encoded with 'ga'.
        else:
            codeword+=word[:len(word)//2]+'ga'+word[len(word)//2]+'ga'+word[len(word)//2+1:]+' '
    #Removes white space from the end of the codeword/phrase and outputs the codeword/phrase.
    codeword=codeword[:-1]
    print(codeword)
    file=open('codetext.txt','w')
    file.write(codeword)

#Decodes a word/phrase.
def decode():
    #'word' is declared as a string, a codeword/phrase is entered and each word is entered into a list.
    word=''
    txt=input("Would you like to import a textfile?: ").lower()
    if txt=='y':
        file=open('codetext.txt','r')
        list=file.read()
        list=list.replace('\n\n',' ')
        list=list.split(' ')
        #for i in range(0,len(list)):
            #list[i] = list[i].replace('\n',' ')
    else:
        codeword=input("Enter a word you would like to decode: ").lower()
        list=codeword.split(' ')
    #Loops through each value(word) in the list.
    for codeword in list:
        #If the codeword has been encoded with 'egg', it is decoded appropriately.
        if codeword[len(codeword)//2-1:len(codeword)//2+2]=='egg':
            word+=codeword[:len(codeword)//2-1]+codeword[len(codeword)//2+2:]+' '
        #If the codeword has been encoded with 'ga', it is decoded appropriately.
        elif codeword[len(codeword)//2-2:len(codeword)//2]=='ga' and\
                codeword[len(codeword)//2+1:len(codeword)//2+3]=='ga':
                word+=codeword[:len(codeword)//2-2]+codeword[len(codeword)//2]+codeword[len(codeword)//2+3:]+' '
        #If the codeword appears to not be encoded, the loop breaks and the codeword is declared as invalid.
        else:
            word="Invalid code word!"
            break
    #Removes white space from the end of the word/phrase and outputs the word/phrase.
    word=word[:-1]
    print(word)

encode()
decode()

