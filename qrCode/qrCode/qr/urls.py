from django.urls import path
from .views import create_qr, home_page

urlpatterns = [
    # path('menu', menu, name="menu"),
    path('', home_page, name="home"),
    path('create', create_qr, name="create"),
]
