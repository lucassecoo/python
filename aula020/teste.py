import tkinter as tk

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")
        self.master.geometry("400x600")
        self.master.configure(bg="#f0f0f0")

        self.resultado = tk.StringVar()

        # Tela de entrada
        self.tela = tk.Entry(master, textvariable=self.resultado, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
        self.tela.grid(row=0, column=0, columnspan=4)

        # Botões
        botoes = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        linha = 1
        coluna = 0
        for botao in botoes:
            tk.Button(master, text=botao, padx=20, pady=20, font=("Arial", 18), command=lambda b=botao: self.adicionar(b)).grid(row=linha, column=coluna, sticky="nsew")
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        # Botão de limpar
        tk.Button(master, text='C', padx=20, pady=20, font=("Arial", 18), command=self.limpar).grid(row=5, column=0, columnspan=4, sticky="nsew")

        # Configurar o grid
        for i in range(6):
            master.grid_rowconfigure(i, weight=1)
            master.grid_columnconfigure(i, weight=1)

    def adicionar(self, valor):
        if valor == '=':
            try:
                self.resultado.set(eval(self.resultado.get()))
            except Exception as e:
                self.resultado.set("Erro")
        else:
            self.resultado.set(self.resultado.get() + valor)

    def limpar(self):
        self.resultado.set("")

# Criação da janela principal
if __name__ == "__main__":
    root = tk.Tk()
    calculadora = Calculadora(root)
    root.mainloop()