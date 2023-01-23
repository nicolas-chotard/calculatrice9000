import tkinter as tk

# Fonction pour gérer le clic sur les boutons de chiffres
def click_chiffre(num):
    global formula
    formula += str(num)
    update_formula_field()

# Fonction pour gérer le clic sur le bouton "="
def clique_egale():
    global formula
    try:
        result = eval(formula)
        formula = str(result)
        update_formula_field()
    except:
        formula = ""
        update_formula_field(error=True)

# Fonction pour gérer le clic sur le bouton "C"
def clique_C():
    global formula
    formula = ""
    update_formula_field()

#Fonction pour gérer le clic sur le bouton "%"
def clique_pourcentage():
    global formula
    try:
        result = eval(formula) / 100
        formula = str(result)
        update_formula_field()
    except:
        formula = ""
        update_formula_field(error=True)

#Fonction pour gérer le clic sur le bouton "√"
def clique_V():
    global formula
    try:
        result = eval(formula) ** 0.5
        formula = str(result)
        update_formula_field()
    except:
        formula = ""
        update_formula_field(error=True)

#Fonction pour gérer le clic sur le bouton "1/x"
def clique_inverse():
    global formula
    try:
        result = 1 / eval(formula)
        formula = str(result)
        update_formula_field()
    except:
        formula = ""
        update_formula_field(error=True)



# Fonction pour mettre à jour le champ d'entrée
def update_formula_field(error=False):
    if error:
        formula_field.config(fg="red")
        formula_field.delete(0, "end")
        formula_field.insert(0, " error ")
    else:
        formula_field.config(fg="black")
        formula_field.delete(0, "end")
        formula_field.insert(0, formula)

# Initialisation de la variable globale "formula"
formula = ""

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice")


# Création du champ d'entrée
formula_field = tk.Entry(root, width=45 ,borderwidth=5)
formula_field.grid(row=0, column=0 ,columnspan=4, padx=40, pady=40)

# Création du cadre pour les boutons de chiffres
digit_button_frame = tk.Frame(root)
digit_button_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Boucle pour créer les boutons de chiffres
for i in range(3):
    for j in range(3):
        button = tk.Button(digit_button_frame, text=str((i*3)+j+1), padx=40, pady=20,command=lambda num= (i*3)+j+1 : click_chiffre(num))
        button.grid(row=i, column=j)

# Bouton 0
button_0 = tk.Button(digit_button_frame, text="0", padx=40, pady=20, command=lambda: click_chiffre(0))
button_0.grid(row=3, column=0)

# Cadre pour les boutons d'opération
operation_frame = tk.Frame(root)
operation_frame.grid(row=1, column=4, padx=10, pady=10)

# Liste des opérations
operations = ["+", "-", "*", "/", "."]

# Boucle pour créer les boutons d'opération
for operation in operations:
    button = tk.Button(operation_frame, text=operation, padx=60, pady=20, background="grey", command=lambda op = operation: click_chiffre(op))
    button.pack()

#Bouton "%"
button_equal = tk.Button(operation_frame, text="%", padx=60, pady=20, command=clique_pourcentage)
button_equal.pack()


#Bouton pour faire la racine caré
button_clear = tk.Button(operation_frame, text="√", padx=60, pady=20, command=clique_V)
button_clear.pack()

#Bouton pour faire fonction inverse
button_clear = tk.Button(operation_frame, text="1/x", padx=60, pady=20, command=clique_inverse)
button_clear.pack()

# Bouton "C"
button_clear = tk.Button(operation_frame, text="C", padx=60, pady=20, command=clique_C)
button_clear.pack()

# Bouton "="
button_equal = tk.Button(operation_frame, text="=", padx=60, pady=20, command=clique_egale)
button_equal.pack()


# Lancement de la boucle principale de l'application
root.mainloop()


