from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from .views import Register_view,Register_detail
from .views import Bookinglistview,AvailableSlotView

urlpatterns = [
   path('register/',Register_view.as_view()),
   path('register/<int:pk>/',Register_detail.as_view()),
   path('login/',TokenObtainPairView.as_view()),
   path('login/refresh/',TokenRefreshView.as_view()),
   path('book/',Bookinglistview.as_view()),
   path('available/',AvailableSlotView.as_view()),
]
