# platzi-embeddings

[![License](https://img.shields.io/badge/license-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)
[![Platform](https://img.shields.io/badge/platform-MacOS%20%7C%20Linux%20%7C%20Windows-lightgrey)]()
[![Conda](https://img.shields.io/badge/Conda-environment-success)](https://docs.conda.io/)

---

### 🌐 Proyecto: Buscador de Películas con Búsqueda Semántica

Este proyecto forma parte del curso de Embeddings de Platzi. Se implementa un sistema de búsqueda semántica de películas utilizando embeddings generados por `sentence-transformers`, una base de datos vectorial con Pinecone y una interfaz gráfica con Gradio.

---

### 📊 Características

* Conversión de descripciones de películas y consultas en vectores usando embeddings.
* Indexación y recuperación semántica eficiente con Pinecone.
* Interfaz interactiva usando Gradio.
* Filtros por género, puntuación mínima y top-k resultados.

---

### 📁 Estructura del Proyecto

```
platzi-embeddings/
├── data/                  # Datos de entrada
├── models/                # Modelos o embeddings guardados
├── notebooks/             # Notebooks de desarrollo
├── references/            # Documentación o papers
├── src/                   # Código fuente si se empaqueta
├── .env                   # Variables de entorno (API keys, etc)
├── config.py              # Configuraciones generales
├── paths.py               # Rutas absolutas centralizadas
├── environment.yml        # Entorno Conda
├── pyproject.toml         # Configuración del proyecto
└── README.md              # Este archivo
```

---

### 🚀 Instalación

1. **Clona el repositorio:**

```bash
git clone https://github.com/jasonssdev/platzi-embeddings.git
cd platzi-embeddings
```

2. **Crea el entorno con Conda:**

```bash
conda env create -f environment.yml
conda activate emb-py3.11
```

3. **Agrega tus variables de entorno (.env):**

```
PINECONE_API_KEY=tu_api_key
OPENAI_API_KEY=tu_api_key
```

---

### 💡 Tecnologías Usadas

* [Gradio](https://gradio.app/) - Interfaz web
* [Pinecone](https://www.pinecone.io/) - Almacenamiento vectorial
* [sentence-transformers](https://www.sbert.net/) - Generación de embeddings
* [Conda](https://docs.conda.io/) - Manejo de entornos
* [Python 3.11+](https://www.python.org/)

---

### 📄 Licencia

Este proyecto está licenciado bajo los términos de la licencia Apache 2.0. Consulta el archivo [LICENSE](LICENSE) para más información.

---

### 🙌 Autor

**Jason (jasonssdev)**

* GitHub: [@jasonssdev](https://github.com/jasonssdev)

