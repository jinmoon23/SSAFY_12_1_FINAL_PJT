from rest_framework import serializers
from .models import Theme, Stock, IndustryCode, UserProfile, Interest, Article

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

class ArticleSerializer(serializers.ModelSerializer):
    like_article = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    author = serializers.ReadOnlyField(source='author.nickname')
    
    class Meta:
        model = Article
        fields = (
            'id',
            'stock',
            'theme',
            'author',
            'title',
            'content',
            'created_at',
            'updated_at',
            'like_article'
        )
        read_only_fields = ('theme', 'like_article', 'author')