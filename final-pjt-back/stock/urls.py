from django.urls import path
from . import views

urlpatterns = [
    path('token/',views.get_token),
    path('stock/analyze/',views.analyze),
    path('stock/indus_chart/',views.draw_theme_chart),
    # 아래의 호출로 article 전체 조회(front에서는 최신순 5개만 보여주기)
    # 커뮤니티 버튼 클릭 시 아래의 호출 재활용
    path('stock/d_chart_and_data/',views.d_chart_and_data),
    path('stock/o_chart_and_data/',views.o_chart_and_data),
    path('stock/d_chart_period/',views.d_chart_period),
    path('stock/o_chart_period/',views.o_chart_period),
    path('stock/same_mbti/',views.get_same_mbti_theme),
    path('stock/article/create/',views.create_stock_article),
    path('stock/article/update_or_delete/',views.stock_article_delete_or_put),
    # 아래의 호출로 article detail로 이동 및 해당 게시글의 comment 전달
    path('stock/article/detail/',views.get_stock_article_detail),
    path('stock/article/detail/delete_or_put',views.comment_update_delete),
]
