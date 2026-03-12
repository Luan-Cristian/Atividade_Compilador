def validar_sintaxe(linha, numero_linha):

    partes = linha.strip().split()

    if not partes:
        return False, f"Erro sintático na linha {numero_linha}"

    comando = partes[0]

    comandos_validos = ['SET', 'ADD', 'SUB', 'MUL', 'DIV', 'PRINT']

    if comando not in comandos_validos:
        return False, f"Erro sintático na linha {numero_linha}"

    if comando == 'SET':
        if len(partes) != 3:
            return False, f"Erro sintático na linha {numero_linha}"

    elif comando == 'PRINT':
        if len(partes) != 2:
            return False, f"Erro sintático na linha {numero_linha}"

    else:
        if len(partes) != 3:
            return False, f"Erro sintático na linha {numero_linha}"

    return True, None