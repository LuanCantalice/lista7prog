op = str(input("Deseja qual tabuada? (1) para adição (2) para multiplicação: \n"))

if(op=="1"):
    num = int(input("Qual número você quer ver a tabuada? (1-10) "))
    i=1
    while(i<=10):
        print(num," + ", i, " = ", num+i)
        i+=1
elif(op=="2"):
    num = int(input("Qual número você quer ver a tabuada? (1-10) "))
    i=1
    while(i<=10):
        print(num," X ", i, " = ", num*i)
        i+=1
else:
    print("Digite uma opção válida.")
