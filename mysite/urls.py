
# from django.urls import include, path
# from rest_framework.authtoken import views

# urlpatterns = [
#     path('', include('polls.urls')),
#     path('admin/', admin.site.urls),

# ]
from django.urls import path, include
from django.contrib import admin
from django.conf.urls import include
urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]