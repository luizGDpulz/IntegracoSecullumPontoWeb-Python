import customtkinter as ctk

class LoginWindow(ctk.CTkToplevel):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.title("Login - Sistema Secullum")
        self.on_login_success = on_login_success
        
        # Configurações da janela
        self.geometry("400x500")
        self.minsize(350, 450)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Centralizar na tela
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')
        
        self.create_widgets()
        self.grab_set()  # Modal
        
    def create_widgets(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Título
        ctk.CTkLabel(
            main_frame, 
            text="Login API Secullum", 
            font=("Roboto", 20, "bold")
        ).pack(pady=(20, 30))
        
        # Campos de entrada
        entries = [
            ("Usuário:", "username_entry"),
            ("Senha:", "password_entry"),
            ("ID do Banco:", "db_id_entry")
        ]
        
        for label_text, attr_name in entries:
            frame = ctk.CTkFrame(main_frame)
            frame.pack(fill="x", pady=5)
            
            # Label
            ctk.CTkLabel(frame, text=label_text).pack(side="left", padx=5)
            
            # Campo de entrada
            entry = ctk.CTkEntry(
                frame,
                width=200,
                show="*" if "Senha" in label_text else ""
            )
            entry.pack(side="right", expand=True)
            setattr(self, attr_name, entry)
        
        # Botão de login
        ctk.CTkButton(
            main_frame,
            text="Entrar",
            command=self.handle_login,
            width=200
        ).pack(pady=30)
    
    def handle_login(self):
        # Obter valores
        credentials = {
            "username": self.username_entry.get(),
            "password": self.password_entry.get(),
            "db_id": self.db_id_entry.get()
        }
        
        # Validação básica
        if all(credentials.values()):
            self.on_login_success(credentials)
            self.destroy()
        else:
            self.show_error("Todos os campos são obrigatórios!")
    
    def show_error(self, message):
        error_label = ctk.CTkLabel(
            self, 
            text=message, 
            text_color="red",
            font=("Roboto", 12)
        )
        error_label.place(relx=0.5, rely=0.95, anchor="center")
        self.after(3000, error_label.destroy)
    
    def on_close(self):
        self.grab_release()
        self.destroy()
        self.master.destroy()  # Fecha aplicação se fechar login