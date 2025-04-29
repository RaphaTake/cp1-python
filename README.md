
# 📚 Sistema de Cadastro de Alunos com Estatísticas

Este projeto em Python permite o cadastro de alunos, incluindo nome, idade e três notas. Com base nesses dados, o sistema calcula a média das notas, exibe todos os alunos cadastrados e gera estatísticas como a média das idades, o aluno com a maior média e a quantidade de aprovados.

## 👨‍👩‍👧‍👦 Participantes
- Felipe Andrade
- Raphael Taketa
- Guilherme Augusto
- Victor Guimarães

## 🧾 Descrição do Projeto

O sistema conta com um menu interativo que permite:
- Adicionar novos alunos.
- Listar os alunos cadastrados com suas respectivas médias.
- Ver estatísticas sobre o grupo de alunos.
- Encerrar o programa.

### 📋 Funcionalidades
- Entrada de dados via terminal.
- Armazenamento de informações em uma lista de dicionários.
- Cálculo da média de notas por aluno.
- Estatísticas gerais do grupo de alunos.

### 📌 Critérios de Aprovação
- Alunos com média **maior ou igual a 7** são considerados aprovados.

## 🛠️ Como Utilizar

1. Use o menu para interagir com o sistema:
```
   📓 MENU
   1 - Adicionar aluno
   2 - Listar alunos
   3 - Ver Estatísticas
   4 - Sair do Programa
   ```

## 💻 Exemplo de Uso

```bash
Digite o nome: João
Digite a idade: 17
Digite a 1 nota: 8
Digite a 2 nota: 7
Digite a 3 nota: 9
Aluno João cadastrado!

Deseja cadastrar outro aluno? s/n
s

...

📓 MENU
1 - Adicionar aluno
2 - Listar alunos
3 - Ver Estatísticas
4 - Sair do Programa
```

## 📊 Estatísticas

Exemplo de saída ao escolher a opção 3 (Ver Estatísticas):

```
Estatísticas:
Média de idades: 16.5
Aluno com maior média foi o João, com uma média de 8.00
Quantidade de alunos aprovados: 2
```

# 🧠 Explicação das Funções do Código de Cadastro de Alunos

Funcionalidade de cada parte do código Python utilizado para cadastrar alunos, calcular médias e gerar estatísticas.

---

## 📌 Lista Global

```python
alunos = []
```

- **alunos**: Lista principal onde os dados dos alunos serão armazenados. Cada aluno é representado como um dicionário contendo nome, idade, notas e média.

---

## 🔧 Função `adicionar_aluno()`

```python
def adicionar_aluno():
```

Essa função realiza o cadastro de um ou mais alunos:
- Solicita **nome**, **idade** e **3 notas**.
- Calcula a **média** das notas.
- Armazena os dados em um dicionário.
- Adiciona o aluno à lista `alunos`.

### Destaques:
- Usa `input()` para entrada de dados.
- Calcula média com: `sum(notas) / len(notas)`.
- Utiliza um `while True` para permitir múltiplos cadastros.

---

## 📋 Função `listar_alunos()`

```python
def listar_alunos():
```

Essa função exibe os dados de todos os alunos cadastrados:
- Mostra nome, idade, notas e média.
- Verifica se a lista está vazia antes de exibir.

### Destaques:
- Usa um laço `for` para percorrer a lista de alunos.

---

## 📊 Função `estatisticas()`

```python
def estatisticas():
```

Esta função mostra estatísticas gerais sobre os alunos:
- Calcula a **média das idades**.
- Encontra o **aluno com maior média**.
- Conta quantos **alunos foram aprovados** (média ≥ 7).

### Destaques:
- Usa compreensão de listas com `sum()` e `max()`.
- Utiliza laço `for` para contar os aprovados.

---

## 🧭 Função `menu()`

```python
def menu():
```

É a função principal que exibe o menu do programa:
- Apresenta 4 opções:
  1. Adicionar aluno
  2. Listar alunos
  3. Ver estatísticas
  4. Sair do programa
- Utiliza `match-case` para controlar o fluxo.
- Executa em loop até o usuário escolher sair.

---

## ▶️ Execução Final

```python
menu()
```

- Inicia o programa chamando a função `menu()`.

## ⚠️ Observações

- O sistema não salva os dados após encerrar a execução.
- Pode ser estendido para usar arquivos ou banco de dados futuramente.

## 📌 Tecnologias Utilizadas
- Python
