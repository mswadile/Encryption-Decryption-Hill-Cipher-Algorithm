import numpy as np
a=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
c=[[0,0,0,0,0,0,0,0,0,0],
   [0,0,0,0,0,0,0,0,0,0]]
ecm=[[2,1],
     [1,1]]
i=0
l=0

#=========================Lists of Alphabets and its values=========
smallalpha=[" ","a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
capitalalpha=[" ","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphavalues=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#specialchar=["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "\", "|", "}", "{", "[", "]", ";", ":", "'", """, "<", ">", ",", ".", "?", "/"]
#specialvalues=[27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57]
#================================================================

b=input("Enter word to Encrypt(max - 18 char)=")
listb=list(b)
lenb=len(listb)

#----Loop to convert Word to Values that are further useful for Encoding
for i in range(lenb):
    for j in range(27):
        if(listb[i]==smallalpha[j]):
            a[i]=alphavalues[j]
            if(j==23):
                j=0
            break
        if(j==23):
            for k in range(27):
                if(listb[i]==capitalalpha[k]):
                    a[i]=alphavalues[k]
                    break
#----------------------------------------------------------------------
                    
                
if(lenb%2==1):
    lenb=lenb+1
a=a[0:lenb]
tb=b


#convert this array to 2D array for further multiplication with encoding matrix
j=0
k=0
#b[m][n] m is always 2
n=int(lenb/2)
for i in range(0,lenb):
    if(j<n):
        c[k][j]=a[i]
        j=j+1
    else:
        k=k+1
        j=0
        c[k][j]=a[i]
        j=j+1
#------------------------------------------------------------------------------
        
        
#Multiplay matrix by Encoding 2x2 matrix------------
c=np.matmul(ecm,c)
#---------------------------------------------------

#Mod of 28
for i in range(0,2):
    for j in range(0,10):
        c[i][j]%=28


#Convert to 1D array for displaying-----------------
i=0
j=0
k=0
for i in range(2):
    for j  in range(int(lenb/2)):
        a[k]=c[i][j]
        k=k+1
#---------------------------------------------------

       
a=a[0:lenb]

lista=list(a)
text=""
for i in range(0,len(lista)):
    for j in range(0,27):
        if(lista[i]==alphavalues[j]):
            text=''.join([text,smallalpha[j]])
print("Encoding matrix = ",ecm)
print("encrypted form= ",text)
