from django.urls import path
from . import views
from .views import booking_form, create_reservation


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),  
    path('bookings', views.bookings, name='bookings'), 
    path('booking/', booking_form, name='booking_form'),
    path('reservation/create/', create_reservation, name='create_reservation'),
]