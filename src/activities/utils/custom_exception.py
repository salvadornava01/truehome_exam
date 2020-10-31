from rest_framework.exceptions import APIException


class ActivityConflict(APIException):
    status_code = 401
    default_detail = 'La propiedad ya cuenta con una actividad agendada en este horario'
    default_code = 'error'


class PropertyInactive(APIException):
    status_code = 403
    default_detail = 'La propiedad se encuentra inactiva'
    default_code = 'error'


class ActivityCancelledOrDone(APIException):
    status_code = 403
    default_detail = 'La actividad se encuentra cancelada o terminada'
    default_code = 'error'


class DatesException(APIException):
    status_code = 401
    default_detail = 'Necesitas proveer un rango de fechas válido'
    default_code = 'error'


class DatesIncomplete(APIException):
    status_code = 401
    default_detail = 'Por favor ingresa fecha de inicio y fecha de fin con un formato válido: dd-mm-aa'
    default_code = 'error'
