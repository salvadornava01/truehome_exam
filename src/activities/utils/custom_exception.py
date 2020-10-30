from rest_framework.exceptions import APIException


class ActivityConflict(APIException):
    status_code = 401
    default_detail = 'La propiedad ya cuenta con una actividad agendada en este horario'
    default_code = 'error'


class PropertyInactive(APIException):
    status_code = 403
    default_detail = 'La propiedad se encuentra inactiva'
    default_code = 'error'


class ActivityCancelled(APIException):
    status_code = 403
    default_detail = 'La actividad se encuentra cancelada'
    default_code = 'error'
