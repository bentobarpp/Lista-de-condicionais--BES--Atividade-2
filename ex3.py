temperatura = int(input("Quantos graus esta marcando na sua cidade?:  "))
if temperatura <= 15:
    print("está frio !!")
elif temperatura >= 25:
    print ("Está calor !")
elif temperatura <= 24 and temperatura >= 16:
    print ("temperatura agradável !")