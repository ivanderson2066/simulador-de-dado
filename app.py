import random
import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

class SimuladorDeDado:
    def __init__(self, jogador):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.jogador = jogador

    def gerar_valor_do_dado(self):
        return random.randint(self.valor_minimo, self.valor_maximo)

class TelaInicial(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Simulador de Dado - Tela Inicial")
        self.pack()

        self.numero_jogadores = 2  # Defina o número desejado de jogadores
        self.nomes_jogadores = []

        for i in range(self.numero_jogadores):
            nome_jogador = simpledialog.askstring("Nome do Jogador", f"Insira o nome do Jogador {i + 1}")
            self.nomes_jogadores.append(nome_jogador)

        self.titulo = tk.Label(self, text="Bem-vindo ao Simulador de Dado!", font=("Arial", 24), fg="#333")
        self.titulo.pack(pady=20)

        self.mensagem = tk.Label(self, text="Pressione o botão para iniciar o jogo.", font=("Arial", 16), fg="#666")
        self.mensagem.pack()

        self.botao = tk.Button(self, text="Iniciar", command=self.iniciar_jogo, fg='white', bg='#2ecc71', activebackground='#27ae60', font=("Arial", 14))
        self.botao.pack(pady=20)

        self.quit_button = tk.Button(master, text='Sair', command=master.quit, fg='white', bg='#e74c3c', activebackground='#c0392b', font=("Arial", 14))
        self.quit_button.pack()

    def iniciar_jogo(self):
        self.master.destroy()
        root = tk.Tk()
        interface_grafica = InterfaceGrafica(root, self.nomes_jogadores)
        root.mainloop()

class InterfaceGrafica:
    def __init__(self, master, nomes_jogadores):
        self.master = master
        master.title('Simulador de Dado')

        self.canvas = tk.Canvas(master, width=200, height=200)
        self.canvas.pack()

        self.nomes_jogadores = nomes_jogadores
        self.jogadores = [SimuladorDeDado(nome) for nome in self.nomes_jogadores]
        self.jogador_atual = 0

        self.dado_img = Image.open("image\R.gif")
        self.dado_img = self.dado_img.resize((200, 200))
        self.dado = ImageTk.PhotoImage(self.dado_img)
        self.canvas.create_image(100, 100, image=self.dado)

        self.label = tk.Label(master, text=f"{self.nomes_jogadores[self.jogador_atual]}, clique no botão para gerar um novo valor de dado.", font=("Arial", 12), fg="#666")
        self.label.pack()

        self.button = tk.Button(master, text='Gerar Dado', command=self.gerar_dado, fg='white', bg='#3498db', activebackground='#2980b9', font=("Arial", 14))
        self.button.pack()

        self.resultado = tk.Label(master, text='', font=('Arial', 36), fg="#333")
        self.resultado.pack()

        self.voltar_button = tk.Button(master, text='Voltar', command=self.voltar_tela_inicial, fg='white', bg='#34495e', activebackground='#2c3e50', font=("Arial", 14))
        self.voltar_button.pack()

        self.quit_button = tk.Button(master, text='Sair', command=master.quit, fg='white', bg='#e74c3c', activebackground='#c0392b', font=("Arial", 14))
        self.quit_button.pack()

    def voltar_tela_inicial(self):
        self.master.destroy()
        root = tk.Tk()
        tela_inicial = TelaInicial(root)
        tela_inicial.mainloop()

    def gerar_dado(self):
        jogador = self.jogadores[self.jogador_atual]
        resultado = jogador.gerar_valor_do_dado()
        self.resultado.config(text=f'{jogador.jogador}: {resultado}')

        self.animacao(10)

        self.jogador_atual = (self.jogador_atual + 1) % len(self.nomes_jogadores)

    def animacao(self, contador):
        angulo = random.randint(-15, 15)
        self.dado_img_rotacionada = self.dado_img.rotate(45 * contador)
        self.dado = ImageTk.PhotoImage(self.dado_img_rotacionada)
        self.canvas.delete("all")
        self.canvas.create_image(100, 100, image=self.dado)

        if contador > 0:
            self.master.after(50, self.animacao, contador - 1)

if __name__ == "__main__":
    root = tk.Tk()
    tela_inicial = TelaInicial(root)
    tela_inicial.mainloop()
