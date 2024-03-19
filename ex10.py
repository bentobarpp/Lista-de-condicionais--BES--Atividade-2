
faculdade = input("qual a sua faculdade? \n 1 - PUCPR \n 2 - UNICAMP\n")
if faculdade == '1':
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = (nota1 + nota2)/2
    if faculdade == 'pucpr':
        print("Voce esta na pucpr")
        if media >= 7:
            print("Aprovado!")
        elif media >= 4 and media <= 7:
            print("Recuperacao!")
        else:
            print("Reprovado!")
elif faculdade == '2':
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    media = (nota1 + nota2)/2
    print("Voce esta na Unicamp!")
    if media >= 5 and media <=10:
        print("Aprovado!")
    else:
        print("Recuperacao Final!") 
else:
    print("Sua faculdade nao e nem pucpr nem unicamp!")