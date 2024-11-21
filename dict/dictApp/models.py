from django.db import models
from django.core.validators import RegexValidator

class Word(models.Model):
    only_letters = RegexValidator(r'^[a-zA-Zа-яА-ЯЁё]*$', 'Для ввода разрешены только буквы.')
    word = models.CharField(max_length=50, blank=False, validators=[only_letters], unique=True)
    translation = models.CharField(max_length=50, blank=False, validators=[only_letters], unique=True)

    def __str__(self):
        return self.word