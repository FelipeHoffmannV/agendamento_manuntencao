from django.urls import path
from .views import ClientCreateView


urlpatterns = [
    path('', ClientCreateView.as_view(), name='cadastro_cliente'),
]