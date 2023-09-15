from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def helloWorld(request):
    return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)
