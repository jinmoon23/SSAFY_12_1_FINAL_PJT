from django.db import migrations

def link_themes_to_industry_codes(apps, schema_editor):
    Theme = apps.get_model('stock', 'Theme')
    IndustryCode = apps.get_model('stock', 'IndustryCode')
    
    # 테마와 업종 코드 매핑 정의
    theme_industry_mapping = {
        '핀테크': ['00020', '00021', '00024', '00025', '00026'],
        '언택트경제': ['00013', '00016', '00020', '00026'],
        '게임월드': ['00013', '00020', '00026'],
        '카리스마창업자': ['00016', '00026'],
        '자율주행차': ['00012', '00013', '00015'],
        '컨텐츠강자': ['00020', '00026'],
        '신나는 드라이빙': ['00012', '00015'],
        '이번 휴가는 어디?': ['00019', '00026'],
        '가상현실(VR)': ['00013', '00014', '00020'],
        '메타버스 구현': ['00013', '00020', '00026'],
        '인공지능': ['00013', '00020'],
        '클라우드': ['00013', '00020'],
        '항공우주&방위산업': ['00012', '00013', '00015'],
        '통신': ['00020'],
        '프랜차이즈': ['00005', '00016', '00026'],
        '스트리밍의 시대': ['00020', '00026'],
        '어디 옷이야?': ['00006', '00016'],
        '리튬&배터리': ['00008', '00013'],
        '반도체': ['00013'],
        '플랫폼 대표주자': ['00016', '00020', '00026'],
        '건물주의 꿈': ['00018'],
        '클린 에너지': ['00017'],
        '갈증해소': ['00005'],
        '소비/원자재': ['00008', '00010', '00011'],
        '자원/에너지': ['00008', '00017'],
        '소셜미디어': ['00020', '00026'],
        '블록체인': ['00020', '00021', '00024'],
        '리테일/유통': ['00016'],
        '사물인터넷(IOT)': ['00013', '00020'],
        '반려동물': ['00005', '00009', '00026'],
        '뷰티의 세계': ['00008', '00016', '00026']
    }

    # 각 테마별로 업종 코드 연결
    for theme_name, industry_codes in theme_industry_mapping.items():
        try:
            theme = Theme.objects.get(name=theme_name)
            industry_codes_objs = IndustryCode.objects.filter(
                api_request_code__in=industry_codes
            )
            theme.industry_codes.add(*industry_codes_objs)
        except Theme.DoesNotExist:
            print(f"Theme '{theme_name}' not found")
        except Exception as e:
            print(f"Error linking {theme_name}: {str(e)}")

def reverse_func(apps, schema_editor):
    Theme = apps.get_model('stock', 'Theme')
    # 모든 테마의 industry_codes 관계를 제거
    for theme in Theme.objects.all():
        theme.industry_codes.clear()

class Migration(migrations.Migration):
    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(link_themes_to_industry_codes, reverse_func),
    ]