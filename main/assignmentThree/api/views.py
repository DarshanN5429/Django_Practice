from assignmentThree.api.serializers import MyModelSerializer
from assignmentThree.models import MyModel
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def modelList(request):
    list1 = MyModel.objects.all()
    serial = MyModelSerializer(list1, many=True)
    return Response(serial.data, status=200)
