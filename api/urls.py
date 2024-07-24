from django.urls import path 
from .views import PlaceList , PlaceDetail ,UserList , UserDetail


name = 'api'
urlpatterns = [
    path("place/", PlaceList.as_view(), name="list"),
    path("place/<int:pk>/", PlaceDetail.as_view(), name="detail"),
    path("user/", UserList.as_view(), name="user-list"),
    path("user/<int:pk>/", UserDetail.as_view(), name="user-detail"),
]
