from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import ThemeSerializer
from .utils import get_industry_price_series, get_theme_price_series
from utils.token import get_access_token,get_access_to_websocket  # 프로젝트 레벨의 token 유틸리티 import
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
# 혜령 디버깅 추가
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserProfile, UserInterest, Interest, IndustryCode, Theme
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta

# 프론트에 필요한 토큰 준비


# CSRF 보호 비활성화
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def analyze(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = request.user
            
            # UserProfile 처리
            try:
                user_profile = UserProfile.objects.get(user=user)
                user_profile.mbti = data.get('mbti')
                user_profile.period = data.get('period')
                user_profile.save()
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(
                    user=user,
                    mbti=data.get('mbti'),
                    period=data.get('period')
                )
            
            # Interest 처리
            interest_names = data.get('interest', [])
            UserInterest.objects.filter(user=user).delete()
            themes_info = []
            for interest_name in interest_names:
                try:
                    interest = Interest.objects.get(name=interest_name)
                    UserInterest.objects.create(
                        user=user,
                        interest=interest
                    )
                    theme = Theme.objects.get(name=interest_name)
                    # stocks = theme.stock_set.all().values_list('name', flat=True)
                    stocks = theme.stock_set.all().values('name', 'code')
                    theme_info = {
                    'theme_name': theme.name,
                    'stocks': list(stocks),
                    'description': theme.description,
                    }
                    themes_info.append(theme_info)
                except Interest.DoesNotExist:
                    continue
            
            # themes_info 길이 조정
            if len(themes_info) < 6:
                # 현재 테마 이름 목록
                current_themes = [theme['theme_name'] for theme in themes_info]
                
                # 추가로 필요한 테마 수
                needed = 6 - len(themes_info)
                
                # 현재 없는 테마들 중에서 랜덤하게 선택
                additional_themes = Theme.objects.exclude(
                    name__in=current_themes
                ).prefetch_related('stock_set')[:needed]
                
                # 추가 테마 정보 수집
                for theme in additional_themes:
                    # stocks = theme.stock_set.all().values_list('name', flat=True)
                    stocks = theme.stock_set.all().values('name', 'code')
                    themes_info.append({
                        'theme_name': theme.name,
                        'stocks': list(stocks),
                        'description': theme.description,
                    })
            
            # 6개로 제한
            themes_info = themes_info[:6]

            return JsonResponse({
                'message': '저장이 완료되었습니다.',
                'recommended_themes': themes_info
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'GET 요청은 허용되지 않습니다.'}, status=405)


def get_token(request):
    websocket_token = get_access_to_websocket()
    return JsonResponse({'websocket_token': websocket_token})

@api_view(['POST'])
def draw_theme_chart(request):
    try:
        access_token = get_access_token()
        data = request.data
        theme_name = data.get('theme_name')
        end_date = data.get('end_date')
        # end_date를 datetime 객체로 변환
        end_date_obj = datetime.strptime(end_date, '%Y%m%d')
        
        # 1년 전 날짜 계산
        start_date_obj = end_date_obj - relativedelta(years=1)
        
        # YYYYMMDD 형식의 문자열로 변환
        start_date = start_date_obj.strftime('%Y%m%d')
        
        # 테마 정보 가져오기
        theme = Theme.objects.get(name=theme_name)
        theme_serializer = ThemeSerializer(theme)
        
        # 차트 데이터 가져오기
        chart_data = get_theme_price_series(
            access_token=access_token,
            theme_name=theme_name,
            start_date=start_date,
            end_date=end_date
        )
        
        # 응답 데이터 구성
        response_data = {
            'theme_info': theme_serializer.data,
            'chart_data': chart_data['data']
        }
        
        return Response(response_data)
    
    except Theme.DoesNotExist:
        return Response({
            'status': 'error',
            'message': f"Theme '{theme_name}' not found"
        }, status=404)
    except Exception as e:
        return Response({
            'status': 'error',
            'message': str(e)
        }, status=500)