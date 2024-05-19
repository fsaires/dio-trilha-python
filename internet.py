def recomendar_plano(consumo):
  plano = ""
  # Solicita ao usuário que insira o consumo médio mensal de dados:
  if consumo <= 10:
    plano = "Plano Essencial Fibra - 50Mbps"
  elif consumo > 11 and consumo <= 20:
    plano =  "Plano Prata Fibra - 100Mbps"
  elif consumo > 20:
    plano = "Plano Premium Fibra - 300Mbps"
    
  return plano


def main():
  consumo = float(input("Informe o consumo médio mensal de dados em GB: "))
  # Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
  recomendado = recomendar_plano(consumo)
  print(recomendado)


if __name__ == "__main__":
  main()