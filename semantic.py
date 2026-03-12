def validar_nome_variavel(nome):

    palavras_reservadas = ['SET','ADD','SUB','MUL','DIV','PRINT']

    if not nome.isalpha():
        return False

    if nome in palavras_reservadas:
        return False

    return True


def validar_semantica(partes, numero_linha, tabela_simbolos):

    comando = partes[0]

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


    elif comando == 'PRINT':

        nome = partes[1]

        if nome not in tabela_simbolos:
            return False, f"Erro semântico na linha {numero_linha}: variável '{nome}' não declarada"


    else:

        op1 = partes[1]
        op2 = partes[2]

        for operando in [op1, op2]:

            if not operando.replace('.', '', 1).isdigit():

                if operando not in tabela_simbolos:
                    return False, f"Erro semântico na linha {numero_linha}: variável '{operando}' não declarada"

    return True, None