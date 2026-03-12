from lexer import lexer
from syntax_parser import validar_sintaxe
from semantic import validar_semantica
from translator import traduzir_para_python


def processar_arquivo(arquivo):

    tabela_simbolos = {}
    codigo_python = []

    with open(arquivo, 'r') as f:
        linhas = f.readlines()

    for i, linha in enumerate(linhas, start=1):

        if linha.strip() == "":
            continue

        # LEXER
        tokens = lexer(linha)

        # PARSER
        valido, erro = validar_sintaxe(linha, i)

        if not valido:
            print(erro)
            return

        partes = linha.strip().split()

        # SEMANTIC
        valido, erro = validar_semantica(partes, i, tabela_simbolos)

        if not valido:
            print(erro)
            return

        # TRANSLATOR
        codigo_python.append(traduzir_para_python(partes))

    with open("saida.py", "w") as f:
        for linha in codigo_python:
            f.write(linha + "\n")

    print("Compilação concluída!")


if __name__ == "__main__":

    arquivo = input("Arquivo de entrada: ")
    processar_arquivo(arquivo)