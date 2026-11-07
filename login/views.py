from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def perfil(request):
    if request.method == 'POST':
        usuario = request.user
        usuario.first_name = request.POST.get('first_name')
        usuario.last_name = request.POST.get('last_name')
        usuario.email = request.POST.get('email')

        usuario.save()

        return redirect('dashboard')
    return render(request, 'perfil.html')
