from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    """
    Модель, позволяющая хранить посты блога в базе данных. 
    * `title` - поле для заголовка поста, тип `CharField`, транслируемый в столбец `VARCHAR` в SQL
    * `slug` - поле для короткой метки, тип `SlugField`, транслируемый в столбец `VARCHAR` в SQL
    * `author` - поле для взаимосвязи один-ко-многим (один автор для множества постов), тип `ForeignKey`, внешний ключ в SQL
    * `body` - поле для тела поста, тип `TextField`, транслируемый в столбец `Text` в SQL
    * `publish` - поле для даты и времени публикации поста, тип `DateTimeField`, транслируемый в `DATETIME` в SQL
    * `created` - поле для даты и времени создания поста , тип `DateTimeField`, транслируемый в `DATETIME` в SQL
    * `updated` - поле для даты и времени обновления поста , тип `DateTimeField`, транслируемый в `DATETIME` в SQL
    * `status` - поле для статуса поста, тип `CharField`, транслируемый в столбец `VARCHAR` в SQL
    """
    class Status(models.TextChoices):
        """
        Класс, определящий статус поста (enum-класс)
        * DRAFT - статус черновика
        * PUBLISHED - статус опубликованного поста
        """
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    class Meta:
        """
        Класс, определяющий метаданные модели
        * `ordering` - атрибут для сортировки результатов, по умолчанию равен `-publish` (по убыванию)
        * `indexes` - атрибут для хранения индексов базы данных
        """
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
    
    def __str__(self) -> str:
        return self.title
