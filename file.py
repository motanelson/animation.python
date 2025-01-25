
import tkinter as tk
from PIL import Image, ImageTk
import time

def move_bitmap():
    global y_position

    # Atualiza a posição do bitmap
    if y_position < window_height - bitmap_height:
        y_position += 5  # Ajusta a velocidade da descida
        canvas.move(bitmap, 0, 5)
        root.after(50, move_bitmap)  # Chama a função novamente após 50ms

# Cria a janela principal
root = tk.Tk()
root.title("Aterrissagem da Nave")
root.configure(bg="yellow")

# Define as dimensões da janela
window_width = 400
window_height = 600
root.geometry(f"{window_width}x{window_height}")

# Cria o canvas para exibir o bitmap
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="yellow", highlightthickness=0)
canvas.pack()

# Carrega a imagem do bitmap
image = Image.open("bit.png")
bitmap_image = ImageTk.PhotoImage(image)
bitmap_width, bitmap_height = image.size

# Calcula a posição inicial
x_position = (window_width - bitmap_width) // 2  # Centraliza horizontalmente
y_position = 0

# Adiciona o bitmap ao canvas
bitmap = canvas.create_image(x_position, y_position, anchor=tk.NW, image=bitmap_image)

# Inicia o movimento do bitmap
move_bitmap()

# Executa a aplicação
root.mainloop()
