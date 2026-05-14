# aXet.Skills

Workflow oficial para la instalación de **skills** en proyectos que utilizan `aXet.plugin`.

---

## 📌 Descripción

`aXet.Skills` es un workflow que permite instalar skills desde el [repositorio oficial](https://github.com/mpalancc/aXet.skills.git)

La instalación se realiza automáticamente validando:

- Existencia local
- Existencia remota
- Descarga del workflow principal
- Procesamiento opcional de `manifest.json`
- Descarga de archivos adicionales definidos en el manifest

---

## 🌱 Instalación

Descargar el archivo [axet.skills](https://raw.githubusercontent.com/mpalancc/aXet.skills/refs/heads/main/axet.skills) y guardarlo en el directorio `%USERPROFILE%\OneDrive - NTT DATA EMEAL\Documentos\Cline\Workflows` para que sea accesible globalmente en cualquier proyecto

---

## 🚀 Uso

Comando:

```axet.plugin
/axet.skills install NOMBRE_SKILL
```

Ejemplo:

```axet.plugin
/axet.skills install mySkill
```

---

## 🔎 Flujo de instalación

El workflow ejecuta los siguientes pasos:

### 1️⃣ Verificación local

Comprueba si ya existe:

```bash
.axetrules/workflows/NOMBRE_SKILL
```

Si existe:

- Muestra mensaje informativo
- Lista comandos disponibles
- Detiene ejecución

---

### 2️⃣ Verificación remota

Comprueba que existe en el repositorio remoto:

```url
https://raw.githubusercontent.com/mpalancc/aXet.skills/main/NOMBRE_SKILL/NOMBRE_SKILL
```

Si no existe:

- Muestra error indicando que el nombre puede estar mal escrito
- Detiene ejecución

---

### 3️⃣ Descarga del workflow principal

Se guarda en:

```bash
.axetrules/workflows/NOMBRE_SKILL
```

---

### 4️⃣ Procesamiento de manifest.json (opcional)

Si existe:

```bash
NOMBRE_SKILL/manifest.json
```

Se parsea y se procesa la propiedad:

```json
{
  "files": [
    "archivo1.py",
    "config.json"
  ]
}
```

Cada archivo listado será descargado en:

```bash
NTTScripts/NOMBRE_SKILL/
```

Si no existe `manifest.json`, la instalación finaliza correctamente.

---

## 📂 Estructura esperada en el repositorio remoto

```bash
NOMBRE_SKILL/
│
├── NOMBRE_SKILL          ← Workflow YAML principal
├── manifest.json         ← Opcional
├── archivo1.py           ← Opcional
└── archivo2.json         ← Opcional
```

---

## 📁 Estructura generada en el proyecto local

```bash
.axetrules/
└── workflows/
    └── NOMBRE_SKILL

NTTScripts/
└── NOMBRE_SKILL/
    ├── archivo1.py
    └── archivo2.json
```

---

## 🧩 Manifest.json

Formato soportado:

```json
{
  "files": ["file1.ext", "file2.ext"]
}
```

- `files` debe ser un array.
- Los archivos deben existir en la raíz del directorio remoto de la skill.

---

## 🔄 Comandos disponibles

```axet.plugin
/axet.skills install skill
/axet.skills uninstall skill
```

> El comando `uninstall` será implementado en una siguiente versión.

---

## 🏗️ Autor

NTT DATA — GDN-e Spain Booster

---

## 📄 Versión

Workflow Version: 1.0.0
