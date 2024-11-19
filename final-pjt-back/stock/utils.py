import requests
from django.conf import settings

def get_industry_price_series(access_token, industry_code, start_date, end_date):
    """
    한국투자증권 API를 통해 업종별 종가 시계열 데이터를 가져오는 함수
    
    Args:
        industry_code (str): 업종코드 (00021: 금융업)
        start_date (str): 조회 시작일자 (YYYYMMDD)
        end_date (str): 조회 종료일자 (YYYYMMDD)
    
    Returns:
        dict: 상태 및 시계열 데이터를 포함한 JSON 형태의 응답
    """
    
    base_url = settings.KIS_BASE_URL
    path = "/uapi/domestic-stock/v1/quotations/inquire-daily-indexchartprice"
    url = f"{base_url}{path}"

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "authorization": f"Bearer {access_token}",
        "appkey": settings.KIS_APP_KEY,
        "appsecret": settings.KIS_APP_SECRET,
        "tr_id": "FHKUP03500100"
    }

    params = {
        "FID_COND_MRKT_DIV_CODE": "U",
        "FID_INPUT_ISCD": industry_code,
        "FID_INPUT_DATE_1": start_date,
        "FID_INPUT_DATE_2": end_date,
        "FID_PERIOD_DIV_CODE": "D"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if data['rt_cd'] == '0':
            price_data = []
            
            for item in data['output2']:
                price_data.append({
                    'date': item['stck_bsop_date'],
                    'close': float(item['bstp_nmix_prpr']),
                })
            
            # 날짜순으로 정렬
            price_data.sort(key=lambda x: x['date'])
            
            return {
                'status': 'success',
                'data': price_data
            }
            
        else:
            raise Exception(f"API Error: {data['msg1']}") 
            
    except requests.exceptions.RequestException as e:
        raise Exception(f"Request Failed: {str(e)}")
    except Exception as e:
        raise Exception(f"Error: {str(e)}")
    

def calculate_mbti_score(mbti, theme_code):
    """MBTI 기반 테마 점수 계산"""
    mbti_weights = {
        'I': {'PIN': 0.8, 'AID': 0.9, 'CLD': 0.7},  # 내향형: 핀테크, AI, 클라우드 선호
        'E': {'CEO': 0.9, 'FRC': 0.8, 'STM': 0.7},  # 외향형: 카리스마CEO, 프랜차이즈, 스트리밍 선호
        'N': {'VRR': 0.8, 'AID': 0.9, 'MEA': 0.7},  # 직관형: VR, AI, 메타버스 선호
        'S': {'FRC': 0.8, 'ADC': 0.7, 'UTE': 0.7},  # 감각형: 프랜차이즈, 자율주행차, 언택트 선호
        'T': {'AID': 0.9, 'SMC': 0.8, 'BAT': 0.7},  # 사고형: AI, 반도체, 배터리 선호
        'F': {'STM': 0.8, 'FRC': 0.7, 'FSH': 0.7},  # 감정형: 스트리밍, 프랜차이즈, 패션 선호
        'J': {'PIN': 0.8, 'BAT': 0.7, 'SMC': 0.7},  # 판단형: 핀테크, 배터리, 반도체 선호
        'P': {'VRR': 0.8, 'MEA': 0.7, 'STM': 0.7}   # 인식형: VR, 메타버스, 스트리밍 선호
    }
    
    score = 0
    for trait in mbti.upper():
        if trait in mbti_weights:
            score += mbti_weights[trait].get(theme_code, 0.3)
    return score / 4  # MBTI 4개 특성의 평균