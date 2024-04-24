from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is None:
        response = Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    exception_class = exc.__class__.__name__

    # print(f'에러종류: {exception_class}')

    if exception_class == 'AttributeError':
        response.data = {
            "error": "서버코드에러"
        }

    if exception_class == 'NotAuthenticated':
        response.data = {
            "error": "로그인필요"
        }

    if exception_class == 'InvalidToken':
        response.data = {
            "error": "토큰만료"
        }

    return response
