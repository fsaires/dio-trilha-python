class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."
    
def main():
    # Entrada:
    nome = input("Digite o nome: ")  
    numero = input("Digite o número: ")  
    plano = input("Digite o plano: ")  

    usuario = UsuarioTelefone(nome, numero, plano)
    print(usuario)

if __name__ == "__main__":
    main()
