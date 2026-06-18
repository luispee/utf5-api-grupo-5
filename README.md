# Patrones de diseño y arquitectura – Trabajo final de unidad.

API para la gestión de FoodTrucks. Desarrollada con **FastAPI** y **Uvicorn**.


##  Instalación y Ejecución

Configurar el entorno y levantar el proyecto localmente:

### 1. Acceder a la carpeta del proyecto
```bash
cd foodtruck-api
```

### 2. Crear y activar el entorno virtual (`venv`)
* **En Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
* **En macOS/Linux:**
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor de desarrollo
```bash
uvicorn app.main:app --reload
```

---

## Endpoints y Verificación

Una vez que el servidor esté corriendo, la API estará disponible en la siguiente dirección:

* **Base de la API:** `http://localhost:8000`

### 📑 Documentación Interactiva
Para probar los endpoints, validar las rutas y ver la documentación generada automáticamente por Swagger, ingresar a:
**[http://localhost:8000/docs](http://localhost:8000/docs)**

---
