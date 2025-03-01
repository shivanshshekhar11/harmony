from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Room
from .serializers import RoomSerializer


@api_view(['GET'])
def getAllRoutes(request):
    routes = [
        'GET api/',
        'GET api/rooms/',
    ]

    return Response(routes)


@api_view(['GET'])
def getAllRooms(request):
    rooms = Room.objects.all()
    response = RoomSerializer(rooms, many=True)
    return Response(response.data)
