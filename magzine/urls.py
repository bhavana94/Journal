from django.conf.urls import url, include
from django.contrib import admin
from magzine import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^article/', views.PublicationList)
]

urlpatterns = format_suffix_patterns(urlpatterns)