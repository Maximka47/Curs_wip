from django.db import models
from django.urls import reverse
from django.utils import timezone

class Ticket(models.Model):
    name = models.CharField(verbose_name="Вид квитка:", max_length=100)
    price = models.PositiveIntegerField(verbose_name="Ціна квитка:")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Квиток"
        verbose_name_plural = "Квитки"

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва:")
    description = models.TextField(blank=True, null=True, verbose_name="Опис:")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

class Actor(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ім'я:")
    age = models.PositiveSmallIntegerField(default=0, verbose_name="Вік:")
    description = models.TextField(blank=True, null=True, verbose_name="Опис:")
    image = models.ImageField(upload_to="actors/", verbose_name="Зображення:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Актори і режисери"
        verbose_name_plural = "Актори і режисери"

class Genre(models.Model):
    name = models.CharField(max_length=50, verbose_name="Назва:")
    description = models.TextField(blank=True, null=True, verbose_name="Опис:")
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"

class Movie(models.Model):
    title = models.CharField(max_length=50, verbose_name="Назва фільму:", unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name="URL:")
    age = models.PositiveSmallIntegerField(verbose_name="Обмеження у віці:")
    year = models.DateField(default=timezone.now, verbose_name="Дата виходу:")
    video = models.FileField(upload_to="main_video", verbose_name="Трейлер фільму:")
    date = models.DateTimeField(default=timezone.now, verbose_name="Початок фільму:")
    runtime = models.PositiveSmallIntegerField(default=0, verbose_name="Тривалість фільму:", help_text="Вказувати суму в гривнях:")
    poster = models.ImageField(upload_to="main_img", blank=True, null=True, verbose_name="Постер:")
    img = models.ImageField(upload_to="main_img", blank=True, null=True, verbose_name="Прев'ю фільму:")
    description = models.TextField(blank=True, null=True, verbose_name="Опис фільму:")
    country = models.CharField(max_length=100, verbose_name="Країна:")
    movie_rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, verbose_name="Рейтинг фільму:")
    world_premiere = models.DateField(default=timezone.now, verbose_name="Світова прем'єра:")
    budget = models.PositiveIntegerField(default=0, verbose_name="Бюджет:", help_text="Вказувати суму в гривнях:")
    draft = models.BooleanField(verbose_name="Чорновик:", default=False)

    ticket = models.OneToOneField(Ticket, verbose_name="Квитки:", related_name="film_tikets", on_delete=models.SET_NULL, null=True)
    directors = models.ManyToManyField(Actor, verbose_name="Режисер", related_name="film_director")
    actors = models.ManyToManyField(Actor, verbose_name="Актор", related_name="film_actor")
    genre = models.ManyToManyField(Genre, verbose_name="Назва жанру:", related_name="film_genre")
    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.SET_NULL, null=True, related_name="film_category")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"

class MovieShots(models.Model):
    title = models.CharField(verbose_name="Заголовок:", max_length=100)
    description = models.TextField(verbose_name="Опис:")
    image = models.ImageField(verbose_name="Зображення:", upload_to="movie_shots/")
    movie = models.ForeignKey(Movie, verbose_name="Фільм:", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадр з фільма"
        verbose_name_plural = "Кадри з фільму"

class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0, verbose_name="Значення:")

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Зірка рейтингу"
        verbose_name_plural = "Зірки рейтингу"

class Rating(models.Model):
    ip = models.CharField(max_length=15, verbose_name="IP-адреса:")
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="Зірка")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Фільм:", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Reviews(models.Model):
    email = models.EmailField(verbose_name="Електронна пошта:")
    name = models.CharField(max_length=100, verbose_name="Ім'я:")
    text = models.TextField(max_length=5000, verbose_name="Повідомлення")
    parent = models.ForeignKey('self', verbose_name="Батько", on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name="Фільм", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Відгук"
        verbose_name_plural = "Відгуки"
