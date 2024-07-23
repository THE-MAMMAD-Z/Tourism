from django.urls import path
from .views import SignUpView, CustomLoginView, logout_view , ProfileView

app_name='account'
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/',ProfileView , name='profile')
]
