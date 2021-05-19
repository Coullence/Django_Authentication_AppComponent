

from django.urls import path
# from .views import articles_data, article_detail, ArticlesMain, ArticleDetail
from .views import GenericAPIView, StationsAPIView, CustomersAPIView, ItemsAPIView, PaymentsAPIView
 
urlpatterns = [
    # path('', articles_data),
    # path('', ArticlesMain.as_view()),
    path('',GenericAPIView.as_view()),
    path('<int:id>/',GenericAPIView.as_view()),


    path('stations/',StationsAPIView.as_view()),
    path('stations/<int:id>/',StationsAPIView.as_view()),

    path('customers/',CustomersAPIView.as_view()),
    path('customers/<int:id>/',CustomersAPIView.as_view()),


    path('items/',ItemsAPIView.as_view()),
    path('items/<int:id>/',ItemsAPIView.as_view()),
    
    path('payments/',PaymentsAPIView.as_view()),
    path('payments/<int:id>/',PaymentsAPIView.as_view()),

    # path('<int:pk>', article_detail),
    # path('detail/<int:id>/', ArticleDetail.as_view()),

]
  