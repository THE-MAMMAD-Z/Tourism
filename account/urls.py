from django.urls import path
from .views import SignUpView, CustomLoginView, logout_view , profile

app_name='account'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/',profile , name='profile')
]
