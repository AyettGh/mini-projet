from django.urls import path
<<<<<<< HEAD
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from rest_framework_simplejwt import views as jwt_views

from .views import SignUpView, LoginView

=======
from . import views
from rest_framework_simplejwt import views as jwt_views

>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
app_name = 'surveillance_api'  # This is important for namespacing!

urlpatterns = [
    path('', views.index, name='index'),
    path('api/upload-excel/', views.UploadExcelView.as_view(), name='upload_excel'),
    path('api/update-availability/', views.UpdateAvailabilityView.as_view(), name='update_availability'),
    path('api/assign-sessions/', views.AssignSessionsView.as_view(), name='assign_sessions'),
    path('api/generate-pdf/', views.GeneratePDFView.as_view(), name='generate_pdf'),
<<<<<<< HEAD
    path('api/signup/', SignUpView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
=======
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

>>>>>>> d968a2574d3a78eb777d428b9fce10c5cae2e480
]
