import tkinter as tk
from tkinter import messagebox

def calcular_tfg(creatinina, idade, sexo):
    try:
        
        if ',' in creatinina:
            creatinina = float(creatinina.replace(',', '.'))
        else:
            creatinina = float(creatinina)
            
        idade = int(idade)

        if sexo.lower() == "masculino":
            k = 0.9
            alfa = -0.411
        elif sexo.lower() == "feminino":
            k = 0.7
            alfa = -0.329
        else:
            raise ValueError("Sexo inválido.")

        tfg = 141 * min(creatinina / k, 1) ** alfa * max(creatinina / k, 1) ** -1.209 * 0.993 ** idade
        if sexo.lower() == "feminino":
            tfg *= 1.018

        return tfg
    except ValueError as e:
        messagebox.showerror("Erro insira um valor válido.")
        return None

def classificar_tfg(tfg):
    if tfg >= 90:
        return "G1: Função renal normal ou elevada"
    elif 60 <= tfg < 90:
        return "G2: Disfunção renal leve"
    elif 45 <= tfg < 60:
        return "G3a: Disfunção renal leve a moderada"
    elif 30 <= tfg < 45:
        return "G3b: Disfunção renal moderada a grave"
    elif 15 <= tfg < 30:
        return "G4: Disfunção renal grave"
    else:
        return "G5: Insuficiência renal"

def calcular():
    creatinina = creatinina_entry.get()
    idade = idade_entry.get()
    sexo = sexo_var.get()

    tfg = calcular_tfg(creatinina, idade, sexo)
    if tfg is not None:
        classificacao = classificar_tfg(tfg)
        resultado_label.config(text=f"TFG estimada: {tfg:.2f} mL/min/1,73 m²\n{classificacao}")

root = tk.Tk()
root.title("Calculadora de TFG (CKD-EPI)")

window_width = 400
window_height = 300

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int((screen_width - window_width) / 2)
center_y = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

tk.Label(root, text="Creatinina sérica (mg/dL):").pack(pady=5)
creatinina_entry = tk.Entry(root)
creatinina_entry.pack()

tk.Label(root, text="Idade (anos):").pack(pady=5)
idade_entry = tk.Entry(root)
idade_entry.pack()

tk.Label(root, text="Sexo:").pack(pady=5)
sexo_var = tk.StringVar(value="masculino")
tk.Radiobutton(root, text="Masculino", variable=sexo_var, value="masculino").pack()
tk.Radiobutton(root, text="Feminino", variable=sexo_var, value="feminino").pack()

calcular_button = tk.Button(root, text="Calcular TFG", command=calcular)
calcular_button.pack(pady=15)

resultado_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
resultado_label.pack(pady=10)

root.mainloop()
