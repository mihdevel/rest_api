from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def words(request):
  token = request.META['HTTP_AUTHORIZATION']

  # Добавление слов
  if request.method == 'POST':
    word = request.POST['key_word']
    return HttpResponse(request.POST)

  # Получить все слова
  if request.method == 'GET':
    return HttpResponse('request.GET')

def word(request, word_id):
  token = request.META['HTTP_AUTHORIZATION']

  # Удаление слов
  if request.method == 'DELETE':
    return HttpResponse(request.DELETE)
  


def video(request, word_id):
  # token = request.META['HTTP_AUTHORIZATION']

  # Получить список видео
  if request.method == 'GET':

    # Если запрос в интервале времени
    if 'date_gte' in request.GET:
      date_gte = request.GET['date_gte']
      date_lte = request.GET['date_lte']

    # Если запрос на постраничное разбиение
    if 'page' in request.GET:
      page = request.GET['page']
      quantity = request.GET['quantity']
      
    return HttpResponse(request.GET)

    
    
  # return HttpResponse(request)
