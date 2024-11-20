from rest_framework import serializers
from .models import Theme, Stock, IndustryCode, UserProfile, Interest

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class IndustryCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndustryCode
        fields = '__all__'

class ThemeSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(source='stock_set', many=True, read_only=True)
    industry_codes = IndustryCodeSerializer(many=True, read_only=True)
    
    class Meta:
        model = Theme
        fields = '__all__'


class ThemeInfoSerializer(serializers.ModelSerializer):
    stocks = StockSerializer(source='stock_set', many=True, read_only=True)
    theme_name = serializers.CharField(source='name')
    
    class Meta:
        model = Theme
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = '__all__'

class AnalyzeResponseSerializer(serializers.Serializer):
    message = serializers.CharField()
    recommended_themes = ThemeInfoSerializer(many=True)    