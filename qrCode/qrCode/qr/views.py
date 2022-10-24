from django.shortcuts import render
from django.utils.text import slugify

from .untils import qrCode

import base64


# Create your views here.

def home_page(request):
    return render(request, "home.html")


def create_qr(request):
    url = request.POST['url']
    name = slugify(url)
    name += ".png"
    new_qr = qrCode(url, name)
    load_image = new_qr.create_img()
    with open(name, "rb") as image_file:
        image_data = base64.b64encode(image_file.read()).decode('utf-8')
    return render(request, 'home.html', {'image': image_data})
