from django.forms import ModelForm
from django import forms
from .models import Genres, Artists, Typesofplaces, Places, Concerts



class GenreForm(ModelForm):
    name = forms.TextInput()
    class Meta:
        model = Genres
        fields = ['name']


class ArtistForm(ModelForm):
    class Meta:
        model = Artists
        fields = '__all__'


class TypeofplaceForm(ModelForm):
    class Meta:
        model = Typesofplaces
        fields = '__all__'

class PlaceForm(ModelForm):
    class Meta:
        model = Places
        fields = '__all__'

class ConcertForm(ModelForm):
    class Meta:
        model = Concerts
        fields = '__all__'