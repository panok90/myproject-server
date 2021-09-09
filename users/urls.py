from django.urls import path
from users.views import Login, registration, Logout, profile

app_name = 'users'
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('registration/', registration, name='registration'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
]
