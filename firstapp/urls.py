from django.conf.urls import include, url
from django.contrib import admin
import article.urls

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^basicview/', include(article.urls)),
    url(r'^', include(article.urls)),
]
