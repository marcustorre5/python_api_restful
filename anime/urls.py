
from django.contrib import admin
from django.urls import path


from django.urls import include
from rest_framework import routers
from webanime import views as aimeviewsets

route = routers.DefaultRouter()
route.register(r'animes', aimeviewsets.AnimeViewSet, basename="Animes")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(route.urls))
]
