# sumatraPDF_Switch
A configuration file selector for the Sumatra PDF reader, which allows you to save working "sessions."

## 📝 Descripción

SumatraSettingsSwitcher permite alternar entre diferentes conjuntos de configuraciones para SumatraPDF, el popular lector de PDF ligero. 
Esta utilidad es especialmente útil si trabajas con múltiples proyectos que requieren diferentes configuraciones de visualización

El programa funciona modificando el archivo `SumatraPDF-settings.txt` que SumatraPDF utiliza para almacenar sus configuraciones, incluyendo qué archivos PDF están abiertos y sus posiciones.

## ✨ Características

- **Cambio rápido de configuraciones**: Selecciona fácilmente entre diferentes archivos de configuración guardados
- **Integración directa**: Ejecuta SumatraPDF con la configuración seleccionada con un solo clic
- **Respaldos automáticos**: Crea una copia de seguridad de tu configuración original automáticamente
- **Interfaz intuitiva**: Diseño simple pero efectivo para cambiar rápidamente entre configuraciones
- **Independiente**: No requiere instalación, funciona como un ejecutable portable

## 🚀 Instalación

### Opción 1: Descargar el ejecutable

1. Ve a la sección de [Releases](https://github.com/username/SumatraSettingsSwitcher/releases)
2. Descarga el archivo `SumatraSettingsSwitcher.exe`
3. Guardalo en la misma carpeta donde se encuentra guardado SumatraPDF
4. Ejecuta

### Opción 2: Construir desde el código fuente

Si prefieres compilar el programa tú mismo:

1. Clona este repositorio:
   ```
   git clone https://github.com/username/SumatraSettingsSwitcher.git
   ```

2. Asegúrate de tener Python 3.6+ instalado

3. Instala PyInstaller:
   ```
   pip install pyinstaller
   ```

4. Navega al directorio del proyecto y ejecuta:
   ```
   pyinstaller --onefile --windowed --name="SumatraSettingsSwitcher" sumatra_switcher.py
   ```

5. Encuentra el ejecutable en la carpeta `dist`

## 💻 Uso

1. Ejecuta `SumatraSettingsSwitcher.exe`
2. El programa detectará automáticamente la ubicación de SumatraPDF y su archivo de configuración
3. Para cargar una configuración:
   - Haz clic en "Cargar configuración"
   - Selecciona un archivo de configuración previamente guardado
   - Confirma si deseas ejecutar SumatraPDF inmediatamente
4. Para guardar la configuración actual:
   - Haz clic en "Guardar configuración actual"
   - Elige un nombre y ubicación para el archivo
5. Para restaurar la configuración original:
   - Haz clic en "Restaurar original"

## 📋 Requisitos

- Sistema operativo Windows (7, 8, 10 o 11)
- SumatraPDF instalado y ejecutado al menos una vez
- Permisos para modificar archivos en la ubicación donde está instalado SumatraPDF

## 🔧 Solución de problemas

### No se encuentra el archivo de configuración

Si el programa no puede encontrar automáticamente el archivo de configuración de SumatraPDF:

1. Asegúrate de haber ejecutado SumatraPDF al menos una vez
2. El archivo de configuración suele estar en:
   - `%APPDATA%\SumatraPDF\SumatraPDF-settings.txt`
   - `%LOCALAPPDATA%\SumatraPDF\SumatraPDF-settings.txt`
   - En la misma carpeta que el ejecutable de SumatraPDF

### No se puede ejecutar SumatraPDF

Si el programa no puede encontrar o ejecutar SumatraPDF automáticamente:

1. Se te pedirá que selecciones manualmente el ejecutable de SumatraPDF
2. Navega hasta donde tienes instalado SumatraPDF y selecciona el archivo `SumatraPDF.exe`

## 🤝 Contribuir

Las contribuciones son bienvenidas:

1. Haz fork del repositorio
2. Crea una rama para tu función (`git checkout -b feature/amazing-feature`)
3. Haz commit de tus cambios (`git commit -m 'Add some amazing feature'`)
4. Haz push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

Link del proyecto: [https://github.com/username/SumatraSettingsSwitcher](https://github.com/username/SumatraSettingsSwitcher)
