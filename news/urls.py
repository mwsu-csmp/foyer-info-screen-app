from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('qrcode/<int:id>', views.qrGen, name='qr'),
    path('slideshow/<int:id>', views.slideshowView, name='slideshowView'),
    path('advslide/<int:id>', views.advanceSlideView, name='advanceSlideView'),
    path('slide/<int:id>', views.slideView, name='singleSlideView')
]