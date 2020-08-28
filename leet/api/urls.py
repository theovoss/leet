from django.conf import settings
from django.views.generic import TemplateView

from django.conf.urls import include, url
from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers

from leet.api.viewsets.two_sum import TwoSumViewset

# Root

root = routers.DefaultRouter()


# App: leet
root.register(r'leet/two-sum', TwoSumViewset, basename="two-sum")

# root.register(...)

# URLs

schema_view = get_schema_view(
    openapi.Info(title="leet", default_version='0', description="The API for leet.",),
    url=settings.BASE_URL,
)

urlpatterns = [
    url('^', include(root.urls)),
    url('^client/', include('rest_framework.urls')),
    url('^docs/', schema_view.with_ui('swagger')),
]
