def encontrar_aluno_com_maior_nota(alunos):
    maior_nota = 0
    aluno_maior_nota = None
    for aluno in alunos:
        if aluno["nota"] > maior_nota:
            maior_nota = aluno["nota"]
            aluno_maior_nota = aluno["nome"]
    return aluno_maior_nota

alunos = [
    {"nome": "João", "nota": 7.5},
    {"nome": "Maria", "nota": 8.2},
    {"nome": "Pedro", "nota": 9.0},
    {"nome": "Ana", "nota": 8.7}
]
resultado = encontrar_aluno_com_maior_nota(alunos)
print(resultado)