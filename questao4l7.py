salj = int(input("Salário de Jorge: "))
sals = salj/3
mes = 1
rendaj = (salj*1.02)+salj
rendas = (sals*1.05)+sals

while(rendas<=rendaj):
    mes+=1
    rendas = (rendas*1.05)+rendas
    rendaj = (rendaj*1.02)+rendaj

print("%i Meses necessários" %mes)
