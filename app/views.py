from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def create_user(request):
    return Response({"message": "Create user"})

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
def pusher_auth(request):
    return Response({"message": "pusher auth"})

@api_view(['GET'])
def save_route(request):
    return Response({"message": "save route"})

@api_view(['GET'])
def search_routes(request):
    return Response({"message": "search routes"})

@api_view(['GET'])
def set_map(request):
    return Response({"message": "set map"})

@api_view(['GET'])
def update_route(request):
    return Response({"message": "update route"})