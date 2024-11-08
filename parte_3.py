import tkinter as tk
from tkinter import messagebox

def calcular_risco(idade, sexo, colesterol_total, hdl, pressao_sistolica, pressao_sistolica_tratada, fumante, diabetes):
    try:
        
        idade = int(idade)
        colesterol_total = int(colesterol_total)
        hdl = int(hdl)
        pressao_sistolica = int(pressao_sistolica)
        pressao_sistolica_tratada = int(pressao_sistolica_tratada)
        
        pontos = 0
        
        if sexo == "masculino":
            if 35 <= idade < 40: pontos += 2
            elif 40 <= idade < 45: pontos += 5
            elif 45 <= idade < 50: pontos += 6
            elif 50 <= idade < 55: pontos += 8
            elif 55 <= idade < 60: pontos += 10
            elif 60 <= idade < 65: pontos += 11
            elif 65 <= idade < 70: pontos += 12
            elif 70 <= idade < 75: pontos += 14
            elif 75 <= idade : pontos += 15
        else:
            if 35 <= idade < 40: pontos += 2
            elif 40 <= idade < 45: pontos += 4
            elif 45 <= idade < 50: pontos += 5
            elif 50 <= idade < 55: pontos += 7
            elif 55 <= idade < 60: pontos += 8
            elif 60 <= idade < 65: pontos += 9
            elif 65 <= idade < 70: pontos += 10
            elif 70 <= idade < 75: pontos += 11
            elif 75 <= idade : pontos += 12

        if sexo == "masculino":
            if colesterol_total < 160: pontos += 0
            elif 160 <= colesterol_total < 200: pontos += 1
            elif 200 <= colesterol_total < 240: pontos += 2
            elif 240 <= colesterol_total < 280: pontos += 3
            else: pontos += 4
        else:
            if colesterol_total < 160: pontos += 0
            elif 160 <= colesterol_total < 200: pontos += 1
            elif 200 <= colesterol_total < 240: pontos += 3
            elif 240 <= colesterol_total < 280: pontos += 4
            else: pontos += 5

        if sexo == "masculino":
            if hdl >= 60: pontos -= 2
            elif 50 <= hdl < 60: pontos -= 1
            elif 45 <= hdl < 50: pontos += 0
            elif 35 <= hdl < 45: pontos += 1
            else: pontos += 2
        else:
            if hdl >= 60: pontos -= 2
            elif 50 <= hdl < 60: pontos -= 1
            elif 45 <= hdl < 50: pontos += 0
            elif 35 <= hdl < 45: pontos += 1
            else: pontos += 2
            
        if sexo == "masculino":
            if pressao_sistolica < 120: pontos -= 2
            elif 120 <= pressao_sistolica < 130: pontos += 0
            elif 130 <= pressao_sistolica < 140: pontos += 1
            elif 140 <= pressao_sistolica < 160: pontos += 2
            else: pontos += 3
        else:
            if pressao_sistolica < 120: pontos -= 3 
            elif 120 <= pressao_sistolica < 130: pontos += 0
            elif 130 <= pressao_sistolica < 140: pontos += 1
            elif 140 <= pressao_sistolica < 150: pontos += 2
            elif 150 <= pressao_sistolica < 160: pontos += 4
            else: pontos += 5

        if sexo == "masculino":
            if pressao_sistolica_tratada < 120: pontos -= 0
            elif 120 <= pressao_sistolica_tratada < 130: pontos += 2
            elif 130 <= pressao_sistolica_tratada < 140: pontos += 3
            elif 140 <= pressao_sistolica_tratada < 160: pontos += 4
            else: pontos += 5
        else:
            if pressao_sistolica_tratada < 120: pontos -= 1 
            elif 120 <= pressao_sistolica_tratada < 130: pontos += 2
            elif 130 <= pressao_sistolica_tratada < 140: pontos += 3
            elif 140 <= pressao_sistolica_tratada < 150: pontos += 5
            elif 150 <= pressao_sistolica_tratada < 160: pontos += 6
            else: pontos += 7
            
        if sexo == "masculino":
            if fumante:
                pontos += 4
        else:
            if fumante:
                pontos += 3
                
        if sexo == "masculino":
            if diabetes:
                pontos += 3
        else:
            if diabetes:
                pontos += 4

        risco = 0
        if sexo == "masculino":
            if pontos <= -3: risco = 0.1
            elif pontos == -2: risco = 1.1
            elif pontos == -1: risco = 1.4
            elif pontos == 0: risco = 1.6
            elif pontos == 1: risco = 1.9
            elif pontos == 2: risco = 2.3
            elif pontos == 3: risco = 2.8
            elif pontos == 4: risco = 3.3
            elif pontos == 5: risco = 3.9
            elif pontos == 6: risco = 4.7
            elif pontos == 7: risco = 5.6
            elif pontos == 8: risco = 6.7
            elif pontos == 9: risco = 7.9
            elif pontos == 10: risco = 9.4
            elif pontos == 11: risco = 11.2
            elif pontos == 12: risco = 13.2
            elif pontos == 13: risco = 15.6
            elif pontos == 14: risco = 18.4
            elif pontos == 15: risco = 21.6
            elif pontos == 16: risco = 25.3
            elif pontos == 17: risco = 29.4
            elif pontos >= 18: risco = 31
        else:
            if pontos <= -2: risco = 0.1
            elif pontos == -1: risco = 1.0
            elif pontos == 0: risco = 1.2
            elif pontos == 1: risco = 1.5
            elif pontos == 2: risco = 1.7
            elif pontos == 3: risco = 2.0
            elif pontos == 4: risco = 2.4
            elif pontos == 5: risco = 2.5
            elif pontos == 6: risco = 3.3
            elif pontos == 7: risco = 3.9
            elif pontos == 8: risco = 4.5
            elif pontos == 9: risco = 5.3
            elif pontos == 10: risco = 6.3
            elif pontos == 11: risco = 7.3
            elif pontos == 12: risco = 8.6
            elif pontos == 13: risco = 10.0
            elif pontos == 14: risco = 11.7
            elif pontos == 15: risco = 13.7
            elif pontos == 16: risco = 15.9
            elif pontos == 17: risco = 18.5
            elif pontos == 18: risco = 21.6
            elif pontos == 19: risco = 24.8
            elif pontos == 20: risco = 28.5
            elif pontos >= 21: risco = 31

        return risco
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")
        return None

def calcular():
    idade = idade_entry.get()
    sexo = sexo_var.get()
    colesterol_total = colesterol_entry.get()
    hdl = hdl_entry.get()
    pressao_sistolica = pressao_entry.get()
    pressao_sistolica_tratada = pressao_tratada_entry.get()
    fumante = fumante_var.get()
    diabetes = diabetes_var.get()

    risco = calcular_risco(idade, sexo, colesterol_total, hdl, pressao_sistolica, pressao_sistolica_tratada, fumante, diabetes)
    if risco is not None:
        if risco < 1:
            resultado_label.config(text=f"Risco cardiovascular em 10 anos: <1%")
        elif risco < 30:
            resultado_label.config(text=f"Risco cardiovascular em 10 anos: {risco}%")
        else:
            resultado_label.config(text=f"Risco cardiovascular em 10 anos: >30%")
        
        if risco < 5:
            explicacao_label.config(text="Risco baixo de desenvolver doenças cardiovasculares em 10 anos.")
        elif (risco < 10 and sexo != 'masculino') or (risco < 20 and sexo == 'masculino'):
            explicacao_label.config(text="Risco intermediário de desenvolver doenças cardiovasculares em 10 anos.")
        elif ((20 <= risco < 50) and sexo == 'masculino') or ((10 <= risco < 50) and sexo != 'masculino'):
            explicacao_label.config(text="Risco alto de desenvolver doenças cardiovasculares em 10 anos.")
        else:
            explicacao_label.config(text="Risco muito alto de desenvolver doenças cardiovasculares em 10 anos.")


root = tk.Tk()
root.title("Calculadora de Risco Cardiovascular")
root.geometry("550x550")

tk.Label(root, text="Idade (anos):").pack(pady=5)
idade_entry = tk.Entry(root)
idade_entry.pack()

tk.Label(root, text="Sexo:").pack(pady=5)
sexo_var = tk.StringVar(value="masculino")
tk.Radiobutton(root, text="Masculino", variable=sexo_var, value="masculino").pack()
tk.Radiobutton(root, text="Feminino", variable=sexo_var, value="feminino").pack()

tk.Label(root, text="Colesterol Total (mg/dL):").pack(pady=5)
colesterol_entry = tk.Entry(root)
colesterol_entry.pack()

tk.Label(root, text="HDL - C(mg/dL):").pack(pady=5)
hdl_entry = tk.Entry(root)
hdl_entry.pack()

tk.Label(root, text="Pressão Arterial Sistólica (PAS) - não tratada (mmHg):").pack(pady=5)
pressao_entry = tk.Entry(root)
pressao_entry.pack()

tk.Label(root, text="Pressão Arterial Sistólica (PAS) - Tratada (mmHg):").pack(pady=5)
pressao_tratada_entry = tk.Entry(root)
pressao_tratada_entry.pack()

fumante_var = tk.BooleanVar()
tk.Checkbutton(root, text="Fumante", variable=fumante_var).pack(pady=5)

diabetes_var = tk.BooleanVar()
tk.Checkbutton(root, text="Diabético", variable=diabetes_var).pack(pady=5)

calcular_button = tk.Button(root, text="Calcular Risco", command=calcular)
calcular_button.pack(pady=20)

resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=5)

explicacao_label = tk.Label(root, text="")
explicacao_label.pack(pady=5)

root.mainloop()
