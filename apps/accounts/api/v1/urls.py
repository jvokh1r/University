from django.urls import path
from .views import AccountRegisterView, LoginView, AccountRetrieveUpdateView, GetAccountView, AccountUpdateOwnImageView, \
   AccountListView, SetNewPasswordView


urlpatterns = [
   path('register/', AccountRegisterView.as_view()),
   path('login/', LoginView.as_view()),
   path('retrieve-update/<int:pk>/', AccountRetrieveUpdateView.as_view()),
   path('get-account/', GetAccountView.as_view()),
   path('image-retrieve-update/<int:pk>/', AccountUpdateOwnImageView.as_view()),
   path('list/', AccountListView.as_view()),
   path('change-password/<int:pk>/', SetNewPasswordView.as_view()),
]