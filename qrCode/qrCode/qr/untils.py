from pyqrcode import create
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

class qrCode():
    def __init__(self, url, img_name):
        self.url = url
        self.img_name = img_name

    def create_img(self):
        embedded_qr = create(self.url)
        embedded_qr.png(self.img_name, scale=7)

def img_cleanner(image_path):
    image_clean_path = BASE_DIR/image_path
    os.remove(image_clean_path)
