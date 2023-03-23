from django.urls import path
from .import views
urlpatterns=[
    path('menu/', views.showmenu.as_view()),
    path('menu/<int:pk>', views.MenuItemByID.as_view()),
    path('booking/', views.BookingsDone.as_view()),
    path('booking/<str:Name>',views.MyBooking.as_view()),
]