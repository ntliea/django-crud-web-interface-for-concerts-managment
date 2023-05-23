from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import GenreForm, ArtistForm, TypeofplaceForm, PlaceForm, ConcertForm
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

def db_info(request):
    return render(request, 'concerts/dbinfo.html')

def addGenre(request):
    form = GenreForm()
    if request.POST:
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
        #return HttpResponseRedirect(reverse("concerts:index"))
        #return redirect(index)
    genres_list = Genres.objects.all()
    context = {'form': form, 'genres_list': genres_list}
    return render(request, 'concerts/create_genre_form.html', context)


def updateGenre(request, genre_id):
    genre = Genres.objects.get(id=genre_id)
    form = GenreForm(instance=genre)
    if request.POST:
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
        # return HttpResponseRedirect(reverse("concerts:add_genre"))
        return redirect('concerts:add_genre')
    context = {'form': form, 'genre': genre}
    return render(request, 'concerts/update_genre_form.html', context)

def deleteGenre(request, genre_id):
    genre = Genres.objects.get(id=genre_id)
    if request.POST:
        genre.delete()
        return redirect('concerts:add_genre')
    context = {'genre': genre}
    return render(request, 'concerts/delete_genre_form.html', context)



def addArtist(request):
    form = ArtistForm()
    if request.POST:
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
        #return HttpResponseRedirect(reverse("concerts:index"))
        #return redirect(index)
    artists_list = Artists.objects.all()
    context = {'form': form, 'artists_list': artists_list}
    return render(request, 'concerts/create_artist_form.html', context)

def updateArtist(request, artist_id):
    artist = Artists.objects.get(id=artist_id)
    form = ArtistForm(instance=artist)
    if request.POST:
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
        # return HttpResponseRedirect(reverse("concerts:add_genre"))
        return redirect('concerts:add_artist')
    context = {'form': form, 'artist': artist}
    return render(request, 'concerts/update_artist_form.html', context)

def deleteArtist(request, artist_id):
    artist = Artists.objects.get(id=artist_id)
    if request.POST:
        artist.delete()
        return redirect('concerts:add_artist')
    context = {'artist': artist}
    return render(request, 'concerts/delete_artist_form.html', context)



def addTypeofplace(request):
    form = TypeofplaceForm()
    if request.POST:
        form = TypeofplaceForm(request.POST)
        if form.is_valid():
            form.save()
    typesofplaces_list = Typesofplaces.objects.all()
    context = {'form': form, 'typesofplaces_list': typesofplaces_list}
    return render(request, 'concerts/create_typeofplace_form.html', context)

def updateTypeofplace(request, typeofplace_id):
    typeofplace = Typesofplaces.objects.get(id=typeofplace_id)
    form = TypeofplaceForm(instance=typeofplace)
    if request.POST:
        form = TypeofplaceForm(request.POST, instance=typeofplace)
        if form.is_valid():
            form.save()
        return redirect('concerts:add_typeofplace')
    context = {'form': form, 'typeofplace': typeofplace}
    return render(request, 'concerts/update_typeofplace_form.html', context)

def deleteTypeofplace(request, typeofplace_id):
    typeofplace = Typesofplaces.objects.get(id=typeofplace_id)
    if request.POST:
        typeofplace.delete()
        return redirect('concerts:add_typeofplace')
    context = {'typeofplace': typeofplace}
    return render(request, 'concerts/delete_typeofplace_form.html', context)



def addPlace(request):
    form = PlaceForm()
    if request.POST:
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
    places_list = Places.objects.all()
    context = {'form': form, 'places_list': places_list}
    return render(request, 'concerts/create_place_form.html', context)

def updatePlace(request, place_id):
    place = Places.objects.get(id=place_id)
    form = PlaceForm(instance=place)
    if request.POST:
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
        return redirect('concerts:add_place')
    context = {'form': form, 'place': place}
    return render(request, 'concerts/update_place_form.html', context)

def deletePlace(request, place_id):
    place = Places.objects.get(id=place_id)
    if request.POST:
        place.delete()
        return redirect('concerts:add_place')
    context = {'place': place}
    return render(request, 'concerts/delete_place_form.html', context)




def addConcert(request):
    form = ConcertForm()
    if request.POST:
        form = ConcertForm(request.POST)
        if form.is_valid():
            form.save()
    concerts_list = Concerts.objects.all()
    context = {'form': form, 'concerts_list': concerts_list}
    return render(request, 'concerts/create_concert_form.html', context)

def updateConcert(request, concert_id):
    concert = Concerts.objects.get(id=concert_id)
    form = ConcertForm(instance=concert)
    if request.POST:
        form = ConcertForm(request.POST, instance=concert)
        if form.is_valid():
            form.save()
        return redirect('concerts:add_concert')
    context = {'form': form, 'concert': concert}
    return render(request, 'concerts/update_concert_form.html', context)

def deleteConcert(request, concert_id):
    concert = Concerts.objects.get(id=concert_id)
    if request.POST:
        concert.delete()
        return redirect('concerts:add_concert')
    context = {'concert': concert}
    return render(request, 'concerts/delete_concert_form.html', context)