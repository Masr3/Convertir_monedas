#convertir de pesos a euros, pesos colombianos y dolares

pesos = int(input("Coloque la cantidad de pesos que desea convertir"))

moneda = int(input("Escriba  1 si desea convertirlo en pesos colombianos\nEscriba 2 si desea convertirlo en euros" 
               "\n""Escriba 3 si desea convertirlo en dolares\n"))

if moneda == 1:
    print(f"En pesos colombianos {pesos} peso/s dominicano/s equivale a  {pesos/67.93} pesos colombianos")
elif moneda == 2 and pesos <59.58:
    print(f"En euros {pesos} peso/s dominicano/s equivale a {pesos * 0.017} centavos de  euro")
elif moneda ==2 and pesos >= 59.58:
    print("En euros", pesos, "peso/s dominicano/s equivale a", round(pesos/59.53,2), "euros")
elif moneda == 3 and pesos<55:
    print(f"En euros {pesos} peso/s dominicano/s equivale a {pesos * 0.018} centavos de dolar")
elif moneda==3 and pesos>= 55:
    print("En euros", pesos, "peso/s dominicano/s equivale a",round(pesos/55,2), "dolares")

