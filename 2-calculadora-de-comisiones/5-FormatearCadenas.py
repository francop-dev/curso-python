#cuando ingresas varios datos, puede resultar engorroso poner todos esos datos y formarlos en un string completo, por eso existe el format

#ejemplo format

color_auto = 'gris'
matricula = 'AAA123'

print('mi auto es {} y matricula {}'.format(color_auto,matricula))


#pero esa forma es bastante dificil de leer asi que tenemos las cadenas literales, que son mucho mas faciles de leer

print(f'mi auto es {color_auto} y la matricula es {matricula}')

#tambien podemos hacer operaciones

y = 12
x = 27

print(f'la suma entre {y} y {x} es igual a {y+x}')