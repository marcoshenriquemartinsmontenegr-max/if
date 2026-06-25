def validar_senha(senha):
    if len(senha) < 8:
        print("mínimo 8 caracteres!")
        return False

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
        print("Pelo menos uma maiuscula")
    if not tem_minuscula:
        print("Pelo menos uma minuscula")
    if not tem_numero:
        print("Pelo menos um numero")
    if not tem_especial:
        print("Pelo menos um caracter especial")
    else:
        print("Logando")