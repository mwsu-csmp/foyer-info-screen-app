from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('qrcode', views.qrGen, name='qr'),
    path('slideshow', views.slideshowView, name='slideshowView'),
    path('slide/<int:id>', views.slideView, name='singleSlideView')
]