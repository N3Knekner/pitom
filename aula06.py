# class Pessoa():
#     def __init__(self, nome:str, idade:int, endereco:str):
#         self.nome = nome
#         self.idade = idade
#         self.endereco = endereco

#     def mostrar_endereco(self):
#         print(self.endereco)

#     def altera_endereco(self, novo_endereco:str):
#         self.endereco = novo_endereco


# p = Pessoa('a', 1, 'onde judas perdeu as botas')
# print(p.nome)
# print(p.idade)

# p.mostrar_endereco()

# p.altera_endereco('casa do c******')

# p.mostrar_endereco()


class Aluno():
    def __init__(self, matricula: int, nome: str, nota1: float, nota2: float, nota3: float):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def get_nome(self):
        return self.nome

    def get_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
    
    def __str__(self):
        return ''.join([str(self.matricula), ' - ', self.nome])


alunos = [Aluno(int(input('Matricula do aluno: ')), input('Nome: '), float(input(
    '1º nota: ')), float(input('2º nota: ')), float(input('3º nota: '))) for i in range(5)]

maior_media = 0
aluno_com_maior_media = None
for aluno in alunos:
    if maior_media < (m:=aluno.get_media()):
        maior_media = m
        aluno_com_maior_media = aluno

print('Aluno com maior media: ', aluno_com_maior_media)

menor_media = 10
aluno_com_menor_media = None
for aluno in alunos:
    if menor_media > (m:=aluno.get_media()):
        menor_media = m
        aluno_com_menor_media = aluno

print('Aluno com menor media: ', aluno_com_menor_media)

for aluno in alunos:
    print(f'Aluno {aluno} reprovado!' if aluno.get_media() < 7 else f'Aluno {aluno} aprovado!')
    
    # if aluno.get_media() < 7:
    #     print(f'Aluno {aluno} reprovado!')
    # else: print(f'Aluno {aluno} aprovado!')