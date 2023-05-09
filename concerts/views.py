from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Concerts, Places, Artists, Genres, Typesofplaces


# Create your views here.
'''class IndexView(generic.ListView):
    template_name = 'concerts/index.html'
    context_object_name = "concerts_list"

    def get_queryset(self):
        return Concerts.objects.all().order_by("date")

class DetailView(generic.DetailView):
    model = Concerts
    template_name = "concerts/detail.html"
'''
def index(request):
    concerts_list = Concerts.objects.all().order_by("date")
    artists_list = Artists.objects.all()
    places_list = Places.objects.all()
    genres_list = Genres.objects.all()
    typesofplaces_list = Typesofplaces.objects.all()
    context = {
            'concerts_list': concerts_list,
            'artists_list': artists_list,
            'places_list': places_list,
            'genres_list': genres_list,
            'typesofplaces_list': typesofplaces_list,
            }
    return render(request, 'concerts/index.html', context)


def detail(request, concert_id):
    concert = get_object_or_404(Concerts, pk=concert_id)
    artist = get_object_or_404(Artists, pk=concert.artist_id)
    place = get_object_or_404(Places, pk=concert.place_id)
    typeofplace = get_object_or_404(Typesofplaces, pk=place.type_id)
    context = {
        'concert': concert,
        'artist': artist,
        'place': place,
        'typeofplace': typeofplace,
    }
    return render(request, 'concerts/detail.html', context)