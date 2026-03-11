import tkinter as tk
    
class tiendabase(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Ventana Base")
        self.geometry("400x400")
        self.config(bg="RED")


class Tienda(tiendabase):
    def __init__(self):
        super().__init__()
        
        self.title = tk.Label(
            self,
            text="Tienda la veci",
            font=("Arial",16,"bold"),
            
        )
        self.title.pack(pady=10)
        
        
        self.producto1= tk.Label(
            self,
            text="Bebidas",
            font=("Arial",12,"bold"),
            bg="BLUE",
            fg="GREEN"
        )
        self.producto1.pack()


        #   Crear el objeto y simplemente adaptarlo        
        self.lista_bebidas=tk.Listbox(
            self,
            width=50,
            height=8,
            font=("Arial",10)
        )
        self.lista_bebidas.pack(pady=5)
        
        
        #   Ingresar productos
        self.lista_bebidas.insert(tk.END,"Coca Cola     -   1$")
        self.lista_bebidas.insert(tk.END,"Te        -       2$")
        

        
        self.producto2= tk.Label(
            self,
            text="Comida",
            font=("Arial",12,"bold"),
            bg="BLUE",
            fg="GREEN",
            width=10
        )
        self.producto2.pack(pady=5)
        
        self.lista_comida=tk.Listbox(
            self,
            width=50,
            height=8,
            font=("Arial",10)
        )
        self.lista_comida.pack(pady=5)
        
        self.lista_comida.insert(tk.END,"Encebollado    -   2#")# END: Al final del ultimo registro ingresa esto
        self.lista_comida.insert(tk.END,"Sushi      -       1$")
        
if __name__ == "__main__":
    app = Tienda()  # Crear la instancia de la tienda
    app.mainloop()  # mainloop para que se ejecute el programa sin cerrarse
