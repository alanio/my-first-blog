from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]

admin.site.site_header = 'ADMIN'
admin.site.index_title = 'BLOG DJANGO'
admin.site.site_title = 'Administração'


