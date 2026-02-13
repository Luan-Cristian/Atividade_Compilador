def validar_linha(linha, numero_linha):
    """
    Valida uma linha de código CalcLang.
    Retorna (True, None) se válida ou (False, mensagem_erro) se inválida.
    """
    partes = linha.strip().split()
    
    # Verifica se tem exatamente 3 elementos
    if len(partes) != 3:
        return False, f"Erro na linha {numero_linha}"
    
    operacao, num1, num2 = partes
    
    # Verifica se a operação é válida
    operacoes_validas = ['ADD', 'SUB', 'MUL', 'DIV']
    if operacao not in operacoes_validas:
        return False, f"Erro na linha {numero_linha}"
    
    # Verifica se os dois últimos elementos são números
    try:
        float(num1)
        float(num2)
    except ValueError:
        return False, f"Erro na linha {numero_linha}"
    
    return True, None


def traduzir_para_python(linha):
    """
    Traduz uma linha de CalcLang para Python.
    """
    partes = linha.strip().split()
    operacao, num1, num2 = partes
    
    mapeamento_operacoes = {
        'ADD': '+',
        'SUB': '-',
        'MUL': '*',
        'DIV': '/'
    }
    
    operador = mapeamento_operacoes[operacao]
    return f"print({num1} {operador} {num2})"


def processar_arquivo(arquivo_entrada):
    """
    Processa o arquivo de entrada em CalcLang e gera o arquivo de saída em Python.
    """
    try:
        # Lê o arquivo de entrada
        with open(arquivo_entrada, 'r', encoding='utf-8') as f:
            linhas = f.readlines()
        
        # Lista para armazenar as linhas traduzidas
        linhas_python = []
        erro_encontrado = False
        
        # Processa cada linha
        for i, linha in enumerate(linhas, start=1):
            # Ignora linhas vazias
            if linha.strip() == '':
                continue
            
            # Valida a linha
            valido, mensagem_erro = validar_linha(linha, i)
            
            if not valido:
                print(mensagem_erro)
                erro_encontrado = True
                break
            
            # Traduz a linha para Python
            linha_python = traduzir_para_python(linha)
            linhas_python.append(linha_python)
        
        # Se não houve erros, gera o arquivo de saída
        if not erro_encontrado:
            arquivo_saida = arquivo_entrada.replace('.txt', '_output.py')
            with open(arquivo_saida, 'w', encoding='utf-8') as f:
                for linha in linhas_python:
                    f.write(linha + '\n')
            
            print(f"Tradução concluída! Arquivo gerado: {arquivo_saida}")
            return arquivo_saida
        
        return None
    
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
        return None


def main():
    """
    Função principal do tradutor.
    """
    print("=== Tradutor CalcLang para Python ===\n")
    
    # Solicita o nome do arquivo de entrada
    arquivo_entrada = input("Digite o nome do arquivo de entrada (ex: input.txt): ")
    
    # Processa o arquivo
    arquivo_saida = processar_arquivo(arquivo_entrada)
    
    if arquivo_saida:
        print("\n--- Conteúdo do arquivo gerado ---")
        with open(arquivo_saida, 'r', encoding='utf-8') as f:
            print(f.read())


if __name__ == "__main__":
    main()