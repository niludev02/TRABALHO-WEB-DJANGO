from django.shortcuts import render
from .models import Contato
from .forms import FormContato

def contatos(request):
    contatos = Contato.objects.all()
    return render(request, "contatos.html", {'contatos': contatos})

def addContatos(request):
    form = FormContato(request.POST or None, request.FILES or None)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contatos')

    return render(request, "add-contato.html", {'form': form})

def delContatos(request, id_contato):
    contato = Contato.objects.get(id=id_contato)

    contato.delete()
    return redirect('contatos')