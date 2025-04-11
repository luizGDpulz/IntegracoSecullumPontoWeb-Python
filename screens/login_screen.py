import customtkinter as ctk
from endpoints.apiToken import APIToken
import os

class LoginWindow(ctk.CTkToplevel):
    def __init__(self, master, on_login_success):
        super().__init__(master)
        self.title("Login - API Secullum")
        self.on_login_success = on_login_success
        
        # Configurações da janela
        self.geometry("400x400")
        # self.minsize(350, 350)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Definir ícone após a janela ser criada
        self.after(200, lambda: self.iconbitmap("assets/secullum.ico"))
        
        # Centralizar na tela
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)  # Row for spacing
        
        self.create_widgets()
        self.grab_set()  # Modal
        
    def create_widgets(self):
        # Title frame
        title_frame = ctk.CTkFrame(self)
        title_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_rowconfigure(0, weight=1)
        title_label = ctk.CTkLabel(
            title_frame, 
            text="Login API Secullum", 
            font=("Roboto", 25, "bold")
        )
        title_label.grid(row=0, column=0, pady=20, padx=20)
       
        # Campos de entrada
        entries = [
            ("Usuário:", "username_entry", ""),
            ("Senha:", "password_entry", "*"),
            ("ID do Banco:", "db_id_entry", "")
        ]
        
        entry_frame = ctk.CTkFrame(self)
        entry_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        entry_frame.grid_columnconfigure(1, weight=1)
        entry_frame.grid_rowconfigure(1, weight=1)
        
        for i, (label_text, attr_name, show) in enumerate(entries):
            ctk.CTkLabel(
                entry_frame, 
                text=label_text
            ).grid(row=i, column=0, padx=5, pady=5, sticky="e")
            
            # Campo de entrada
            entry = ctk.CTkEntry(
                entry_frame,
                width=200,
                show=show
            )
            entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
            setattr(self, attr_name, entry)
        
        button_frame = ctk.CTkFrame(self)
        button_frame.grid(row=2, column=0, padx=20, pady=20 , sticky="new")
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        # Botão de login
        login_button = ctk.CTkButton(
            button_frame,
            text="Entrar",
            command=self.authenticate,
            width=300,
            height=40,
            anchor="center"
        )
        login_button.grid(row=0, column=0, pady=30, sticky="ns")
        
        # Area para mensagem de erro
        self.error_label = ctk.CTkLabel(
            self, 
            text="",
            text_color="red",
            font=("Roboto", 12),
            width=300,
            height=40,
        )
    
    def authenticate(self):
        # Obter valores
        username = self.username_entry.get()
        password = self.password_entry.get()
        db_id = self.db_id_entry.get()
        
        # Validação básica
        if not all([username, password, db_id]):
            self.show_error("Todos os campos são obrigatórios!")
            return
            
        try:
            # Tenta autenticar usando a API
            api_token = APIToken()
            token_data = api_token.get(username, password)
            
            # Se chegou aqui, login foi bem sucedido
            credentials = {
                "username": username,
                "password": password,
                "db_id": db_id,
                "token": token_data.get('access_token')
            }
            
            self.on_login_success(credentials)
            self.destroy()
            
        except Exception as e:
            self.show_error(f"Falha no login: {str(e)}")
    
    def show_error(self, message):
        self.error_label.grid(row=2, column=0, pady=5)
        self.error_label.configure(text=message)
        self.after(3000, lambda: self.error_label.configure(text=""))
        self.error_label.after(3000, lambda: self.error_label.grid_forget())
    
    def on_close(self):
        self.grab_release()
        self.destroy()
        self.master.destroy()  # Fecha aplicação se fechar login