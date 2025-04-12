class Televisão:
    def __init__(self, canal_inicial=2):
        self.ligada = False
        self.canal = canal_inicial

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False

    def muda_canal_para_cima(self):
        if self.ligada:
            self.canal += 1
        else:
            print("A televisão está desligada. Não é possível mudar o canal.")

    def muda_canal_para_baixo(self):
        if self.ligada:
            if self.canal > 0:  # Ensure channel doesn't go below 0
                self.canal -= 1
            else:
                print("Você já está no canal mais baixo.")
        else:
            print("A televisão está desligada. Não é possível mudar o canal.")

    def mostrar_estado(self):
        estado = "ligada" if self.ligada else "desligada"
        print(f"A televisão está {estado}. Canal atual: {self.canal}")

# Testando o código
tv = Televisão()
tv.ligar()
tv.muda_canal_para_cima()
tv.muda_canal_para_cima()
tv.mostrar_estado()  # Exibe: Ligada, Canal: 4

tv.muda_canal_para_baixo()
tv.mostrar_estado()  # Exibe: Ligada, Canal: 3

tv.desligar()
tv.muda_canal_para_cima()  # Mostra mensagem de erro

