from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('qrcode', views.qrGen, name='qr'),
    path('slide/<int:id>', views.slideView, name='slideView'),
    path('slideshow/<int:id>', views.advanceSlideView, name='advanceSlideView')
]