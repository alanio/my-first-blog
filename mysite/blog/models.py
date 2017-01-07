from django.db import models
from django.utils import timezone
from redactor.fields import RedactorField
import datetime

class Post(models.Model):
    author = models.ForeignKey('auth.User', verbose_name='Autor')
    title = models.CharField('Título',max_length=200)
    #text = models.TextField()
    text = RedactorField('Texto')
    created_date = models.DateTimeField('Criado em',
            default=timezone.now)
    published_date = models.DateTimeField('Publicado em',
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title