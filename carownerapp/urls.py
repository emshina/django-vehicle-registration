from carownerapp import views
from django.urls import path

urlpatterns = [
    path("", views.carowner),
    path('registration/',views.registration),
#     path('records/',views.display),
    # path('list/', views.display2),
    path('signup/', views.signup),
    path('login/', views.login),
#     path('police/', views.my_custom_sql),
]