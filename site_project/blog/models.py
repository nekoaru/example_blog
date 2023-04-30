from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """
    Модель, позволяющая хранить посты блога в базе данных. 
    * `title` - поле для заголовка поста, тип `CharField`, транслируемый в столбец `VARCHAR` в SQL
    * `slug` - поле для короткой метки, тип `SlugField`, транслируемый в столбец `VARCHAR` в SQL
    * `body` - поле для тела поста, тип `TextField`, транслируемый в столбец `Text` в SQL
    * `publish` - поле для даты и времени публикации поста, тип `DateTimeField`, транслируемый в `DATETIME` в SQL
    * `created` - поле для даты и времени создания поста , тип `DateTimeField`, транслируемый в `DATETIME` в SQL
    * `updated` - поле для даты и времени обновления поста , тип `DateTimeField`, транслируемый в `DATETIME` в SQL
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
