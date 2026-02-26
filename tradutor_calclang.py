def validar_sintaxe(linha, numero_linha):
    partes = linha.strip().split()

    if not partes:
        return False, f"Erro sintático na linha {numero_linha}"

    comando = partes[0]

    comandos_validos = ['SET', 'ADD', 'SUB', 'MUL', 'DIV', 'PRINT']

    if comando not in comandos_validos:
        return False, f"Erro sintático na linha {numero_linha}"

    # SET nome numero
    if comando == 'SET':
        if len(partes) != 3:
            return False, f"Erro sintático na linha {numero_linha}"

    # PRINT nome
    elif comando == 'PRINT':
        if len(partes) != 2:
            return False, f"Erro sintático na linha {numero_linha}"

    # Operações aritméticas
    else:
        if len(partes) != 3:
            return False, f"Erro sintático na linha {numero_linha}"

    return True, None


def validar_nome_variavel(nome):
    palavras_reservadas = ['SET', 'ADD', 'SUB', 'MUL', 'DIV', 'PRINT']

    if not nome.isalpha():
        return False

    if nome in palavras_reservadas:
        return False

    return True


def validar_semantica(partes, numero_linha, tabela_simbolos):
    comando = partes[0]

    # SET nome numero
    if comando == 'SET':
        nome = partes[1]
        valor = partes[2]

        if not validar_nome_variavel(nome):
            return False, f"Erro semântico na linha {numero_linha}: nome de variável inválido"

        try:
            float(valor)
        except ValueError:
            return False, f"Erro semântico na linha {numero_linha}: valor inválido"

        tabela_simbolos[nome] = valor

    # PRINT nome
    elif comando == 'PRINT':
        nome = partes[1]

        if nome not in tabela_simbolos:
            return False, f"Erro semântico na linha {numero_linha}: variável '{nome}' não declarada"

    # Operações
    else:
        op1 = partes[1]
        op2 = partes[2]

        for operando in [op1, op2]:
            if not operando.replace('.', '', 1).isdigit():
                if operando not in tabela_simbolos:
                    return False, f"Erro semântico na linha {numero_linha}: variável '{operando}' não declarada"

    return True, None


def traduzir_para_python(partes):
    comando = partes[0]

    if comando == 'SET':
        return f"{partes[1]} = {partes[2]}"

    elif comando == 'PRINT':
        return f"print({partes[1]})"

    else:
        mapeamento = {
            'ADD': '+',
            'SUB': '-',
            'MUL': '*',
            'DIV': '/'
        }

        operador = mapeamento[comando]
        return f"print({partes[1]} {operador} {partes[2]})"


def processar_arquivo(arquivo_entrada):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        tabela_simbolos = {}
        linhas_python = []

        for i, linha in enumerate(linhas, start=1):
            if linha.strip() == '':
                continue

            valido_sintaxe, erro = validar_sintaxe(linha, i)
            if not valido_sintaxe:
                print(erro)
                return None

            partes = linha.strip().split()

            valido_semantica, erro = validar_semantica(partes, i, tabela_simbolos)
            if not valido_semantica:
                print(erro)
                return None

            linha_python = traduzir_para_python(partes)
            linhas_python.append(linha_python)

        arquivo_saida = arquivo_entrada.replace('.txt', '_output.py')

        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            for linha in linhas_python:
                f.write(linha + '\n')

        print(f"Tradução concluída! Arquivo gerado: {arquivo_saida}")
        return arquivo_saida

    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
        return None

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return None


def main():
    print("=== Compilador CalcLang 2.0 ===\n")

    arquivo = input("Digite o nome do arquivo de entrada: ")

    resultado = processar_arquivo(arquivo)

    if resultado:
        print("\n--- Código Python Gerado ---")
        with open(resultado, 'r', encoding='utf-8') as f:
            print(f.read())


if __name__ == "__main__":
    main()