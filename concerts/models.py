from django.db import models


# Create your models here.
class Genres(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Genres"


class Typesofplaces(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name_plural = "Typesofplaces"


class Places(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    type = models.ForeignKey(Typesofplaces, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Places"


class Artists(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genres, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Artists"


class Concerts(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date = models.DateTimeField()
    place = models.ForeignKey(Places, on_delete=models.RESTRICT)
    artist = models.ForeignKey(Artists, on_delete=models.RESTRICT, related_name='concerts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Concerts"