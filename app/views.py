from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Account, Route

@api_view(['POST'])
def create_user(request):
    username = request.data.get('username')
    try:
        Account.objects.get(username=username)
    except Account.DoesNotExist:
        Account.objects.create(username=username)

    return Response("ok")

@api_view(['POST'])
def save_route(request):
    end_location = request.data.get('end_location')
    start_location = request.data.get('start_location')
    username = request.data.get('username')
    from_name = request.data.get('from')
    to_name = request.data.get('to')

    user = Account.objects.get(username=username)

    data = {
        'username': user,
        'start_lat': start_location['latitude'],
        'start_lon': start_location['longitude'],
        'end_lat': end_location['latitude'],
        'end_lon': end_location['longitude'],
        'from_name': from_name,
        'to_name': to_name
        }

    route = Route.objects.create(**data)

    return Response({"id": route.id})

@api_view(['POST'])
def search_routes(request):
    dest = request.data.get('dest')
    origin = request.data.get('origin')

    route = Route.objects.all().last()
    response = {
        'username': route.username.username,
        'from': route.from_name,
        'to': route.to_name
    }
    return Response(response)

@api_view(['GET'])
def pusher_auth(request):
    return Response({"message": "pusher auth"})

@api_view(['GET'])
def delete_index(request):
    return Response({"message": "delete index"})

@api_view(['GET'])
def delete_route(request):
    return Response({"message": "delete route"})

@api_view(['GET'])
def loader(request):
    return Response({"message": "loader"})

@api_view(['GET'])
def set_map(request):
    return Response({"message": "set map"})

@api_view(['GET'])
def update_route(request):
    return Response({"message": "update route"})