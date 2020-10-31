from django.conf.urls import url
from .views import PropertyRudView, PropertyAPIView, CreateAndListActivityAPIView, RescheduleOrCancelActivityAPIView, SurveyAPIView

urlpatterns = [
    url(r'^$', PropertyAPIView.as_view(), name='property-create'),
    url(r'^(?P<id>\d+)/$', PropertyRudView.as_view(), name='property-rud'),
    url(r'^activity/$', CreateAndListActivityAPIView.as_view(), name='activity-create'),
    url(r'^activity/(?P<id>\d+)/$', RescheduleOrCancelActivityAPIView.as_view(), name='activity-update'),
    url(r'^survey/(?P<id>\d+)/$', SurveyAPIView.as_view(), name='survey-retrieve')

]
