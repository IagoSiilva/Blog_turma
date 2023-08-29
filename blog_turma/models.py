from django.db import models
from django.conf import settings
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    title = models.CharField(max_length=200, verbose_name= 'Título')
    text = RichTextUploadingField()
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Criado em')
    published_date = models.DateField(blank=True, null=True, verbose_name='Publicado em')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title
