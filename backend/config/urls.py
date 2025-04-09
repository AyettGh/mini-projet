from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('surveillance_api.urls')),

<<<<<<< HEAD
=======
    # Include the app's URLs
>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
]
