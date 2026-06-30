def validar_senha(senha):
    if len(senha) < 8:
        raise ValueError("mínimo 8 caracteres")

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    for letra in senha:
        if letra.isupper():
            tem_maiuscula = True
        if letra.islower():
            tem_minuscula = True
        if letra.isdigit():
            tem_numero = True
        if not letra.isalpha() and not letra.isdigit():
            tem_especial = True

    if not tem_maiuscula:
        raise ValueError("precisa maiúscula")
    if not tem_minuscula:
        raise ValueError("precisa minúscula")
    if not tem_numero:
        raise ValueError("precisa número")
    if not tem_especial:
        raise ValueError("precisa caractere especial")

    return senha