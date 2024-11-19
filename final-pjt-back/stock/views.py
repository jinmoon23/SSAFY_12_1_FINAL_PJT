from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_industry_price_series 
from utils.token import get_access_token  # 프로젝트 레벨의 token 유틸리티 import
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
# 혜령 디버깅 추가
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import UserProfile, UserInterest, Interest, IndustryCode, Theme
import json

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
                    stocks = theme.stock_set.all().values_list('name', flat=True)
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
                    stocks = theme.stock_set.all().values_list('name', flat=True)
                    themes_info.append({
                        'theme_name': theme.name,
                        'stocks': list(stocks)
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

# def get_recommended_themes(user):
#     # 사용자의 관심사와 연결된 IndustryCode 정보 가져오기
#     industry_codes = IndustryCode.objects.filter(
#         interest__userinterest__user=user
#     ).values_list('api_request_code', flat=True)

#     # IndustryCode와 매칭되는 Theme 정보 가져오기
#     themes = Theme.objects.filter(
#         code__in=industry_codes
#     ).prefetch_related('stock_set')
    
#     themes_info = []
#     for theme in themes:
#         # 각 테마에 연결된 주식들 가져오기
#         stocks = theme.stock_set.all().values_list('name', flat=True)
        
#         theme_info = {
#             'theme_name': theme.name,
#             'stocks': list(stocks)
#         }
#         themes_info.append(theme_info)
    
#     return themes_info


# def get_recommended_themes(user):
#     # 사용자 프로필 정보 가져오기
#     user_profile = UserProfile.objects.get(user=user)
#     mbti = user_profile.mbti
#     period = user_profile.period
    
#     # 사용자의 관심사에 해당하는 업종코드 가져오기
#     industry_codes = IndustryCode.objects.filter(
#         interest__userinterest__user=user
#     ).values_list('api_request_code', flat=True)
    
#     # MBTI 기반 투자 성향 분석
#     risk_level = analyze_mbti_risk(mbti)
    
#     # 투자 기간에 따른 가중치 설정
#     period_weight = get_period_weight(period)
    
#     # 한국투자증권 API 호출을 위한 테마 코드 구성
#     theme_codes = list(set(industry_codes))  # 중복 제거
    
#     # API 호출 및 테마 정보 가져오기
#     themes_info = []
#     for code in theme_codes:
#         theme_data = get_theme_data_from_api(code)  # 한국투자증권 API 호출
#         if theme_data:
#             # 위험도와 기간 가중치를 고려한 점수 계산
#             score = calculate_theme_score(theme_data, risk_level, period_weight)
#             themes_info.append({
#                 'code': code,
#                 'data': theme_data,
#                 'score': score
#             })
    
#     # 점수 기반으로 상위 테마 선정
#     recommended = sorted(themes_info, key=lambda x: x['score'], reverse=True)[:5]
    
#     return recommended

# def analyze_mbti_risk(mbti):
#     # MBTI 기반 위험 성향 분석
#     risk_map = {
#         'ENTJ': 5, 'ENTP': 5,  # 높은 위험 성향
#         'INTJ': 4, 'INTP': 4,  # 중상 위험 성향
#         'ESTJ': 3, 'ISTJ': 3,  # 중간 위험 성향
#         'ISFJ': 2, 'ISFP': 2,  # 중하 위험 성향
#         'INFJ': 1, 'INFP': 1   # 낮은 위험 성향
#     }
#     return risk_map.get(mbti, 3)  # 기본값 3 (중간 위험)

# def get_period_weight(period):
#     # 투자 기간에 따른 가중치 설정
#     period_weights = {
#         'SHORT': 0.8,    # 단기 (1년 미만)
#         'MEDIUM': 1.0,   # 중기 (1-3년)
#         'LONG': 1.2      # 장기 (3년 이상)
#     }
#     return period_weights.get(period, 1.0)

# def calculate_theme_score(theme_data, risk_level, period_weight):
#     # 테마 점수 계산 로직
#     volatility = theme_data.get('volatility', 0)
#     growth_potential = theme_data.get('growth_potential', 0)
#     market_cap = theme_data.get('market_cap', 0)
    
#     score = (
#         (volatility * risk_level) +
#         (growth_potential * period_weight) +
#         (market_cap * 0.5)
#     ) / 3
    
#     return score















# def analyze(request):
#     # axios 통신 테스트를 위함
#     data = request.data()
#     print(data)
#     try:
#         access_token = get_access_token()
        
#         # API 호출 및 데이터 반환
#         result = get_industry_price_series(
#             access_token=access_token,
#             industry_code='0021',
#             start_date='20240601',  # YYYYMMDD 형식
#             end_date='20240630'     # YYYYMMDD 형식
#         )
        
#         # API 응답을 그대로 JSON으로 반환
#         return JsonResponse(result)
        
#     except Exception as e:
#         return JsonResponse({
#             'status': 'error',
#             'message': str(e)
#         }, status=500)