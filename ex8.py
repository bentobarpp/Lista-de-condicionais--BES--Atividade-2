idade = int(input("Informe sua idade: "))
if idade < 16:
    print("Nao e eleitor!")
elif idade >= 16 and idade <=18 or idade > 65:
    print("Facultativo!")
elif idade >= 18 or idade <= 65:
    print("Eleitor obrigatorio!")

