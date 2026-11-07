from django.urls import path
from . import views

urlpatterns = [
    path("", views.contatos, name="contatos"),
    path("add-contato", views.addContatos, name="addContatos"),
    path("del-contato/<int:id_contato>", views.delContatos, name="delContatos")
]