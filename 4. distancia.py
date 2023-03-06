# Distância entre Ribeirão Preto e Franca

distancia_total = 100


# Velocidade do carro (km/h)

velocidade_carro = 110


# Velocidade do caminhão (km/h)

velocidade_caminhao = 80


# Tempo que o caminhão leva a mais nos pedágios (em horas)

tempo_pedagios = 0.0833


# Distância que o carro percorreu até o ponto de encontro

distancia_carro = distancia_total/2


# Distância que o caminhão percorreu até o ponto de encontro

distancia_caminhao = distancia_total/2 - (velocidade_caminhao * tempo_pedagios)


# Se a distância percorrida pelo carro for menor, ele estará mais próximo de Ribeirão Preto

if distancia_carro < distancia_caminhao:
    print("O carro estará mais próximo de Ribeirão Preto.")
else:
    print("O caminhão estará mais próximo de Ribeirão Preto.")