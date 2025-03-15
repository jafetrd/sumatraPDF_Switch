import os
import sys
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path

class SumatraPDFSettingsSwitcher:
    def __init__(self):
        self.sumatra_settings_path = self.find_sumatra_settings()
        
        if not self.sumatra_settings_path:
            print("No se pudo encontrar el archivo de configuración de SumatraPDF.")
            print("Por favor, ejecute SumatraPDF al menos una vez para crear el archivo de configuración.")
            messagebox.showerror("Error", "No se pudo encontrar el archivo de configuración de SumatraPDF.\n"
                                "Por favor, ejecute SumatraPDF al menos una vez para crear el archivo de configuración.")
            sys.exit(1)
            
        self.sumatra_exe_path = self.find_sumatra_exe()
        self.backup_settings()
        self.create_gui()
    
    def find_sumatra_settings(self):
        """Busca la ubicación del archivo SumatraPDF-settings.txt"""
        possible_locations = [
            os.path.join(os.getenv('APPDATA'), 'SumatraPDF'),
            os.path.join(os.getenv('LOCALAPPDATA'), 'SumatraPDF'),
            os.path.dirname(sys.executable),
            os.getcwd()
        ]
        
        for location in possible_locations:
            if location:
                settings_path = os.path.join(location, 'SumatraPDF-settings.txt')
                if os.path.exists(settings_path):
                    return settings_path
                
        # Buscar en el directorio de programas
        program_files = [
            os.getenv('PROGRAMFILES'),
            os.getenv('PROGRAMFILES(X86)')
        ]
        
        for pf in program_files:
            if pf:
                settings_path = os.path.join(pf, 'SumatraPDF', 'SumatraPDF-settings.txt')
                if os.path.exists(settings_path):
                    return settings_path
        
        return None
    
    def find_sumatra_exe(self):
        """Busca la ubicación del ejecutable de SumatraPDF"""
        settings_dir = os.path.dirname(self.sumatra_settings_path)
        exe_path = os.path.join(settings_dir, 'SumatraPDF.exe')
        
        if os.path.exists(exe_path):
            return exe_path
            
        program_files = [
            os.getenv('PROGRAMFILES'),
            os.getenv('PROGRAMFILES(X86)')
        ]
        
        for pf in program_files:
            if pf:
                exe_path = os.path.join(pf, 'SumatraPDF', 'SumatraPDF.exe')
                if os.path.exists(exe_path):
                    return exe_path
        
        # Pedir al usuario que seleccione manualmente el ejecutable
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("Seleccionar SumatraPDF", 
                           "No se pudo encontrar SumatraPDF.exe automáticamente.\n"
                           "Por favor, seleccione manualmente el ejecutable.")
        exe_path = filedialog.askopenfilename(
            title="Seleccione SumatraPDF.exe",
            filetypes=[("Executable files", "*.exe")]
        )
        
        if exe_path and os.path.basename(exe_path).lower() == 'sumatrapdf.exe':
            return exe_path
        else:
            messagebox.showerror("Error", "No se seleccionó un ejecutable válido de SumatraPDF.")
            sys.exit(1)
    
    def backup_settings(self):
        """Crea una copia de seguridad de la configuración original"""
        backup_path = self.sumatra_settings_path + '.backup'
        if not os.path.exists(backup_path):
            try:
                shutil.copy2(self.sumatra_settings_path, backup_path)
                print(f"Copia de seguridad creada en {backup_path}")
            except Exception as e:
                print(f"Error al crear copia de seguridad: {str(e)}")
    
    def load_settings_file(self):
        """Permite al usuario seleccionar un archivo de configuración personalizado"""
        file_path = filedialog.askopenfilename(
            title="Seleccione un archivo de configuración para SumatraPDF",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                # Hacer copia de seguridad del archivo actual si no es la original
                temp_backup = self.sumatra_settings_path + '.temp'
                shutil.copy2(self.sumatra_settings_path, temp_backup)
                
                # Copiar el nuevo archivo
                shutil.copy2(file_path, self.sumatra_settings_path)
                self.status_label.config(text=f"Configuración cargada: {os.path.basename(file_path)}")
                
                # Preguntar si desea ejecutar SumatraPDF
                if messagebox.askyesno("Ejecutar SumatraPDF", "¿Desea ejecutar SumatraPDF con esta configuración?"):
                    self.run_sumatra()
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar la configuración: {str(e)}")
    
    def save_current_settings(self):
        """Guarda la configuración actual con un nuevo nombre"""
        file_path = filedialog.asksaveasfilename(
            title="Guardar configuración actual",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                shutil.copy2(self.sumatra_settings_path, file_path)
                messagebox.showinfo("Éxito", f"Configuración guardada como {os.path.basename(file_path)}")
                self.status_label.config(text=f"Configuración guardada: {os.path.basename(file_path)}")
            except Exception as e:
                messagebox.showerror("Error", f"Error al guardar la configuración: {str(e)}")
    
    def restore_original_settings(self):
        """Restaura la configuración original"""
        backup_path = self.sumatra_settings_path + '.backup'
        if os.path.exists(backup_path):
            try:
                shutil.copy2(backup_path, self.sumatra_settings_path)
                self.status_label.config(text="Configuración original restaurada")
                
                # Preguntar si desea ejecutar SumatraPDF
                if messagebox.askyesno("Ejecutar SumatraPDF", "¿Desea ejecutar SumatraPDF con la configuración original?"):
                    self.run_sumatra()
            except Exception as e:
                messagebox.showerror("Error", f"Error al restaurar la configuración: {str(e)}")
        else:
            messagebox.showwarning("Advertencia", "No se encontró copia de seguridad de la configuración original")
    
    def run_sumatra(self):
        """Ejecuta SumatraPDF"""
        try:
            subprocess.Popen([self.sumatra_exe_path])
            print(f"SumatraPDF iniciado con la configuración seleccionada")
        except Exception as e:
            messagebox.showerror("Error", f"Error al iniciar SumatraPDF: {str(e)}")
    
    def create_gui(self):
        """Crea la interfaz gráfica"""
        self.root = tk.Tk()
        self.root.title("Selector de Configuraciones para SumatraPDF")
        self.root.geometry("550x350")
        self.root.resizable(True, True)
        
        # Establecer icono si está disponible
        try:
            self.root.iconbitmap(default=os.path.join(os.path.dirname(self.sumatra_exe_path), "SumatraPDF.ico"))
        except:
            pass
        
        # Frame principal
        main_frame = tk.Frame(self.root, padx=20, pady=20)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Información
        tk.Label(main_frame, text="Selector de Configuraciones para SumatraPDF", font=("Arial", 14, "bold")).pack(pady=(0, 20))
        
        info_text = f"Configuración actual: {self.sumatra_settings_path}\n\nEjecutable: {self.sumatra_exe_path}"
        info_label = tk.Label(main_frame, text=info_text, justify=tk.LEFT, wraplength=500)
        info_label.pack(anchor=tk.W, pady=(0, 20))
        
        # Frame para los botones
        button_frame = tk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        # Botones principales
        tk.Button(button_frame, text="Cargar configuración", command=self.load_settings_file, 
                 width=20, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Guardar configuración actual", command=self.save_current_settings, 
                 width=25).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Restaurar original", command=self.restore_original_settings, 
                 width=15).pack(side=tk.LEFT, padx=5)
        
        # Botón para ejecutar SumatraPDF
        run_button = tk.Button(main_frame, text="Ejecutar SumatraPDF", command=self.run_sumatra, 
                             font=("Arial", 11, "bold"), bg="#1E88E5", fg="white", 
                             height=2, width=20)
        run_button.pack(pady=20)
        
        # Instrucciones
        instructions = (
            "Instrucciones:\n"
            "1. Use 'Cargar configuración' para seleccionar un archivo de configuración personalizado.\n"
            "2. Use 'Guardar configuración actual' para guardar la configuración actual con otro nombre.\n"
            "3. Use 'Restaurar original' para volver a la configuración inicial.\n"
            "4. Presione 'Ejecutar SumatraPDF' para abrir el programa con la configuración actual."
        )
        
        instructions_label = tk.Label(main_frame, text=instructions, justify=tk.LEFT, 
                                   bg="#f0f0f0", relief=tk.GROOVE, padx=10, pady=10)
        instructions_label.pack(fill=tk.X, pady=(0, 10))
        
        # Etiqueta de estado
        self.status_label = tk.Label(main_frame, text="Listo para usar", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Centrar ventana
        self.center_window()
        
        self.root.mainloop()
    
    def center_window(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

if __name__ == "__main__":
    try:
        app = SumatraPDFSettingsSwitcher()
    except Exception as e:
        tk.Tk().withdraw()
        messagebox.showerror("Error", f"Error al iniciar la aplicación: {str(e)}")
