from dataclasses import field
from rest_framework import serializers
from users.models import User
from articles.serializers import ArticleListSerializer

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    followers = serializers.StringRelatedField(many=True)
    followings = serializers.StringRelatedField(many=True)
    article_set = ArticleListSerializer(many=True)
    like_articles = ArticleListSerializer(many=True)

    class Meta:
        model = User
        fields = ("id", "email", "followings", "followers", "article_set", "like_articles")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

        # 정보 확인할 때 비밀번호 출력 안되게 설정
        extra_kwargs = {
            "password":{
                "write_only":True,
            },
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()        
        return user
    
    def update(self, validate_data):
        user = super().create(validate_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        token['name'] = user.name
        token['age'] = user.age
        token['gender'] = user.gender

        return token