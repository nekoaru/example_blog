from django.db import models

# Create your models here.


class Post(models.Model):
    """
    Модель, позволяющая хранить посты блога в базе данных. 
    * `title` - поле заголовка поста, тип `CharField`, транслируемый в столбец `VARCHAR` в SQL
    * `slug` - поле короткой метки, тип `SlugField`, транслируемый в столбец `VARCHAR` в SQL
    * `body` - поле тела поста, тип `TextField`, транслируемый в столбец `Text` в SQL
    """
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title
