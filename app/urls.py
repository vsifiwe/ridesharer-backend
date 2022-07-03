from django.urls import path
from .views import (create_user, delete_index, delete_route, loader,
                    pusher_auth, save_route, search_routes,
                    set_map, update_route)

urlpatterns = [
    path('create-user', create_user),
    path('delete-index', delete_index),
    path('delete-route', delete_route),
    path('loader', loader),
    path('pusher-auth', pusher_auth),
    path('save-route', save_route),
    path('search-routes', search_routes),
    path('set-map', set_map),
    path('update-route', update_route),
]
