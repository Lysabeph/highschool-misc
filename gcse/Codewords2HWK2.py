#Encodes a word.
def encode():
    #Word is entered and any white space is removed.
    word=input("Enter a word you would like to encode: ").lower()
    word=word.replace(' ','')
    #If the word is even length, the word is encoded with 'egg'.
    if len(word)%2==0:
        codeword=word[:len(word)//2]+'egg'+word[len(word)//2:len(word)]
    #If the word is odd length, the word is encoded with 'ga'.
    else:
        codeword=word[:len(word)//2]+'ga'+word[len(word)//2]+'ga'+word[len(word)//2+1:]
    #Outputs the encoded word.
    print(codeword)

#Decodes a word.
def decode():
    #Codeword is entered and any white space is removed.
    codeword=input("Enter a word you would like to decode: ").lower()
    codeword=codeword.replace(' ','')
    #If the codeword has been encoded with 'egg', it is decoded appropriately.
    if codeword[len(codeword)//2-1:len(codeword)//2+2]=='egg':
        word=codeword[:len(codeword)//2-1]+codeword[len(codeword)//2+2:]
    #If the codeword has been encoded with 'ga', it is decoded appropriately.
    elif codeword[len(codeword)//2-2:len(codeword)//2]=='ga' and\
            codeword[len(codeword)//2+1:len(codeword)//2+3]=='ga':
            word=codeword[:len(codeword)//2-2]+codeword[len(codeword)//2]+codeword[len(codeword)//2+3:]
    #If the codeword appears to not be encoded, the codeword is declared as invalid.
    else:
        word="Invalid code word!"
    #Outputs the decoded word.
    print(word)

encode()
decode()

