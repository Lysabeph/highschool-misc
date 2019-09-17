def encode():
    codeword=''
    word=input("Please enter a word you would like to encode: ").lower()
    word.replace(' ','')
    if len(word)%2==1:
        for i in range(0,len(word)//2):
            codeword+=word[i]
        for ii in ['g','a',word[i+1],'g','a']:
            codeword+=ii
        for iii in range(len(word)//2+1,len(word)):
            codeword+=word[iii]
    else:
        for i in range(0, len(word)//2):
            codeword+=word[i]
        codeword+='egg'
        for ii in range(len(word)//2,len(word)):
            codeword+=word[ii]
    print(codeword)

def decode():
    word=''
    codeword=input("Please enter a word you would like to decode: ").lower()
    codeword.replace(' ','')
    if codeword[len(codeword)//2]