curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
totalcreditos = 0
for asignatura, credito in curso.items():
    print(asignatura, 'tiene', credito, 'créditos')
    totalcreditos += credito
print('Número total de créditos del curso: ', totalcreditos)
