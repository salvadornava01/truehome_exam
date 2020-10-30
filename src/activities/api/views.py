from rest_framework import generics, mixins, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_409_CONFLICT

from .services import create_activity, reschedule_activity
from ..models import Property
from .serializers import PropertySerializer


class PropertyAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PropertyRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = PropertySerializer

    def get_queryset(self):
        return Property.objects.all()


class CreateActivityAPIView(APIView):
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

    def get_queryset(self):
        return Property.objects.all()


class RescheduleActivityAPIView(APIView):
    class InputSerializer(serializers.Serializer):
        activity_id = serializers.IntegerField()
        new_date = serializers.DateTimeField()

    lookup_field = 'id'
    serializer_class = InputSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        activity_id = kwargs['id']
        new_date = serializer.validated_data['new_date']
        reschedule_activity(activity_id=activity_id, new_date=new_date)

        return Response(status=HTTP_200_OK)
