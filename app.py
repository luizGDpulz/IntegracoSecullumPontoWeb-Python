import customtkinter as ctk
from CTkMenuBar import *
from endpoints.apiToken import APIToken
from tkinter import messagebox

class IntegrationApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Integração Secullum")
        self.geometry("800x600")
        
        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)  # Row 1 for main content
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create main content frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        
        # Initially show login frame
        self.show_login_frame()
        
    def create_menu_bar(self):
        self.menu = CTkMenuBar(self)
        self.menu.grid(row=0, column=0, sticky="new")
        
        # File menu
        file_menu = self.menu.add_cascade("Arquivo")
        self.file_dropdown = CustomDropdownMenu(file_menu)
        # self.file_dropdown.add_option("Departamentos", command=lambda: self.show_departments())
        self.file_dropdown.add_separator()
        self.file_dropdown.add_option("Sair", command=self.quit)
        
        # Departamentos menu
        endpoints_menu = self.menu.add_cascade("Endpoints")
        self.endpoints_dropdown = CustomDropdownMenu(endpoints_menu)
        self.endpoints_dropdown.add_option("Atividades", command=lambda: self.show_activities())
        self.endpoints_dropdown.add_option("Atividades Lançamentos", command=lambda: self.show_activity_entries())
        self.endpoints_dropdown.add_option("Batidas", command=lambda: self.show_clock_entries())
        self.endpoints_dropdown.add_option("Cálculos", command=lambda: self.show_calculations())
        self.endpoints_dropdown.add_option("Cartão Ponto", command=lambda: self.show_time_card())
        self.endpoints_dropdown.add_option("Departamentos", command=lambda: self.show_departments())
        self.endpoints_dropdown.add_option("Empresas", command=lambda: self.show_companies())
        self.endpoints_dropdown.add_option("Equipamentos", command=lambda: self.show_equipment())
        self.endpoints_dropdown.add_option("Fonte de Dados", command=lambda: self.show_data_sources())
        self.endpoints_dropdown.add_option("Funcionários", command=lambda: self.show_employees())
        self.endpoints_dropdown.add_option("Afastamentos", command=lambda: self.show_leaves())
        self.endpoints_dropdown.add_option("Funções", command=lambda: self.show_roles())
        self.endpoints_dropdown.add_option("Horários", command=lambda: self.show_schedules())
        self.endpoints_dropdown.add_option("Incluir Ponto", command=lambda: self.show_add_timecard())
        self.endpoints_dropdown.add_option("Justificativas", command=lambda: self.show_justifications())
        self.endpoints_dropdown.add_option("Motivos de Demissão", command=lambda: self.show_dismissal_reasons())
        self.endpoints_dropdown.add_option("Perguntas Adicionais", command=lambda: self.show_additional_questions())
        
        # self.departamentos_dropdown.add_option("Listar Todos", command=lambda: self.show_departments())
        # self.departamentos_dropdown.add_option("Buscar por Descrição", command=lambda: self.show_departments())
        # self.departamentos_dropdown.add_option("Criar/Atualizar", command=lambda: self.show_departments())
        # self.departamentos_dropdown.add_option("Deletar", command=lambda: self.show_departments())
        
        self.menu.lift()  # Ensure menu stays on top
        
    def show_login_frame(self):
        # Reset main frame position
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Configure main frame grid
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
            
        # Create login frame
        login_frame = ctk.CTkFrame(self.main_frame)
        login_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        # Configure login frame grid
        login_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        ctk.CTkLabel(login_frame, text="Login Secullum", font=("Roboto", 24)).grid(row=0, column=0, pady=(20, 10))
        
        # Username field
        ctk.CTkLabel(login_frame, text="Usuário:").grid(row=1, column=0, pady=(10, 0))
        self.username_entry = ctk.CTkEntry(login_frame, width=200)
        self.username_entry.grid(row=2, column=0, pady=(0, 10))
        
        # Password field
        ctk.CTkLabel(login_frame, text="Senha:").grid(row=3, column=0, pady=(10, 0))
        self.password_entry = ctk.CTkEntry(login_frame, show="*", width=200)
        self.password_entry.grid(row=4, column=0, pady=(0, 10))
        
        # Database ID field
        ctk.CTkLabel(login_frame, text="ID do Banco:").grid(row=5, column=0, pady=(10, 0))
        self.db_id_entry = ctk.CTkEntry(login_frame, width=200)
        self.db_id_entry.grid(row=6, column=0, pady=(0, 10))
        
        # Login button
        ctk.CTkButton(
            login_frame, 
            text="Entrar", 
            command=self.handle_login,
            width=200
        ).grid(row=7, column=0, pady=20)
        
    def handle_login(self):
        # username = self.username_entry.get()
        # password = self.password_entry.get()
        # db_id = self.db_id_entry.get()
        
        username = "teste@api.com"
        password = "api@123"
        db_id = 117408
        
        if not all([username, password, db_id]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return
            
        try:
            api_token = APIToken()
            token_data = api_token.get(username, password)
            
            # Store token and database ID for future use
            self.token_api = token_data.get('access_token')
            self.db_id = db_id
            
            # Show success message
            # messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
            
            # Show main application interface
            self.show_main_interface()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Falha no login: {str(e)}")
            
    def show_main_interface(self):
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Configure main frame
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        
        # Welcome message in main frame
        welcome_label = ctk.CTkLabel(
            self.main_frame,
            text="Bem-vindo ao Sistema de Integração Secullum",
            font=("Roboto", 20)
        )
        welcome_label.grid(row=0, column=0, pady=20, sticky="n")
        
    def show_departments(self):
        # TODO: Implement departments view
        print("Show departments view")
        print(f"Token: {self.token_api}")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
    ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
    
    app = IntegrationApp()
    app.mainloop()