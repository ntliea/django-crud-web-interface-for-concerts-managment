from django.urls import path

from . import views


app_name = 'concerts'
urlpatterns = [
    #path("", views.IndexView.as_view(), name="index"),
    path('', views.index, name='index'),
    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path('<int:concert_id>/', views.detail, name='detail'),
]