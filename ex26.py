salario = int(input('seu salario é de:'))
if salario <= 1250:
    salarioNovo = salario + (salario * 15 /100)
else:
    salarioNovo = salario + (salario * 10 /100)

print('seu novo salario é de R${:.2f}'.format(salarioNovo))