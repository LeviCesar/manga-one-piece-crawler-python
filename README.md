# Crawler Manga
![Static Badge](https://img.shields.io/badge/license-MIT-blue)
![Static Badge](https://img.shields.io/badge/Python-3.8%7C3.9%7C3.10-blue)
![Static Badge](https://img.shields.io/badge/Requests-2.31-blue)
![Static Badge](https://img.shields.io/badge/Pillow-10.1.0-blue)
![Static Badge](https://img.shields.io/badge/beautifulsoup4-4.12.2-blue)

# Sobre o projeto

ETL Manga é um projeto de automação que segue os principios básicos da engenharia de dados, o ETL (Extração, Transformação e Armazenamento). 

A automação consiste em capturar as imagens das páginas do manga One Piece separadas por captulo. Após a captura das imagens é realizado um pós processamento das imagens para unifica-las e salvar em um arquivo pdf. A automação foi realizada do site **https://onepieceex.net/**.

# Como executar o projeto
Pré-Requisito: Python 3.8+

```bash
git clone https://github.com/LeviCesar/etl-manga.git

cd etl-manga

python3 -m virtualenv env
source env/bin/activate
python -m pip install -r requirements.txt

python main.py <numCaptuloInicio> <numCaptuloFim>
```

# Autores

Levi Lima

https://www.linkedin.com/in/levi-cesar-lima/