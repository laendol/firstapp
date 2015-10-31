from django.conf.urls import patterns, include, url

urlpatterns = [
    url(r'^1/', 'article.views.basic_one'),
    url(r'^3/', 'article.views.template_three'),
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
    url(r'^', 'article.views.articles'),
]
