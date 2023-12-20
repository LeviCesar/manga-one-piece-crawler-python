from PIL import Image
from pathlib import Path


class Manga:
    def __init__(self, name: str, charpter: int, pages_img: list, ) -> None:
        self._name = name.lower().replace(' ', '_')
        self._charpter = charpter
        self._page = 0
        self._pages_img = pages_img
        self._total_pages = len(pages_img)

    def generate_pdf(self, path: Path = Path('.')) -> bool:
        pdf_path = path.absolute().joinpath('pdf')
        pdf_path.mkdir(parents=True, exist_ok=True)
        
        manga = Image.open(self._pages_img[0]).convert('RGB')
        manga_images = [Image.open(img).convert('RGB') for img in self._pages_img[1:]]
        
        file_pdf = pdf_path.joinpath(f'{self._name}_{self._charpter}.pdf')
        manga.save(
            file_pdf, "PDF", resolution=100.0, save_all=True, append_images=manga_images)

        return file_pdf.exists()
