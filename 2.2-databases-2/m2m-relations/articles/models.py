from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        constraints = [
            models.UniqueConstraint(fields=['name'],name='такой тег уже есть')
        ]

    def __str__(self):
        return self.name

class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag,related_name='articles',through='Scope', verbose_name='Теги')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Scope(models.Model):

    class Meta:
        verbose_name = 'связь'
        constraints = [
            models.UniqueConstraint(fields=['tag', 'article'], name='тег должен быть уникальным'),
            models.UniqueConstraint(fields=['article', 'is_main'], condition=models.Q(is_main=True) , name='главный один')
        ]

    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='scopes')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    is_main = models.BooleanField(default=False)

