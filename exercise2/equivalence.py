class Participante:
    def __init__(self, idade, categoria, tempoEstimado, assinaturaTermo):
        self.idade = idade
        self.categoria = categoria
        self.tempoEstimado = tempoEstimado
        self.assinaturaTermo = assinaturaTermo


def verificarCadastro(participante):
    if not (10 <= participante.idade <= 60):
        return False
    if participante.idade <= 14 and participante.categoria != "infantil":
        return False
    if 15 <= participante.idade <= 17 and participante.categoria != "juvenil":
        return False
    if 18 <= participante.idade <= 60 and participante.categoria != "adulto":
        return False
    if not (30 <= participante.tempoEstimado <= 180):
        return False
    if not participante.assinaturaTermo:
        return False
    return True


p1 = Participante(12, "infantil", 60, True)
assert verificarCadastro(p1) == True

p2 = Participante(16, "juvenil", 90, True)
assert verificarCadastro(p2) == True

p3 = Participante(30, "adulto", 45, True)
assert verificarCadastro(p3) == True

p4 = Participante(9, "infantil", 60, True)
assert verificarCadastro(p4) == False

p5 = Participante(61, "adulto", 60, True)
assert verificarCadastro(p5) == False

p6 = Participante(12, "adulto", 60, True)
assert verificarCadastro(p6) == False

p7 = Participante(16, "sênior", 60, True)
assert verificarCadastro(p7) == False

p8 = Participante(20, "adulto", 25, True)
assert verificarCadastro(p8) == False

p9 = Participante(20, "adulto", 200, True)
assert verificarCadastro(p9) == False

p10 = Participante(20, "adulto", 60, False)
assert verificarCadastro(p10) == False
