from bs4 import BeautifulSoup
from pathlib import Path
import requests
import json
import re


class OnePiece:

    def __init__(self) -> None:
        self.base_headers = {
            # windows agents
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            # linux agent
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }
        self.url = "https://onepieceex.net/"


    def get_pages(self, charpter: int) -> list:
        response = requests.get(
            url=self.url + f"mangas/leitor/{charpter}",
            headers=self.base_headers
        )

        soup = BeautifulSoup(response.text, "html.parser")
        dict_img = self.get_images(soup)

        if dict_img:
            for page, img_link in dict_img.items():
                yield page, self.url + img_link, img_link.split('.')[1]
    
    
    @staticmethod
    def get_images(html_text: BeautifulSoup) -> dict:
        script_list = html_text.find_all("script", type="text/javascript")

        for script in script_list:
            pattern = re.compile(r'paginasLista = ("\{(?:[^{}])*\}")')
            match = pattern.findall(script.text)
        
            if match:
                try:
                    dict_img = json.loads(json.loads(match[0]))
                    if "1" in dict_img:
                        return dict_img        
                    else:
                        pass
                
                except Exception as e:
                    print(e)
                    pass

        return None


    def download_page_image(
        self, 
        url_image: str, 
        charpter: int, 
        page: int, 
        ext_img: str = 'jpg', 
        path: Path = Path('.')) -> Path:
        response = requests.get(
            url=url_image,
            headers=self.base_headers,
            stream=True
        )
        
        if response.status_code == 200:
            p = path.absolute().joinpath(f"images/{charpter}/")
            p.mkdir(parents=True, exist_ok=True)
            file_img = p.joinpath(f'{page}.{ext_img}')
            
            with file_img.open("wb") as f:
                f.write(response.content)

            assert p.exists()
            
            return file_img

    
    def get_last_charpter(self) -> int:
        return ...
