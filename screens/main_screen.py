import customtkinter as ctk
from CTkMenuBar import *
from endpoints.apiToken import APIToken
from tkinter import messagebox
import platform

class IntegrationApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Integração Secullum")
        self.geometry("854x480")
        self.withdraw()  # Hide main window initially
        
        # Set icon
        self.iconbitmap("assets/secullum.ico")
        
        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)  # Row 1 for main content
        
        # Create menu bar
        self.create_menu_bar()
        
        # Create main content frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        
        # Show login frame immediately
        self.show_login_frame()
        
    def maximized_window(self):
        if platform.system == "Windows":
            self.state('zoomed')
        elif platform.system == "Linux":
            self.attributes('-zoomed', True)
        else: 
            self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        
    def create_menu_bar(self):
        self.menu = CTkMenuBar(self)
        self.menu.grid(row=0, column=0, sticky="new")
        
        # Arquivo menu
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
        
        self.menu.lift()  # Ensure menu stays on top
            
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
        
    def show_login_frame(self):
        from screens.login_screen import LoginWindow
        login_window = LoginWindow(self, self.on_login_success)
        
    def on_login_success(self, credentials):
        self.deiconify()  # Show main window
        self.handle_login()  # Process login with stored credentials
