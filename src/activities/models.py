from django.db import models
from django.utils.encoding import smart_text
from django.contrib.postgres.fields import JSONField


class Property(models.Model):
    title = models.CharField(max_length=255)
    address = models.TextField(blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False)
    disabled_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=35)

    def __str__(self):
        return smart_text(self.title)


class Activity(models.Model):
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    schedule = models.DateTimeField(null=False)
    title = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True, null=False)
    status = models.CharField(max_length=35)

    def __str__(self):
        return smart_text(self.title)


class Survey(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    answers = JSONField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)
