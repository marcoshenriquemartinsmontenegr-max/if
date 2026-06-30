from datetime import date

def validar_idade(data_nascimento: date):
    hoje = date.today()

    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1

    if idade < 18:
        raise ValueError("Você é menor de 18 anos!")

    return data_nascimento