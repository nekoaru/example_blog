from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Класс для отображения информации о модели на сайте и о том, как с ней взаимодействовать
    * list_display - поля модели, которые будут отображаться на странице списка объектов администрирования
    * list_filter - поля модели, по которым можно фильтровать список объектов на странице администрирования
    * search_fields - поля модели, по которым можно производить поиск объектов на странице администрирования
    * prepopulated_fields - словарь, используется для автоматического заполнения поля 'slug' на основе поля 'title'
    * raw_id_fields - поля модели, которые должны отображаться как ссылки на объекты, а не как выпадающие списки
    * date_hierarchy - имя поля модели, используемое для построения иерархии дат на странице администрирования
    * ordering - порядок сортировки списка объектов на странице администрирования
    """
    list_display = ['title', 'slug', 'author', 'publish', 'status',]
    list_filter= ['status', 'created', 'publish', 'author',]
    search_fields = ['title', 'body',]
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
