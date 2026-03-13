# CalcLang 2.0 Compiler — Tradutor para Python

Projeto desenvolvido para a disciplina de **Compiladores**, com o objetivo de simular as principais fases de um compilador através da implementação de um mini compilador da linguagem fictícia **CalcLang 2.0**.

---

# Objetivo

Este projeto estende um tradutor simples implementado anteriormente, adicionando novas fases típicas de compiladores:

✔ Análise Léxica (Lexer)  
✔ Análise Sintática (Parser)  
✔ Análise Semântica  
✔ Tabela de Símbolos  
✔ Verificação de variáveis declaradas  
✔ Geração de código Python equivalente  

---

# Arquitetura do Compilador

O compilador foi organizado em **quatro fases principais**:

## 1️⃣ Análise Léxica (Lexer)

Responsável por dividir cada linha do programa em **tokens**, identificando comandos, variáveis e valores.

---

## 2️⃣ Análise Sintática (Parser)

Verifica se a estrutura das instruções segue as regras da linguagem.

Exemplo de verificação:

- comando válido  
- quantidade correta de argumentos

---

## 3️⃣ Análise Semântica

Realiza verificações de significado do programa:

- uso de **variáveis não declaradas**
- **nomes válidos de variáveis**
- verificação de **valores numéricos**
- controle através de uma **tabela de símbolos**

---

## 4️⃣ Geração de Código

As instruções válidas da linguagem **CalcLang** são traduzidas para **código Python equivalente**.

---

# Estrutura do Projeto
calc_compiler/
lexer.py
parser.py
semantic.py
translator.py
main.py
entrada.calc
erro.calc
saida.py
README.md


### Arquivos principais

**lexer.py**  
Responsável pela análise léxica.

**parser.py**  
Realiza a validação sintática das instruções.

**semantic.py**  
Executa a análise semântica e mantém a **tabela de símbolos**.

**translator.py**  
Traduz as instruções para código Python.

**main.py**  
Controla o fluxo do compilador e executa todas as fases.

---

# Linguagem CalcLang 2.0

## Declaração de variável
SET nome numero

Exemplo:
SET a 10

---

## Operações aritméticas
ADD op1 op2
SUB op1 op2
MUL op1 op2
DIV op1 op2

---

## Impressão
PRINT nome

---

# Regras da Linguagem

- Variáveis devem ser **declaradas antes do uso**
- Nome da variável deve conter **apenas letras**
- Não pode usar **palavras reservadas**
- Operações **não alteram variáveis**
- `PRINT` aceita apenas **variáveis declaradas**

---

# Exemplo de Programa Válido

### Entrada (`entrada.calc`)
SET a 10
SET b 5
ADD a b
PRINT a

### Código Python Gerado (`saida.py`)

```python
a = 10
b = 5
print(a + b)
print(a)

Exemplo de Erro Semântico
Entrada (erro.calc)
ADD a 10

Saída
Erro semântico na linha 1: variável 'a' não declarada

Execução

Executar o compilador:
python main.py
Depois informar o arquivo de entrada:
Arquivo de entrada: entrada.calc

Se não houver erros, será gerado:
saida.py

Conceitos de Compiladores Aplicados

Análise Léxica
Análise Sintática
Análise Semântica
Tabela de Símbolos
Tratamento de Erros
Geração de Código