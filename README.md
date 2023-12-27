# manga-one-piece-crawler-python
![Static Badge](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Python-3.8%7C3.9%7C3.10-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Requests-2.31-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/Pillow-10.1.0-blue?style=for-the-badge)
![Static Badge](https://img.shields.io/badge/beautifulsoup4-4.12.2-blue?style=for-the-badge)

# Sobre o projeto

Este projeto é um crawler que foi desenvolvido utilizando python para captura de imagens e conversão em pdf. 

O crawler consiste em consultar as imagens do manga <a href="https://onepieceex.net/">One Piece</a>, realizar o download delas e armazena-las em pastas organizadas em uma estrutura de captulos. Após ser realizada a captura de todas as imagens referentes ao captulo é realizado um tratamento das imagens e a conversão das mesmas em um arquivo PDF.


## Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [x] Captura das imagens do manga
- [x] Tratamento e conversão de imagens

# Como executar o projeto
Pré-Requisito: Python 3.8+

```bash
git clone https://github.com/LeviCesar/etl-manga.git

cd manga-one-piece-crawler-python

python3 -m virtualenv env
source env/bin/activate
python -m pip install -r requirements.txt

python main.py <numCaptuloInicio> <numCaptuloFim>
```


## 📫 Contribuindo para manga-one-piece-crawler-python

Para contribuir com manga-one-piece-crawler-python, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <nome_do_projeto> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).


## 🤝 Autores & Colaboradores

<table>
  <tr>
    <td align="center">
      <a href="https://www.linkedin.com/in/levi-cesar-lima/" title="LinkedIn">
        <img src="https://avatars.githubusercontent.com/u/57629756?v=4" width="100px;" alt="Foto do Iuri Silva no GitHub"/><br>
        <sub>
          <b>Levi César</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
