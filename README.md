### Hexlet tests and linter status:
[![Actions Status](https://github.com/ByronDakFox/python-project-174/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ByronDakFox/python-project-174/actions)

[![Maintainability](https://qlty.sh/gh/ByronDakFox/projects/python-project-174/maintainability.svg)](https://qlty.sh/gh/ByronDakFox/projects/python-project-174)

[![Code Coverage](https://qlty.sh/gh/ByronDakFox/projects/python-project-174/coverage.svg)](https://qlty.sh/gh/ByronDakFox/projects/python-project-174)

# Gendiff

![CI](https://github.com/ByronDakFox/hexlet-ci-app/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

Herramienta para comparar archivos de configuración y mostrar sus diferencias de forma clara y estructurada. Compatible actualmente con **JSON**, extendible a más formatos.

---

## 📋 Requisitos

* Python 3.10 o superior
* Poetry instalado
* Sistema operativo compatible (Linux, macOS o Windows)

## 🚀 Instalación

Clona el repositorio:

```bash
git clone https://github.com/ByronDakFox/hexlet-ci-app.git
cd hexlet-ci-app
```

Instala dependencias con Poetry:

```bash
poetry install
```

---

## 🚀 Uso desde la línea de comandos

### Formato por defecto (stylish)

```bash
gendiff file1.json file2.json
```

Salida:

```text
{
  common: {
    + follow: false
      setting1: Value 1
    - setting2: 200
    + setting3: null
  }
}
```

---

### 📄 Formato Plain

```bash
gendiff --format plain file1.json file2.json
```

Salida:

```text
Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
```

📌 Notas:

* Valores complejos se muestran como `[complex value]`
* Se usa la **ruta completa** de la propiedad (`a.b.c`)

---

### 🧾 Formato JSON

```bash
gendiff --format json file1.json file2.json
```

Salida (ejemplo):

```json
[
  {
    "key": "common",
    "type": "nested",
    "children": [
      {
        "key": "follow",
        "type": "added",
        "value": false
      }
    ]
  }
]
```

📌 Este formato es ideal para integraciones con otras aplicaciones o APIs.

---

## 🧪 Tests

Ejecutar pruebas automáticas:

```bash
poetry run pytest
```

Incluye pruebas para:

* Archivos iguales
* Claves agregadas / eliminadas / modificadas
* Estructuras anidadas
* Formatos `stylish`, `plain` y `json`

---

## 🛠️ Arquitectura

El proyecto está dividido en **dos responsabilidades principales**:

1. **Construcción del diff (AST)**

   * `diff_builder.py`
   * Detecta cambios: added, removed, updated, nested, unchanged

2. **Formateo de salida**

   * `formatters/`
   * Cada formato es independiente y reutilizable

Esto permite agregar nuevos formatos sin modificar la lógica principal.

---

---

## 📦 Uso como biblioteca en Python

Puedes usar la función `generate_diff()` directamente en tu código:

```python
from gendiff import generate_diff

diff = generate_diff("file1.json", "file2.json")
print(diff)
```

Salida:

```
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

---

## 📁 Estructura del proyecto

```
gendiff/
├── pyproject.toml
├── README.md
├── gendiff/
│   ├── __init__.py
│   ├── generate_diff.py
│   ├── diff_builder.py
│   ├── parser.py
│   ├── scripts/
│   │   ├── __init__.py
│   │   └── gendiff.py
│   └── formatters/
│       ├── __init__.py
│       ├── stylish.py
│       ├── plain.py
│       └── json.py
├── tests/
│   ├── __init__.py
│   ├── test_generate_diff.py
│   └── fixtures/
│       ├── file1.json
│       ├── file2.json
│       ├── file1.yaml
│       └── file2.yaml

```

---

## 🎥 Demostración (Asciinema)

* ✅ Mostrar ayuda

Ejemplo:

```
[![asciicast](https://asciinema.org/a/766012.svg)](https://asciinema.org/a/766012)
```

* ✅ Formato Plain

Ejemplo:

```
[![asciicast](https://asciinema.org/a/766039.svg)](https://asciinema.org/a/766039)
```

* ✅ Formato JSON

Ejemplo:

```
[![asciicast](https://asciinema.org/a/766060.svg)](https://asciinema.org/a/766060)
```

* ✅ Formato por defecto

Ejemplo:

```
[![asciicast](https://asciinema.org/a/766077.svg)](https://asciinema.org/a/766077)
```
---

## 📌 Características

* ✅ Soporta archivos **JSON** y **YAML** (`.json`, `.yml`, `.yaml`)
* ✅ Comparación **recursiva** (estructuras anidadas)
* ✅ Múltiples formatos de salida:

  * `stylish` (por defecto)
  * `plain`
  * `json`
* ✅ CLI fácil de usar
* ✅ Arquitectura modular y extensible
---

## ✨ Autor

Proyecto educativo — inspirado en prácticas profesionales de desarrollo en Python por **Byron Ramirez**.