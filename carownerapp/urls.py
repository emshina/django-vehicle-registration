from carownerapp import views
from django.urls import path

urlpatterns = [
    path("", views.carowner),
    path('insertuser/',views.insertuser),
]