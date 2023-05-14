from carownerapp import views
from django.urls import path

urlpatterns = [
    path("", views.carowner),
    path('insertuser/',views.insertuser),
    path('records/',views.display),
    path('list/', views.display2),
    path('signup/', views.signup),
    path('login/', views.login),
]