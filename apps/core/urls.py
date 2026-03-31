from django.urls import path
from .views import home, ServicoCreateView


app_name = 'core'

urlpatterns = [
    path('home/', view=home, name='home'),
    path('agendar/', ServicoCreateView.as_view(), name='agendar')
]