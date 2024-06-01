class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)
        if custo > self.plano.verificar_saldo():
            return "Saldo insuficiente para fazer a chamada."
        else:
            self.plano.deduzir_saldo(custo)
            saldo_restante = self.plano.verificar_saldo()
            return f"Chamada para {destinatario} realizada com sucesso. Saldo: ${saldo_restante:.2f}"


class Plano:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def verificar_saldo(self):
        return self.saldo

    def custo_chamada(self, duracao):
        return duracao * 0.10

    def deduzir_saldo(self, custo):
        self.saldo -= custo
        return self.saldo

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


def main():
    # Entrada:
    nome = input()
    numero = input()
    saldo_inicial = float(input())

    usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
    destinatario = input()
    duracao = int(input())

    print(usuario_pre_pago.fazer_chamada(destinatario, duracao))

if __name__ == "__main__":
    main()
