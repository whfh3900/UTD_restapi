from rest_framework import serializers
from .models import Transaction, UserInfo


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함