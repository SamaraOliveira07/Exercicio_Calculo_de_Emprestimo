import time
valor = float(input('\033[1mValor da casa: '))
salario = float(input('\033[1mSalário do comprador: '))
anos = int(input('\033[1mPagamento em quantos anos: '))
meses = anos*12
valor_prestacao = valor / meses
print('\033[1mPor favor, aguarde...')
time.sleep(2)
print(f'\033[1mO valor da prestação mensal será de R${valor_prestacao:.2f}')
if (salario*0.3)+salario >= valor_prestacao:
    print('\033[1;32mEmpréstimo aprovado!')
else:
    print('\033[1;31mEmpréstimo reprovado!')
