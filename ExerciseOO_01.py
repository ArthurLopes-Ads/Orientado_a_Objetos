class Televisao():
    def __init__(self):
        self.marca=''
        self.tamanho=0

tv1 = Televisao
tv1.marca = input("Marca: ")
tv1.tamanho = int(input("Tamanho: "))
print(f"Marca: {tv1.marca}, Tamanho: {tv1.tamanho}")

tv2 = Televisao()
tv2.marca = input("Marca: ")
tv2.tamanho = int(input("Tamanho: "))
print(f"Marca: {tv2.marca}, Tamanho: {tv2.tamanho}")