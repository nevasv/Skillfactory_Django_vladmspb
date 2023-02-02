# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

UserLoginDict = {
    "veniki": 'ООО"Веники" page2',
    "valenki": 'Валенки" page3',
    "vostok": 'ООО"Восток" page4',
}


def pages_view(request):
    return render(request, 'flatpages/default.html')


def static_pages(request, partner_pages: str):
    user_login = str(UserLoginDict.get(partner_pages, None))
    user_login = {'user_login': user_login}
    if user_login:
        return render(request, 'flatpages/contact_page.html', user_login)
    else:
        return HttpResponseNotFound(f'Неизвестный логин партнёра : {user_login} ')


def static_pages_id(request, partner_pages: int):
    return HttpResponse(f" Введено число {partner_pages} , открытие страниц по ID пока не работает")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

