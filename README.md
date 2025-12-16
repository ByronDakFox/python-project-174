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

## 🛠 Uso desde la terminal

### Mostrar ayuda

```bash
poetry run gendiff -h
```

Salida:

```
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.
```

### Comparar dos archivos JSON

```bash
poetry run gendiff file1.json file2.json
```

Ejemplo de salida:

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
│
├── __init__.py
├── generate_diff.py
└── scripts/
    └── gendiff.py
```

---

## 🎥 Demostración (Asciinema)

*(Insertar grabación aquí cuando esté lista)*

Ejemplo:

```
[![asciicast](https://asciinema.org/a/123456.svg)](https://asciinema.org/a/123456)
```

---

## 📘 Características

* Comparación clara y ordenada
* Salida estilo *stylish*
* Compatible como CLI y como librería
* Extensible a múltiples formatos (JSON, YAML, etc.)

---

## 📝 Licencia

Proyecto distribuido bajo licencia **MIT**.
