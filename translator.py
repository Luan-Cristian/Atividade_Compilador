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