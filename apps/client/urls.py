from django.urls import path
from .views import ClientCreateView
from .views import index_

urlpatterns = [
    path('', ClientCreateView.as_view(), name='cadastro_cliente'),
    path('home/', view=index_, name='home')
]