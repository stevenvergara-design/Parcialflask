# 🔐 Gestor de Contraseñas Seguro (Flask + MVC)

Aplicación web para la gestión segura de credenciales (usuario y contraseña), desarrollada en **Python con Flask**, aplicando el patrón de arquitectura **Modelo-Vista-Controlador (MVC)** y principios de **Programación Orientada a Objetos (POO)**.

---

## 🚀 Características

* Registro de contraseña maestra
* Autenticación de usuario (login)
* Panel principal (dashboard)
* Gestión de credenciales:

  * Crear credenciales
  * Listar credenciales
* Visualización segura:

  * Mostrar/Ocultar contraseña bajo demanda

---

## 🏗️ Arquitectura (MVC)

El proyecto está estructurado bajo el patrón MVC:

* **Model (Modelo):**

  * Manejo de base de datos SQLite
  * Lógica de acceso a datos
* **View (Vista):**

  * Interfaces HTML (templates)
* **Controller (Controlador):**

  * Manejo de rutas y lógica de negocio con Flask Blueprints

✔ Separación clara de responsabilidades
✔ Código mantenible y escalable

---

## 📂 Estructura del Proyecto

```
Parcial/
│
├── app.py
├── controllers/
│   ├── auth_controller.py
│   └── credencial_controller.py
│
├── models/
│   ├── db.py
│   ├── usuario_model.py
│   └── credencial_model.py
│
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── crear.html
│   └── ver.html
│
├── database.db
└── requirements.txt
```

---

## 🔐 Seguridad Implementada

### 🔑 Hash (bcrypt)

* Utilizado para la **contraseña maestra**
* No reversible
* Protege contra acceso directo a la base de datos

### 🔒 Cifrado (Fernet)

* Utilizado para las **credenciales almacenadas**
* Permite recuperar la contraseña cuando el usuario lo solicita
* Se usa cifrado simétrico seguro

---

## 🧠 Diferencia Clave

| Tipo    | Uso                | ¿Se puede recuperar? |
| ------- | ------------------ | -------------------- |
| Hash    | Contraseña maestra | ❌ No                 |
| Cifrado | Credenciales       | ✅ Sí                 |

---

## 💾 Base de Datos

* Motor: **SQLite**
* Archivo: `database.db`

### Tablas:

**usuario**

* id
* password_hash

**credenciales**

* id
* servicio
* usuario
* password_encriptada

---

## ⚙️ Instalación y Ejecución

### 1. Clonar repositorio

```bash
git clone <TU_REPOSITORIO>
cd Parcial
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno

```bash
venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Ejecutar aplicación

```bash
python app.py
```

### 6. Abrir en navegador

```
http://127.0.0.1:5000
```

---

## 🧪 Flujo de Uso

1. Crear contraseña maestra
2. Iniciar sesión
3. Acceder al dashboard
4. Crear credenciales
5. Visualizar credenciales
6. Mostrar/ocultar contraseña

---

## 🧠 Conceptos Aplicados

* Arquitectura MVC
* Programación Orientada a Objetos
* Seguridad:

  * Hash (bcrypt)
  * Cifrado (Fernet)
* Persistencia con SQLite
* Flask Blueprints

---

## 📌 Notas

* Las contraseñas nunca se almacenan en texto plano
* La visualización de contraseñas es bajo demanda
* La clave de cifrado debe mantenerse segura

---

## 👨‍💻 Autor

Desarrollado por **Steven Vergara**

---

## 📄 Licencia

Uso académico
