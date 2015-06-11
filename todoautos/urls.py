from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 

from main_app import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todoautos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^buscar/', views.search, name='search'),
    url(r'^publicacion/(?P<publication_id>\d+)/$', views.publication, name='publication'),
    url(r'^scraper_admin/', views.scraper_admin, name='scraper_admin'),
    url(r'^add_publication/chileautos/(?P<chileautos_id>\d+)/$', views.add_publication_from_chileautos, name='add_publication_from_chileautos'),
    url(r'^$', views.index, name='index'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


