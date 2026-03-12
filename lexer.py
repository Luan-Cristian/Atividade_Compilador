class Token:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor

    def __repr__(self):
        return f"[{self.tipo}:{self.valor}]"


def is_number(value):
    try:
        float(value)
        return True
    except:
        return False


def lexer(linha):
    tokens = []

    palavras_reservadas = ["SET", "ADD", "SUB", "MUL", "DIV", "PRINT"]

    partes = linha.strip().split()

    for parte in partes:

        if parte in palavras_reservadas:
            tokens.append(Token("COMMAND", parte))

        elif is_number(parte):
            tokens.append(Token("NUMBER", parte))

        else:
            tokens.append(Token("IDENTIFIER", parte))

    return tokens