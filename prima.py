n = int(input('Masukan banyak bilangan prima : '))

k=0
i=2

while(k<n):
    prima=True
    for j in range(2,i):
       if(i%j==0):
           prima=False
    if(prima):
        print(i,end=' ')
        k+=1
    i+=1