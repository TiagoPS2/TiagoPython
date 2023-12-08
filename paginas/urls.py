from django.urls import path, include
from paginas.views import inicio


urlpatterns = [
    path('',inicio, name="inicio"),
]
