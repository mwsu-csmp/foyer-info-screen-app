from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('qrcode', views.qrGen, name='qr'),
    path('newsArticle', views.newsArticle, name='newsArticle'),
    path('slide/<str:id>', views.slideView, name='slideView'),
]