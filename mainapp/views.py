from django.shortcuts import render

def home(request):
    data = {
        'news': "news",
        'title': 'Главная страница'
    }
    return render(request, 'mainapp/home.html', data)

def aboutus(request):
    data = {
        'title': 'О нас'
    }
    return render(request, 'mainapp/aboutus.html', data)