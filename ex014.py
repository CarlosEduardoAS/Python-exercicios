c = float(input('Informe a temperatura em °C: '))
f = c * 9/5 + 32
k = c + 273.15
print('A temperatura de \033[1;4;30m{}°C\033[m corresponde a \033[1;33m{}°F\033[m e \033[1;34m{}K\033[m.'.format(c, f, k))