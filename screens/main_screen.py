import customtkinter as ctk
from CTkMenuBar import *
from tkinter import messagebox
import platform

class IntegrationApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Integração Secullum")
        
        # Set initial size and minimum size
        self.geometry("1280x720")
        self.minsize(1280, 720)
        self.update_idletasks()
        
        self.withdraw()  # Hide main window initially
        self._set_appearance_mode("system")
        
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
        
    def create_menu_bar(self):
        self.menu = CTkMenuBar(self)
        self.menu.grid(row=0, column=0, sticky="new")
        
        # Arquivo menu
        file_menu = self.menu.add_cascade("Arquivo")
        self.file_dropdown = CustomDropdownMenu(file_menu)
        # self.file_dropdown.add_option("Departamentos", command=lambda: self.show_departments())
        self.file_dropdown.add_separator()
        self.file_dropdown.add_option("Sair", command=self.quit)
        
        # Define menu options with their corresponding functions
        menu_options = [
            ("Afastamentos", "show_leaves"),
            ("Atividades", "show_activities"),
            ("Atividades Lançamentos", "show_activity_entries"),
            ("Batidas", "show_clock_entries"),
            ("Cálculos", "show_calculations"),
            ("Cartão Ponto", "show_time_card"),
            ("Departamentos", "show_departments"),
            ("Empresas", "show_companies"),
            ("Equipamentos", "show_equipment"),
            ("Fonte de Dados", "show_data_sources"),
            ("Funções", "show_roles"),
            ("Funcionários", "show_employees"),
            ("Horários", "show_schedules"),
            ("Incluir Ponto", "show_add_timecard"),
            ("Justificativas", "show_justifications"),
            ("Motivos de Demissão", "show_dismissal_reasons"),
            ("Perguntas Adicionais", "show_additional_questions"),
        ]

        # Create Endpoints menu
        endpoints_menu = self.menu.add_cascade("Endpoints")
        self.endpoints_dropdown = CustomDropdownMenu(endpoints_menu)
        
        # Add options using loop
        for label, func in menu_options:
            self.endpoints_dropdown.add_option(label, command=lambda f=func: getattr(self, f)())
        
        options_menu = self.menu.add_cascade("Opções")
        self.options_dropdown = CustomDropdownMenu(options_menu)
        self.options_dropdown.add_option("Configurações", command=lambda: self.show_settings())
        
        self.menu.lift()  # Ensure menu stays on top 
            
    def show_main_interface(self):
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Configure main frame
        self.main_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
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
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
            
        # Import and create department view
        from screens.department_view import DepartmentView
        department_view = DepartmentView(
            self.main_frame,
            token=self.token_api,
            db_id=self.db_id
        )
        department_view.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        
    def show_login_frame(self):
        from screens.login_screen import LoginWindow
        login_window = LoginWindow(self, self.on_login_success)
        
    def handle_credentials(self, credentials=None):
        try:
            # Store credentials for future use
            self.token_api = credentials.get('token')
            self.db_id = credentials.get('db_id')
            print(f"Token: {self.token_api}")
            print(f"DB ID: {self.db_id}")
            # Show main application interface
            self.show_main_interface()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao armazenar credênciais: {str(e)}")
            
    def on_login_success(self, credentials):
        self.deiconify()  # Show main window
        self.handle_credentials(credentials)  # Process login with credentials
