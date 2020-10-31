from django.contrib import admin
from .models import Property, Activity, Survey


class PropertyAdmin(admin.ModelAdmin):
    class Meta:
        model = Property


admin.site.register(Property, PropertyAdmin)


class ActivityAdmin(admin.ModelAdmin):
    class Meta:
        model = Activity


admin.site.register(Activity, ActivityAdmin)


class SurveyAdmin(admin.ModelAdmin):
    class Meta:
        model = Survey


admin.site.register(Survey, SurveyAdmin)
