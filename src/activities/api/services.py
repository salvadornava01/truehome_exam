"""
Este módulo contiene la lógica de negocio para la creación de actividades
"""
from datetime import datetime, timedelta

from django.db import transaction
from django.shortcuts import get_object_or_404

from ..models import Activity, Property
from ..utils.custom_exception import ActivityConflict, PropertyInactive, ActivityCancelled


@transaction.atomic
def create_activity(
        *,
        property_id,
        title: str,
        schedule: datetime,
        status: str
) -> Activity:
    property_found = Property.objects.get(id=property_id)

    # Check if property_found is active
    if property_found.status != 'active':
        raise PropertyInactive()

    # Check if property has related activities
    activities_for_property = Activity.objects.filter(property_id=property_id)
    activities_times = map(lambda activity: activity.schedule, activities_for_property)
    for activity_time in activities_times:
        # If activity schedule between actual activity_time and activity_time + 1 hour
        if (schedule >= activity_time) and (schedule <= (activity_time + timedelta(hours=1))):
            raise ActivityConflict()
    activity = Activity.objects.create(property_id=property_found, title=title, schedule=schedule, status=status)
    return activity


@transaction.atomic
def reschedule_activity(
        *,
        activity_id,
        new_date: datetime,
) -> Activity:
    activity_found = get_object_or_404(Activity, id=activity_id)
    # Check if activity is active
    if activity_found.status == 'canceled':
        raise ActivityCancelled()
    property_found = activity_found.property
    property_id = property_found.id
    activities_for_property = Activity.objects.filter(property_id=property_id)
    activities_times = map(lambda activity: activity.schedule, activities_for_property)
    for activity_time in activities_times:
        # If activity schedule between actual activity_time and activity_time + 1 hour
        if (new_date >= activity_time) and (new_date <= (activity_time + timedelta(hours=1))):
            raise ActivityConflict()
    activity_found.schedule = new_date
    activity_found.save(update_fields=['schedule'])
    return activity_found
