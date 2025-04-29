
alunos = []

def adicionar_aluno():
  while True:
    aluno = {}

    aluno['Nome']= input('Digite o nome: ')
    aluno ['idade'] = int(input('Digite a idade: '))

    notas = []
    for i in range (1,4):
        nota = float(input('digite a {} nota: '.format(i)))
        notas.append(nota)

    aluno['Notas'] = notas
    aluno['Média'] = sum(notas) / len(notas)

    alunos.append(aluno)
    print(f"Aluno {aluno['Nome']} cadastrado!\n")
    continuar = input("Deseja cadastrar outro aluno? s/n \n")

    if continuar != "s":
      break

def listar_alunos():
    if not alunos:
      print("Nenhum aluno foi cadastrado!")
      return

    print('\n Alunos Cadastrados:')
    for aluno in alunos:
      print(f"Nome: {aluno['Nome']}\n Idade:{aluno['idade']}\n Notas:{aluno['Notas']} \n Média:{aluno['Média']}\n")

def estatisticas():
  if not alunos:
    print("Nenhum aluno foi cadastrado!")
    return

  total_idade = sum(aluno['idade'] for aluno in alunos)
  media_idade = total_idade / len(alunos)

  maior_media = max(aluno['Média'] for aluno in alunos)
  nome_maior_media = [aluno['Nome'] for aluno in alunos if aluno['Média'] == maior_media][0]

  aprovados = 0

  for aluno in alunos:

    if aluno['Média'] >= 7:
      aprovados+=1


  print('\n Estatísticas:')
  print(f"Média de idades: {media_idade}")
  print(f"Aluno com maior média foi o {nome_maior_media}, com uma média de {maior_media:.2f}")
  print(f"Quantidade de alunos aprovados: {aprovados}\n")

def menu():

  while True:
    print("📓 MENU")
    print("1 - Adicionar aluno")
    print("2 - Listar alunos")
    print("3 - Ver Estatísticas")
    print("4 - Sair do Programa")

    decisão = input(" Escolha uma das opções: \n")

    match decisão:
      case "1":
        adicionar_aluno()

      case "2":
        listar_alunos()

      case "3":
        estatisticas()

      case "4":
        print("Programa Finalizado")

        break

      case _:
        print("Escolha uma opção\n")


menu()