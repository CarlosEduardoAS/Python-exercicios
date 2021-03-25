from datetime import date
print('\033[1;30m-=-'*17)
print('\033[1;34mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m\nDescubra a sua categoria de acordo com a sua idade')
print('\033[1;30m-=-\033[m'*17)
ano = int(input('Digite o ano de seu nascimento: '))
i = (date.today().year) - ano
if i <= 9:
    print('Sua categoria é \033[1;30mMIRIM\033[m.')
elif 9 < i <= 14:
    print('Sua categoria é \033[1;30mINFANTIL\033[m.')
elif 14 < i <= 19:
    print('Sua categoria é \033[1;30mJUNIOR\033[m.')
elif 19 < i <= 20:
    print('Sua categoria é \033[1;30mSÊNIOR\033[m.')
else:
    print('Sua categoria é \033[1;30mMASTER\033[m.')