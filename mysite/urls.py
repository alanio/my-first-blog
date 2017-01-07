from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('mysite.blog.urls')),
    url(r'^redactor/', include('redactor.urls')),
]

admin.site.site_header = 'ADMIN'
admin.site.index_title = 'BLOG DJANGO'
admin.site.site_title = 'alncs.pythonanywhere.com'


