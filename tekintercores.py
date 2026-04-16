import tkinter as tk

janela = tk.Tk()
janela.geometry('600x400')
janela.title("minecraft")

frameazul = tk.Frame(janela, bg="lightblue", bd=0)
frameazul.place(rely=0, relx=0, relheight=1.0, relwidth=0.2)
textoazul = tk.Label(frameazul, text="explorador", bg="lightblue")
textoazul.place(rely=0.1, relx=0.2)

frameverde = tk.Frame(janela, bg="green", bd=0)
frameverde.place(rely=0.0, relx=0.2 , relheight=0.1 , relwidth=1.0)
textoverde = tk.Label(frameverde, text="páginas de códigos", bg="green", fg="white")
textoverde.place(rely=0.4, relx=0.1)

frameverdeclaro = tk.Frame(janela, bg="lightgreen", bd=0)
frameverdeclaro.place(rely=0.1, relx= 0.2, relheight=0.7, relwidth=1.0)
textoverdeclaro = tk.Label(frameverdeclaro, text="editor de código", bg="lightgreen")
textoverdeclaro.place(rely=0.2, relx=0.1)

frameamarelo = tk.Frame(janela, bg="yellow", bd=0)
frameamarelo.place(rely=0.8, relx=0.2, relheight=0.3, relwidth=1.0)
textoamarelo = tk.Label(frameamarelo, text="terminal", bg="yellow")
textoamarelo.place(rely=0.1, relx=0.1)


janela.mainloop()

