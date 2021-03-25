from datetime import date
g = input('Digite seu gênero (Masculino ou Feminino): ').lower()
if g == 'masculino':
    d = int(input('Digite o ano de seu nascimento: '))
    i = (date.today().year) - d
    tf = abs(18 - i)
    if i < 18:
        print('Daqui a {} ano(s), em {}, você terá que se alistar.'.format(tf, (date.today().year + tf)))
    elif i == 18:
        print('Já está na hora de se alistar.')
    else:
        print('Já se passaram {} ano(s) desde seu alistamento obrigatório, que ocorreu em {}.'.format(tf, (date.today().year - tf)))
else:
    print('O alistamento militar não é obrigatório para você.')