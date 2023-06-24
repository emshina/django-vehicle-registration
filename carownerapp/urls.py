from carownerapp import views
from django.urls import path


urlpatterns = [
    path("", views.carowner),
    path('registration/',views.registration),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
  
    

]