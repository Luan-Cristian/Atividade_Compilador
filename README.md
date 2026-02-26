🧠 CalcLang 2.0 Compiler — Tradutor para Python
Projeto desenvolvido para a disciplina de Compiladores, com o objetivo de simular as principais fases de um compilador através da implementação de um mini compilador da linguagem fictícia CalcLang 2.0.

🎯 Objetivo
Estender um tradutor simples implementado anteriormente, adicionando:
✔ Tabela de Símbolos
✔ Análise Semântica
✔ Verificação de variáveis declaradas
✔ Separação entre análise sintática e semântica
✔ Geração de código Python equivalente

🏗 Arquitetura do Compilador
O sistema foi dividido em três etapas principais:

1️⃣ Análise Sintática
Validação estrutural das instruções da linguagem.

2️⃣ Análise Semântica
Verificação de:
Uso de variáveis não declaradas
Nome válido de identificadores
Correção semântica das instruções

3️⃣ Geração de Código
Tradução das instruções válidas para código Python.

📘 Linguagem CalcLang 2.0

🔹 Declaração de variável
SET nome numero

🔹 Operações aritméticas
ADD op1 op2
SUB op1 op2
MUL op1 op2
DIV op1 op2

🔹 Impressão
PRINT nome

📜 Regras
Variáveis devem ser declaradas antes do uso.
Nome da variável deve conter apenas letras.
Não pode usar palavras reservadas.
Operações não alteram variáveis.
PRINT aceita apenas variáveis declaradas.

📥 Exemplo de Entrada
SET a 10
SET b 5
ADD a b
PRINT a

📤 Saída Gerada
a = 10
b = 5
print(a + b)
print(a)

❌ Exemplo de Erro
ADD a 10
Saída:
Erro semântico na linha 1: variável 'a' não declarada

🚀 Execução
python compilador.py

📚 Conceitos Aplicados
Análise Sintática
Análise Semântica
Tabela de Símbolos
Tratamento de Erros
Geração de Código