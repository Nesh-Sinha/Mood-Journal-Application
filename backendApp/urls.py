from django.urls import path,include
from django.contrib import admin

from rest_framework_simplejwt.views import TokenObtainPairView
from .views import RegisterUserView

urlpatterns = [
    path('signup/', RegisterUserView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='login'),  # JWT login
    path('admin/', admin.site.urls),
    path('api/', include('backendApp.urls')),  # Include backendApp URLs

]
