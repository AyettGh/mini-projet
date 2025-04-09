from django.contrib import admin
<<<<<<< HEAD
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('surveillance_api.urls')),

<<<<<<< HEAD
=======
    # Include the app's URLs
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
]
=======
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("surveillance_api.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", RedirectView.as_view(url="/admin/")),

]
>>>>>>> 4a04a29dd8e8ed24a3f757d5564cfb98af3520ea
