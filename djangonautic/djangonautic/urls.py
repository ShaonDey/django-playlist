from django.conf.urls import url, include
from django.contrib import admin
#from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('about/$', views.about),
    #path('^$', views.homepage)

    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
]

urlpatterns += staticfiles_urlpatterns()
