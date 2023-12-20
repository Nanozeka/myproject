from django.shortcuts import render, redirect
from .forms import ServiceForm


def service_view(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()  # Этот метод сохраняет данные в базе данных
            return redirect('success_page')  # Перенаправьте пользователя на страницу успешного сохранения

    else:
        form = ServiceForm()

    return render(request, 'main/index.html', {'form': form})

def index(request):
    return render(request, 'main/index.html')

def success_page(request):
    return render(request, 'main/success_page.html')

