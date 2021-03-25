from datetime import date
perfil = {}
perfil['nome'] = str(input('Nome: ')).strip().capitalize()
ano = int(input('Ano de Nascimento: '))
perfil['idade'] = date.today().year - ano
perfil['ctps'] = int(input('Carteira de Trabalho: (0 não tem) '))
if perfil['ctps'] == 0:
    print('-='*30)
    print(perfil)
    for k, v in perfil.items():
        print(f'{k} tem o valor de {v}')
else:
    perfil['contratação'] = int(input('Ano de contratação: '))
    perfil['salário'] = float(input('Salário: R$'))
    perfil['aposentadoria'] = (perfil['contratação'] + 35) - ano
    print('-='*30)
    print(perfil)
    for k, v in perfil.items():
        print(f'{k} tem o valor de {v}')