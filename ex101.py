from datetime import date


def voto():
    if idade < 16:
        print('VOTO NEGADO.')
    elif 16 <= idade < 18 or idade > 65:
        print('VOTO OPCIONAL.')
    else:
        print('VOTO OBRIGATÓRIO.')


print('---'*10)
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
print(f'Com {idade} anos: ', end='')
voto()