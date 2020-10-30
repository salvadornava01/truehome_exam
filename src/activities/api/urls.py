from django.conf.urls import url
from .views import PropertyRudView, PropertyAPIView, CreateActivityAPIView, RescheduleActivityAPIView

urlpatterns = [
    url(r'^$', PropertyAPIView.as_view(), name='property-create'),
    url(r'^(?P<id>\d+)/$', PropertyRudView.as_view(), name='property-rud'),
    url(r'^activity/$', CreateActivityAPIView.as_view(), name='activity-create'),
    url(r'^activity/(?P<id>\d+)/$', RescheduleActivityAPIView.as_view(), name = 'activity-update')

]
