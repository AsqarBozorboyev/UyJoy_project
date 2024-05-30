from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



    def __str__(self):
        return self.name

class Homes(models.Model):

    class Status(models.TextChoices):
        Draft = 'DF', 'Draft'
        Published = 'PB', 'Published'

    class Tariff(models.TextChoices):
        maxsus = 'maxsus'
        orta = "o'rta"
        oddiy = 'oddiy'

    title = models.CharField(max_length=200)
    maydoni = models.CharField(max_length=200)
    xona_soni = models.IntegerField()
    tamiri = models.CharField(max_length=200)
    image = models.ImageField(upload_to='homes/images')
    tafsilotlari = models.CharField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.Draft)
    narxi = models.CharField(max_length=50, blank=True)
    manzil = models.CharField(max_length=150, blank=True)
    tarifi = models.CharField(choices=Tariff.choices, default=Tariff.oddiy, null=True, blank=True, max_length=6)
    tel = models.CharField(max_length=9, blank=True)

    class Meta:
        ordering = ['-publish_time']

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()


    def __str__(self):
        return self.name




class Comment(models.Model):
    homes = models.ForeignKey(Homes, on_delete=models.CASCADE,
                              related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_time']

    def __str__(self):
        return f"Comment - {self.body} by {self.user}"
