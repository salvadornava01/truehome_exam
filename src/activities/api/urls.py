from django.conf.urls import url
from .views import PropertyRudView, PropertyAPIView

urlpatterns = [
    url(r'^$', PropertyAPIView.as_view(), name='property-create'),
    url(r'^(?P<id>\d+)/$', PropertyRudView.as_view(), name='property-rud')
]
