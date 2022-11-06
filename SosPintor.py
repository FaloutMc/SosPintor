from math import ceil
litro=float(input('Quantos litros sua caixa de tinta tem? ' ))
area=float(input('A sua caixa de tinta pinta quantos m²? '))
real=float(input('Quanto custa a sua caixa de tinta? R$'))
l=float(input('Qual é a largura da sua parede/casa? '))
h=float(input('Qual é a altura da sua parede/casa? '))
a=l*h
lt=a/area
c=lt/litro
p=c.__ceil__()*real
print(f'A sua área é de {ceil(a):.0f} m², voce precisará de {ceil(lt):.0f}')
print(f'litros de tinta, e te custará {p:.2f}R$,')
print(f'e você precisara de {ceil(c)} Caixas de tinta.')
