from datetime import datetime

from rest_framework import generics, mixins, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK

from .selectors import get_activities, get_activities_filter
from .services import create_activity, reschedule_activity, cancel_activity
from ..models import Property, Survey
from .serializers import PropertySerializer
from ..utils.custom_exception import DatesException, DatesIncomplete


# For Create Properties
class PropertyAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# For Retrieve Update and Delete Properties
class PropertyRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()


# For Create and get List Activities
class CreateAndListActivityAPIView(APIView):
    class InputSerializer(serializers.Serializer):
        property_id = serializers.IntegerField()
        title = serializers.CharField()
        schedule = serializers.DateTimeField()
        status = serializers.CharField()

    serializer_class = InputSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_activity(**serializer.validated_data)

        return Response(status=HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        start_date_str: datetime = request.GET.get('start_date')
        end_date_str: datetime = request.GET.get('end_date')
        start_date = None
        end_date = None
        status = request.GET.get('status')

        if all([start_date_str, end_date_str]):
            try:
                start_date = datetime.strptime(start_date_str, '%d-%m-%y')
                end_date = datetime.strptime(end_date_str, '%d-%m-%y')
            except:
                raise DatesException()

        elif any([start_date_str, end_date_str]):
            raise DatesIncomplete()

        activities = None
        # If there is a filter option, use filter list
        if any([start_date, end_date, status]):
            activities = get_activities_filter(start_date, end_date, status)
        # Otherwise use default list
        else:
            activities = get_activities()

        return Response(data=activities, status=HTTP_200_OK)

    def get_queryset(self):
        return Property.objects.all()


# For Reschedule or Cancel Activities
class RescheduleOrCancelActivityAPIView(APIView):
    class UpdateSerializer(serializers.Serializer):
        activity_id = serializers.IntegerField()
        new_date = serializers.DateTimeField()

    lookup_field = 'id'
    serializer_class = UpdateSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.UpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        activity_id = kwargs['id']
        new_date = serializer.validated_data['new_date']
        reschedule_activity(activity_id=activity_id, new_date=new_date)

    def delete(self, request, *args, **kwargs):
        activity_id = kwargs['id']

        cancel_activity(activity_id=activity_id)
        return Response(status=HTTP_200_OK)


# For Survey View Link
class SurveyAPIView(generics.RetrieveAPIView):
    class SurveySerializer(serializers.ModelSerializer):
        class Meta:
            fields = "__all__"
            model = Survey

    lookup_field = 'id'
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer
