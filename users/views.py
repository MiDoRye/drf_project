from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from django.contrib import auth

from users.models import User

from users.serializers import UserSerializer, CustomTokenObtainPairSerializer, UserProfileSerializer
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입완료"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        return Response(UserSerializer(request.user).data)
        
    def put(self, request):
        user = request.user   
        serializer = UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"회원정보 변경 완료"}, status=status.HTTP_200_OK)
        else:
            return Response({"message":f"${serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        user = request.user      
        user.delete()
        return Response({"message": "회원 탈퇴 완료"}, status=status.HTTP_200_OK)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    

class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user.save()
        return Response("get 요청")    
    

class FollowView(APIView):
    def post(self, request, user_id):
        you = get_object_or_404(User, id=user_id)
        me = request.user
        if me in you.followers.all():
            you.followers.remove(me)
            return Response("언팔로우했습니다.", status=status.HTTP_200_OK)
        else:
            you.followers.add(me)
            return Response("팔로우했습니다.", status=status.HTTP_200_OK)


class ProfileView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)