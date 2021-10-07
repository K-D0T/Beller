from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('artwork', views.artwork, name='artwork'),
    path('artwork/view/<int:id>/', views.ViewArtWork, name='ViewArtWork'),
    ]