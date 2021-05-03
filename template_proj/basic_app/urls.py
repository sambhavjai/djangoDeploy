from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative_url,name='relative'),
    path('register/',views.register,name='registeration'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
]
