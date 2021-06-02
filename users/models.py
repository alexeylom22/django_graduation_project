from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'

    def save(self, *args, **kwargs):
        super().save()


class Person(models.Model):

    name = models.CharField(max_length=100)
    short_link = models.CharField(max_length=100, unique=True)
    full_link = models.CharField(max_length=250)

    def __str__(self):
        return f'Ссылка пользователя {self.name}'

    class Meta:
        verbose_name = 'Ссылки'
        verbose_name_plural = 'Ссылки'

    def clean(self):
        cleaned_data = super().clean(self)
        if User.objects.filter(short_link=cleaned_data.get('short_link')).exists():
            self.fields.add_error('short_link', "Эта почта уже зарегистрированна")
        return cleaned_data