import tkinter as tk
from tkinter import messagebox

# Variables del juego
player = 'X'
game_over = False
buttons = [[None, None, None], [None, None, None], [None, None, None]]  # Matriz de botones

# Función para validar si hay un ganador
def check_winner():
    # Comprobar filas
    for i in range(3):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return True
    # Comprobar columnas
    for i in range(3):
        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return True
    # Comprobar diagonal principal
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return True
    # Comprobar diagonal secundaria
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return True
    return False

# Función cuando se hace clic en un botón
def button_click(row, col):
    global player, game_over
    if buttons[row][col]['text'] == '' and not game_over:
        buttons[row][col]['text'] = player
        buttons[row][col]['bg'] = '#37474f' if player == 'X' else '#455A64'
        if check_winner():
            messagebox.showinfo("¡Ganador!", f"¡El jugador {player} ha ganado!")
            game_over = True
        else:
            player = 'O' if player == 'X' else 'X'  # Cambiar de jugador

# Crear la ventana principal
root = tk.Tk()
root.title("Juego de Triki")

# Crear los botones
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', width=10, height=3, font=("Arial", 24),
                                  command=lambda i=i, j=j: button_click(i, j))
        buttons[i][j].grid(row=i, column=j)

# Función para reiniciar el juego
def restart_game():
    global player, game_over
    player = 'X'
    game_over = False
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ''
            buttons[i][j]['bg'] = 'SystemButtonFace'

# Botón para reiniciar el juego
restart_button = tk.Button(root, text="Reiniciar", font=("Arial", 14), command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3, pady=10)

# Ejecutar la interfaz
root.mainloop()

         
        
        





