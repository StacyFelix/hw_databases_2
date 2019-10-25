from django.db.models import Prefetch
from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    list_articles = []
    articles = Article.objects.all().prefetch_related('tags').order_by('-published_at')#.values()
    for article in articles:
        object_article = {}
        object_article['image'] = article.image
        object_article['title'] = article.title
        object_article['text'] = article.text

        object_article['tags'] = article.tags.all().order_by('-articlehastag__is_main', 'title').values('articlehastag__is_main', 'title')
        print(object_article['tags'])

        list_articles.append(object_article)
    context = {'list_articles': list_articles}

    return render(request, template, context)
