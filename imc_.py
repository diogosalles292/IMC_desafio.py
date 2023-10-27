import tkinter as tk

def calcular():
    peso = float(entry_peso.get())
    altura = float(entry_altura.get())**2
    resultado = peso/altura 
    print(peso, altura, resultado)

    if resultado < 18.6:
       resultado['text'] = "Seu IMC é: Abaixo do peso"
    elif resultado >= 18.5 and resultado < 24.9:
         resultado['text'] = "Seu IMC é: Normal"
    elif resultado >=25 and resultado < 29.9:
        resultado['text'] ="Seu IMC é: Sobrepeso"
    else:
        resultado['text'] = "Seu IMC é: Obesidade"
        
    resultado['text'] = "{:.{}f}".format(resultado, 2)


    
   

root = tk.Tk()
root.title("Calculadora de IMC")

label_peso = tk.Label(root, text="Insira seu peso:")
entry_peso = tk.Entry(root)

label_altura = tk.Label(root, text="Insira sua altura:")
entry_altura = tk.Entry(root)






botao_calcular = tk.Button(root, text="calcular", command=calcular)



label_peso.pack()
entry_peso.pack()
label_altura.pack()
entry_altura.pack()
botao_calcular.pack()


root.mainloop()