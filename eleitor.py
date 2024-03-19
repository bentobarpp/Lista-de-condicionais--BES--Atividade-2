idade = int(input("Informe sua Idade: "))
if idade <= 16:
    print("Voce nao e leitor")
elif idade >= 18 and idade <= 65:
    print("Voce e eleitor obrigatorio! ")
elif idade == 17 and idade >=66:
    print("Voce e eleitor facultativo! ")


