from tkinter import *
from tkinter import messagebox

def caculaIMC():
    try:
        nomePaciente = varNome.get()
        enderecoPaciente = varEndereco.get()
        alturaPaciente = float(varAltura.get().replace(',', '.'))
        pesoPaciente = float(varPeso.get().replace(',', '.'))

        if len(nomePaciente) <= 0 :
            raise ValueError('Insira um nome valido!')
        if len(enderecoPaciente) <= 0 :
            raise ValueError('Insira um endereço valido!')
        if alturaPaciente <= 0 :
            raise ValueError('Insira uma altura valida!')
        if pesoPaciente <= 0 :
            raise ValueError('Insira um peso valido!')

        IMC = round((pesoPaciente/(alturaPaciente * alturaPaciente)),2);

        if IMC < 17 :
            condicaoPaciente = "Muito abaixo do peso"
        elif IMC > 17 and IMC < 18.49:
            condicaoPaciente = "Abaixo do peso"
        elif IMC > 18.50 and IMC < 24.99:
            condicaoPaciente = "Peso normal"
        elif IMC > 25 and IMC < 29.99:
            condicaoPaciente = "Acima do peso"
        elif IMC > 30 and IMC < 34.99:
            condicaoPaciente = "Obesidade I"
        elif IMC > 35 and IMC < 39.99:
            condicaoPaciente = "Obesidade II (severa)"
        elif IMC > 40:
            condicaoPaciente = "Obesidade III (mórbida)"
        resultLabel = Label(janela, text=f"IMC igual à: {IMC}kg/m²\n{condicaoPaciente}", font="3", borderwidth=2, relief="ridge", width=20, height=4)
        resultLabel.grid(row=2, column=2, padx=10, pady=10, rowspan=2)

    except Exception as e:
        messagebox.showerror(title="Falha ao calcular IMC", message=f"{str(e)}")

def reset():
    enderecoEntry.delete(0,END)
    nomeEntry.delete(0,END)
    alturaEntry.delete(0,END)
    pesoEntry.delete(0,END)
    resultLabel = Label(janela, text=f"Resultado", font="3", borderwidth=2,
                        relief="ridge", width=20, height=4)
    resultLabel.grid(row=2, column=2, padx=10, pady=10, rowspan=2)
    nomeEntry.focus()


janela = Tk()
janela.eval('tk::PlaceWindow . center')
janela.title("Cálculo do IMC - Indice de Massa Corporal")
#janela.iconbitmap('image.ico')
janela.resizable(False,False)

#variables
varNome = StringVar();
varEndereco = StringVar();
varAltura = StringVar();
varPeso = StringVar();


nomeLabel = Label(janela, text= "Nome do paciente:", font="6")
nomeLabel.grid(row=0,column=0,padx=10,pady=10,sticky=W)
nomeEntry = Entry(janela, textvariable=varNome, width=65)
nomeEntry.grid(row=0,column=1,padx=10,pady=10,columnspan=2,sticky=W)
nomeEntry.get()


enderecoLabel = Label(janela, text= "Endereço do paciente:", font="6")
enderecoLabel.grid(row=1,column=0,padx=10,pady=0,sticky=W)
enderecoEntry = Entry(janela, textvariable=varEndereco, width=65)
enderecoEntry.grid(row=1,column=1,padx=10,pady=10,columnspan=2,sticky=W)
enderecoEntry.get()


alturaLabel = Label(janela, text= "Altura(cm):", font="6")
alturaLabel.grid(row=2,column=0,padx=10,pady=0,sticky=W)
alturaEntry = Entry(janela, textvariable=varAltura, width=30)
alturaEntry.grid(row=2,column=1,padx=10,pady=10,sticky=W)
alturaEntry.get()


pesoLabel = Label(janela, text= "Peso(kg):", font="6")
pesoLabel.grid(row=3,column=0,padx=10,pady=0,sticky=W)
pesoEntry = Entry(janela, textvariable=varPeso, width=30)
pesoEntry.grid(row=3,column=1,padx=10,pady=10,sticky=W)
pesoEntry.get()


resultLabel = Label(janela, text= "Resultado", font="6", borderwidth=2, relief="ridge", width=20,height=4)
resultLabel.grid(row=2,column=2,padx=10,pady=10,rowspan=2)


btCalcular = Button (janela, width=20, text="Calcular", command=caculaIMC)
btCalcular.grid(column=0,row=4,padx=0,pady=0)

btReiniciar = Button (janela, width=20, text="Reiniciar", command=reset)
btReiniciar.grid(column=1,row=4,padx=0,pady=0)

btSair = Button (janela, width=20, text="Sair", command=exit)
btSair.grid(column=2,row=4,padx=10,pady=20)


janela.mainloop()