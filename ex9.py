idade = int(input("Informe sua idade: "))
tempoServico =int(input("Informe o tempo de servico em anos: "))
if idade >= 65:
    print("Pode se aposentar!")
elif tempoServico >= 30:
    print("Pode se aposentar!")
elif idade >= 60 and tempoServico >=25:
    print("Pode se aposentar!")
else:
    print("Nao pode se aposentar!")