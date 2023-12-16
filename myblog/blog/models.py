from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=250, verbose_name="Имя")
    username = models.CharField(max_length=35, verbose_name="Логин", unique=True)
    avatar = models.ImageField('Аватар', upload_to='avatars/', blank=True)
    userInfo = models.TextField(max_length=500, verbose_name="Информация о пользователе", blank=False)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('Заголовок поста', max_length=100)
    description = models.TextField('Текст поста')
    date = models.DateField('Дата публикации', auto_now_add=True)
    image = models.ImageField('Изображение', upload_to='post_image/')

    def __str__(self):
        return f'{self.user.username} - {self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='комментатор', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='пост', on_delete=models.CASCADE)
    comment_text = models.TextField('Текст комментария', max_length=2000)
    comment_image = models.ImageField('Фотография', upload_to='comment_image/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.date}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.post.id)])

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

