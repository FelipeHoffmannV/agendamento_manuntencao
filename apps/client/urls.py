from django.urls import path
from .views import ClientCreateView, ClientLoginView
from django.contrib.auth import views as auth_views

app_name = 'client'
urlpatterns = [
 
    path('', ClientCreateView.as_view(), name='cadastro_cliente'),
    

    path('login/', ClientLoginView.as_view(), name='login'),

    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
