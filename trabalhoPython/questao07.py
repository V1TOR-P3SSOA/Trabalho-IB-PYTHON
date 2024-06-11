nome = input('Informe seu nome: ')
mat = input('Informe a matéria: ')
n1 = int(input('Informe sua primeira nota: '))
n2 = int(input('Informe sua segunda nota: '))
m = (n1 + n2)/2
if m >= 6:
    print(f'{nome} está aprovado na disciplina {mat}')
else:
    print(f'{nome} está reprovado na disciplina {mat}')