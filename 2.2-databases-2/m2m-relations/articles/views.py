from django.shortcuts import render, HttpResponse

from articles.models import Article,Tag


def articles_list(request):
    template = 'articles/news.html'
    data = Article.objects.all()
    context = {'object_list':data}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context)


