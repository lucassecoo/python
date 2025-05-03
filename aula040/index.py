from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def Emprestimo():
    try:
        valorEmprestimo = float(input('Digite o valor do emprestimo: '))
        parcelas = int(input('Digite a quantidade de parcelas: '))
        carencia = int(input('Digite quantos dias de carencia: '))
        data_atual = datetime.now()
        data_com_carencia = data_atual + timedelta(days=carencia)

        print(f'Valor do empréstimo: R${valorEmprestimo}\nParcelas: {parcelas}\nCarencia: {carencia} dias')
        for i in range(parcelas):
            data_parcela = data_com_carencia + relativedelta(months=i)
            print(f'Parcela {i + 1}: {data_parcela.strftime("%d/%m/%Y")}')

    except ValueError:
        print('Digite um numero!')

Emprestimo()