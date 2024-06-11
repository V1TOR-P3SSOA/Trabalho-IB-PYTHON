hora = int(input('Digite a hora: '))
if hora >= 0 and hora <12:
    print('Bom dia! já está de manhã.')
elif hora >=12 and hora <18:
    print('Boa tarde! já está de tarde')
else :
    print('Boa noite! já está de noite')