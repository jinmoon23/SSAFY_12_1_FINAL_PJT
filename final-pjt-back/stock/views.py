from django.shortcuts import render
from django.http import JsonResponse
from .utils import get_industry_price_series 
from utils.token import get_access_token  # 프로젝트 레벨의 token 유틸리티 import
# Create your views here.


# views.py
from django.http import JsonResponse
from .utils import get_industry_price_series
from utils.token import get_access_token

def analyze(request):
    # axios 통신 테스트를 위함
    data = request.data()
    print(data)
    try:
        access_token = get_access_token()
        
        # API 호출 및 데이터 반환
        result = get_industry_price_series(
            access_token=access_token,
            industry_code='0021',
            start_date='20240601',  # YYYYMMDD 형식
            end_date='20240630'     # YYYYMMDD 형식
        )
        
        # API 응답을 그대로 JSON으로 반환
        return JsonResponse(result)
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=500)