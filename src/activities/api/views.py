from rest_framework import generics, mixins

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
