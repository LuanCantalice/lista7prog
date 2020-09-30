x = 1
i=0
soma=0

while(x>0):
    num = int(input("Digite o número: "))
    if(num%2==0 and num>0):
        soma+=num
        i+=1
    elif(num==0):
        x = 0
    else:
        pass


media = soma/i
print("Média:", media)
