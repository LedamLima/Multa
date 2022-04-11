# PROGRAMA QUE LER A VELOCIDADE DE UM CARRO
# SE PASSAR DE 80KM/H CUSTA r$7,00
velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade-80) *7
    print('Voce deve pagar uma MULTA de  {:.2f}'.format(multa))
print('Tenha Um Bom Dia! Com Dirija Com Segurança')
