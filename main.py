from crawlers.one_piece import OnePiece
from tools.manga import Manga
from pathlib import Path
import sys


def run(fist_charpter: int = 1, last_charpter: int = ...) -> None:
    manga_op = OnePiece()
    path = Path('.').absolute().joinpath('media/one_piece')
    
    for charpter in range(fist_charpter, last_charpter):
        manga_images = []
        
        print(f'Start download charpter {charpter}... ')
        for page, url_image, extension in manga_op.get_pages(charpter):
            print(f'page = {page}', end='\r')
            path_img = manga_op.download_page_image(
                url_image=url_image, charpter=charpter, page=page, ext_img=extension, path=path)
            manga_images.append(path_img)

        print(f'Finish download charpter {charpter}\n')
        
        path_charpter = path.joinpath(f'images/{charpter}')

        if path_charpter.exists():
            manga = Manga(pages_img=manga_images, charpter=charpter, name='one piece')
            assert manga.generate_pdf(path=path), 'Manga generate pdf fail!'


if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2])