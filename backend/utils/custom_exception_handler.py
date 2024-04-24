from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is None:
        response = Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    exception_class = exc.__class__.__name__

    if exception_class == 'AttributeError':
        response.data = {
            "error": "서버코드에러"
        }

    if exception_class == 'NotAuthenticated':
        response.data = {
            "error": "Login first to access this resource."
        }

    if exception_class == 'InvalidToken':
        response.data = {
            "error": "Your authentication token is expired. Please login again."
        }

    return response
