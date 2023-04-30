from django import path
from . import views

# пространство имён приложения
app_name = 'blog'

# шаблоны URL-адресов
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]