from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
from .models import TvShow


def filmListView(request):
    film_value = models.TvShow.objects.all()
    html_name = 'films/films_list.html'
    context = {
        'film_key': film_value,
    }
    return render(request, html_name, context)


def filmDetailView(request, id):
    film_id = get_object_or_404(models.TvShow, id=id)
    html_name = 'films/film_detail.html'
    context = {
        'film_id': film_id,
    }
    return render(request, html_name, context)


def createFilmView(request):
    method = request.method
    if method == "POST":
        form = forms.TVShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Фильм успешно добавлен')
    else:
        form = forms.TVShowForm()

    return render(request, 'films/create_film.html', {'form': form})


def deleteFilmView(request, id):
    film_id = get_object_or_404(models.TvShow, id=id)
    film_id.delete()
    return HttpResponse('Фильм успешно удален')


def updateFilmView(request, id):
    film_id = get_object_or_404(models.TvShow, id=id)
    if request.method == 'POST':
        form = forms.TVShowForm(instance=film_id, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Фильм изменен')

    else:
        form = forms.TVShowForm(instance=film_id)
    return render(request, 'films/update_film.html',
                  {
                      'form': form,
                      'film_id': film_id
                  }
                  )


def movie_schedule(request):
    tvshows = TvShow.objects.all()
    return render(request, 'films/ab.html', {'tvshows': tvshows})
