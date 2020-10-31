"""
This module contains the business logic for retrieving Activities List from DB
"""
from datetime import datetime, timedelta

import pytz
from django.db.models import Q

from ..models import Activity
from ..utils.custom_exception import DatesIncomplete


# This is the default getter for activities
def get_activities(base_url):
    utc = pytz.UTC
    today_date = datetime.today()
    start_date = today_date - timedelta(days=3)
    end_date = today_date + timedelta(weeks=2)

    schedule_greater_than_start = Q(schedule__gte=start_date)
    schedule_less_than_end = Q(schedule__lte=end_date)
    activities_found = Activity.objects.filter(schedule_greater_than_start, schedule_less_than_end)

    response = {'activities': []}

    for activity in activities_found:
        condition = None
        if activity.status == 'active' and utc.localize(today_date) <= activity.schedule:
            condition = 'Pendiente a realizar'
        elif activity.status == 'active' and utc.localize(today_date) > activity.schedule:
            condition = 'Atrasada'
        elif activity.status == 'done':
            condition = 'Finalizada'
        activity_property = activity.property
        activity_survey_link = None
        if activity.get_survey():
            activity_survey_link = base_url + activity.survey.get_absolute_url()

        formatted_activity = {
            'id': activity.id,
            'title': activity.title,
            'created_at': activity.created_at,
            'status': activity.status,
            'condition': condition,
            'property': {'ID': activity_property.id, 'title': activity_property.title,
                         'address': activity_property.address},
            'survey': activity_survey_link
        }
        response['activities'].append(formatted_activity)
    return response


# This is the getter with filter for activities
def get_activities_filter(start_date, end_date, status, base_url):
    utc = pytz.UTC
    today_date = datetime.today()
    if all([start_date, end_date]):
        schedule_greater_than_start = Q(schedule__gte=start_date)
        schedule_less_than_end = Q(schedule__lte=end_date)
        activities_found = None
        if status:
            activities_found = Activity.objects.filter(schedule_greater_than_start, schedule_less_than_end,
                                                       status=status)
        else:
            activities_found = Activity.objects.filter(schedule_greater_than_start, schedule_less_than_end)
    else:
        raise DatesIncomplete()

    response = {'activities': []}

    for activity in activities_found:
        condition = None
        if activity.status == 'active' and utc.localize(today_date) <= activity.schedule:
            condition = 'Pendiente a realizar'
        elif activity.status == 'active' and utc.localize(today_date) > activity.schedule:
            condition = 'Atrasada'
        elif activity.status == 'done':
            condition = 'Finalizada'
        activity_property = activity.property
        activity_survey_link = None
        if activity.get_survey():
            activity_survey_link = base_url + activity.survey.get_absolute_url()

        formatted_activity = {
            'id': activity.id,
            'title': activity.title,
            'created_at': activity.created_at,
            'status': activity.status,
            'condition': condition,
            'property': {'ID': activity_property.id, 'title': activity_property.title,
                         'address': activity_property.address},
            'survey': activity_survey_link
        }
        response['activities'].append(formatted_activity)
    return response
