from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.core.serializers import json
from django.db.models import Q
from rest_framework.authtoken import views
from rest_framework import generics, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.authtoken.models import Token

from .permissions import IsOwnerOrReadOnly
from ...models import Account
from .serializers import RegisterSerializer, LoginSerializer, AccountUpdateSerializer, AccountOwnImageUpdateSerializer, \
    SetNewPasswordSerializer
from rest_framework.response import Response


class AccountRegisterView(generics.GenericAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/register/
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        username = serializer.data.get('username')
        tokens = Account.objects.get(username=username).tokens
        user_data['tokens'] = tokens
        return Response({'success': True, 'data': user_data}, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/login/
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)


class GetAccountView(generics.RetrieveAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/get-account/
    serializer_class = AccountUpdateSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)

    def get(self, request, *args, **kwargs):
        user = request.user
        query = Account.objects.get(id=user.id)
        serializer = self.get_serializer(query)
        return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)


class AccountRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/retrieve-update/<id>/
    serializer_class = AccountUpdateSerializer
    queryset = Account.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request, *args, **kwargs):
        query = self.get_object()
        if query:
            serializer = self.get_serializer(query)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'query did not exist'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response({'success': False, 'message': 'credentials is invalid'}, status=status.HTTP_404_NOT_FOUND)


class AccountUpdateOwnImageView(generics.RetrieveUpdateAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/image-retrieve-update/<id>/
    serializer_class = AccountOwnImageUpdateSerializer
    queryset = Account.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)

    def get(self, request, *args, **kwargs):
        query = self.get_object()
        if query:
            serializer = self.get_serializer(query)
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'query does not match'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response({'success': False, 'message': 'credentials are invalid'}, status=status.HTTP_400_BAD_REQUEST)


class AccountListView(generics.ListAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/list/
    serializer_class = AccountUpdateSerializer
    queryset = Account.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q')
        role = self.request.GET.get('role')

        q_condition = Q()
        if q:
            q_condition = Q(full_name__icontains=q) | Q(phone__icontains=q) | Q(username__icontains=q) | \
                          Q(email__icontains=q)

        role_condition = Q()
        if role:
            role_condition = Q(role__exact=role)
        queryset = qs.filter(q_condition, role_condition)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            serializer = self.get_serializer(queryset, many=True)
            count = queryset.count()
            return Response({'success': True, 'count': count, 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'success': False, 'data': 'queryset does not match'}, status=status.HTTP_404_NOT_FOUND)


class SetNewPasswordView(generics.UpdateAPIView):
    # http://127.0.0.1:8000/api/accounts/v1/change-password/
    serializer_class = SetNewPasswordSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    authentication_classes = [BasicAuthentication]
    queryset = Account.objects.all()

    def patch(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": self.request})
        if serializer.is_valid(raise_exception=True):
            return Response({'success': True, 'data': 'Successfully changed'}, status=status.HTTP_200_OK)
        return Response({'success': False, 'message': 'Credentials is invalid'}, status=status.HTTP_400_BAD_REQUEST)

