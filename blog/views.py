from django.shortcuts import render
from django.http import HttpResponse

news = [
    {
        'title': 'Наша первая запись',
        'text': 'Просто большой текст для 1 записи',
        'date': '1 Января 2019',
        'avtor': 'Георгий'
    },
    {
        'title': 'Наша вторая запись запись',
        'text': 'Просто большой текст для 2 записи',
        'date': '1 Января 2019',
        'avtor': 'Джон'
    }
]


def home(request):
    data = {
        'news': news,
        'title': 'Главная страница блога'
    }
    return render(request, 'blog/home.html', data)


def contacti(request):
    return render(request, 'blog/contacti.html')
