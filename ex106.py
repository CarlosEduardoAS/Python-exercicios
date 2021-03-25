from time import sleep
while True:
    txt = '  SISTEMA DE AJUDA PyHELP'
    tam = len(txt) + 4
    print('\033[1;30;42m~' * tam)
    print(txt)
    print('~' * tam)
    func = str(input('\033[mFunção ou Biblioteca > ')).strip().lower()
    if func == 'fim':
        txt = '  ATÉ LOGO!'
        tam = len(txt) + 4
        print('\033[1;30;41m~' * tam)
        print(txt)
        print('~' * tam)
        break
    txt = f"  Acessando o manual do comando '{func}'"
    tam = len(txt) + 4
    print('\033[1;30;44m~' * tam)
    print(txt)
    print('~' * tam)
    print('\033[1;7;30m')
    sleep(1)
    help(func)