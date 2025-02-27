perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def perguntar():
    for index, questions in enumerate(perguntas):
        print(f'{questions['Pergunta']}\n')
        print('Opções:')
        for i, options in enumerate(questions['Opções']):
            print(f'{i}) {options}')
            
        resposta_user = input('Digite a resposta: ')
        while resposta_user != questions['Resposta']:
            print('Resposta errada, tente novamente!')
            resposta_user = input('Digite a resposta: ')
          
        print('Resposta certa!\n')

    



perguntar()