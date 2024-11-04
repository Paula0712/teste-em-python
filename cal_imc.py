
peso = float(input("Por favor, digite o seu peso em kg: "))


altura = float(input("Por favor, digite a sua altura em metros: "))


imc = peso / (altura ** 2)


if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    classificacao = "Peso normal"
elif 25 <= imc < 29.9:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Seu IMC é: {imc:.2f}. Classificação: {classificacao}")

