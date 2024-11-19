from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_industry_price_series 
from utils.token import get_access_token  # 프로젝트 레벨의 token 유틸리티 import
# Create your views here.


# views.py
from django.http import JsonResponse
from .utils import get_industry_price_series
from utils.token import get_access_token


# 혜령 디버깅 추가
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

# CSRF 보호 비활성화
@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        try:
            # 요청의 body에서 JSON 데이터를 로드
            data = json.loads(request.body)

            # 요청 데이터 출력 (테스트용)
            print(f"MBTI: {data.get('mbti')}")
            print(f"Interest: {data.get('interest')}")
            print(f"Period: {data.get('period')}")

            # 분석 로직 처리 후 결과 반환 (예시)
            response_data = {
                'status': 'success',
                'message': '분석 요청이 성공적으로 처리되었습니다.',
                'recommended_themes': ['테마1', '테마2', '테마3', '테마4', '테마5', '테마6']
            }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': '잘못된 JSON 형식입니다.'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'GET 요청은 허용되지 않습니다.'}, status=405)

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