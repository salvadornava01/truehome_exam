from django.db import models
from django.utils.encoding import smart_text
from django.urls import reverse
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

    def get_survey(self):
        if hasattr(self, 'survey'):
            return self.survey
        return None


class Survey(models.Model):
    activity = models.OneToOneField(Activity, on_delete=models.PROTECT)
    answers = JSONField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)

    def __str__(self):
        return smart_text(self.activity)

    def get_absolute_url(self):
        return reverse('api-properties:survey-retrieve', kwargs={'id': self.id})
