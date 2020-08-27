from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('leet.leet.urls', namespace='leet')),
    path('api/', include('leet.api.urls')),
    path('admin/', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
]
