class Personagem:
    def __init__(self, nome, idade, forca, vida, enemy):
        self.nome = nome
        self.idade = idade
        self.forca = forca
        self.vida = vida
        self.enemy = enemy

    def atacar(self, alvo, nivel):
        alvo.vida -= self.forca/10*nivel
        print(f"{self.nome} atacou {alvo} com {self.forca/10*nivel} de dano.")
    
    def curar(self, vezes=None):
        vida_antiga = self.vida
        self.vida += self.vida/10*vezes
        print(f"{self.nome} foi curado com {self.vida-vida_antiga} de vida e agora está com {self.vida}.")

    def falar(self, texto):
        print(f"{self.nome} | {texto}")


Eduardo = Personagem("Eduardo", 16, 100, 100, False)
Gabriela = Personagem("Gabriela", 17, 70, 90, False)
Monstro = Personagem("Monstro", 70, 200, 200, True)
