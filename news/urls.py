from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('qrcode', views.qrGen, name='qr'),
    path('slideshow', views.slideView, name='slideView'),
    path('slide/<int:id>', views.advanceSlideView, name='advanceSlideView')
]