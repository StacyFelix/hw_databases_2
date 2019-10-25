from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=60, verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(Tag, through='ArticleHasTag', related_name='articles')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class ArticleHasTag(models.Model):
    is_main = models.BooleanField(verbose_name='Основной')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['article', 'tag'], name='article_tag'),
            # не стала добавлять эту unique_together, поскольку есть ValidationError в админке для нее
            # models.UniqueConstraint(fields=['article', 'tag', 'is_main'], name='article_tag_is_main'),
        ]

