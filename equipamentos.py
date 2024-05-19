def adicionar_equipamentos(equipamento, lista_equipamentos):
    lista_equipamentos.append(equipamento)
    return lista_equipamentos

def imprimir_equipamentos(itens):
    print("Lista de Equipamentos:")  
    for item in itens:
        print(f"- {item}")

def main():
    lista_equipamentos = []

    contador = 1 
    while contador <=3:
        eqp = input("Informe um equipamento: ")
        lista = adicionar_equipamentos(eqp, lista_equipamentos)        
        contador += 1

    imprimir_equipamentos(lista)

if __name__ == "__main__":
  main()