import customtkinter as ctk
from tkinter import ttk
from endpoints.departamentos import Departamentos
from typing import Dict, Any
import json

class DepartmentView(ctk.CTkFrame):
    def __init__(self, master, token: str, db_id: str, **kwargs):
        super().__init__(master, **kwargs)
        self.token = token
        self.db_id = db_id
        self.departments_api = Departamentos(token, db_id)
        
        # Configure grid
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        self.create_widgets()
        self.load_departments()
        
    def create_widgets(self):
        # Header Frame
        header_frame = ctk.CTkFrame(self)
        header_frame.grid(row=0, column=0, padx=10, pady=(10,5), sticky="ew")
        header_frame.grid_columnconfigure(1, weight=1)
        
        # Title
        title_label = ctk.CTkLabel(
            header_frame,
            text="Departamentos",
            font=("Roboto", 24, "bold"),
            text_color="#ffffff"
        )
        title_label.grid(row=0, column=0, padx=10, pady=10)
        
        # Buttons Frame
        button_frame = ctk.CTkFrame(header_frame)
        button_frame.grid(row=0, column=1, padx=10, pady=5, sticky="e")
        
        # Add Department Button
        self.add_btn = ctk.CTkButton(
            button_frame,
            text="+ Novo Departamento",
            command=self.add_department
        )
        self.add_btn.grid(row=0, column=0, padx=5)
        
        # Refresh Button
        self.refresh_btn = ctk.CTkButton(
            button_frame,
            text="↻ Atualizar",
            command=self.load_departments
        )
        self.refresh_btn.grid(row=0, column=1, padx=5)
        
        # Table Frame
        table_frame = ctk.CTkFrame(self)
        table_frame.grid(row=1, column=0, padx=10, pady=(5,10), sticky="nsew")
        table_frame.grid_columnconfigure(0, weight=1)
        table_frame.grid_rowconfigure(0, weight=1)
        
        # Create Treeview]
        
        style = ttk.Style()
        style.configure("Custom.Treeview",
            background="#ffffff",
            foreground="#333333",
            rowheight=30,
            fieldbackground="#ffffff",
            font=('Arial', 12),
            bordercolor="#dddddd",  # Cor da borda das células
            borderwidth=1,          # Largura da borda
            relief="solid",         # Estilo da borda
            show="tree headings")   # Mostra linhas de grade
        
        # style.configure("Custom.Treeview.Heading",
        #        background="ffffff",      # Cor de fundo
        #        foreground="000000",        # Cor do texto
        #        font=('Arial', 10, 'bold'), # Fonte
        #        padding=(10, 5),          # Espaçamento interno
        #        relief="raised")          # Efeito 3D (flat, raised, sunken, etc.)
        
        self.tree = ttk.Treeview(
            table_frame,
            style="Custom.Treeview",
            columns=("id", "description", "nfolha"),
            show="headings",
            selectmode="browse"
        )
        
        # Configure columns
        self.tree.heading("id", text="ID")
        self.tree.heading("description", text="Descrição")
        self.tree.heading("nfolha", text="Número Folha")
        
        self.tree.column("id", width=40)
        self.tree.column("description", width=300)
        self.tree.column("nfolha", width=50)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        # Grid table and scrollbar
        self.tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Bind double click event
        self.tree.bind("<Double-1>", self.edit_department)
        
    def load_departments(self):
        try:
            # Clear existing items
            for item in self.tree.get_children():
                self.tree.delete(item)
            
            # Get departments from API
            departments = self.departments_api.get_all()
            
            # Add departments to treeview
            for dept in departments:
                self.tree.insert(
                    "",
                    "end",
                    values=(
                        dept.get("Id", ""),
                        dept.get("Descricao", ""),
                        dept.get("Nfolha", ""),
                    )
                )
        except Exception as e:
            self.show_error(f"Erro ao carregar departamentos: {str(e)}")
    
    def add_department(self):
        # TODO: Implement add department dialog
        print("Add department")
        
    def edit_department(self, event):
        # TODO: Implement edit department dialog
        item = self.tree.selection()[0]
        print(f"Edit department: {self.tree.item(item)['values']}")
        
    def show_error(self, message: str):
        # TODO: Implement proper error dialog
        print(f"Error: {message}")