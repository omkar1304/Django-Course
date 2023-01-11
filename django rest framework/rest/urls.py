from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken import views as auth_views
from .views import SongViewSet, SingerViewSet, CodeViewSet, AnimeViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router2 = DefaultRouter()
router2.register('singer-viewset', SingerViewSet, basename='singer')
router2.register('song-viewset', SongViewSet, basename='song')


router3 = DefaultRouter()
router3.register('code', CodeViewSet, basename='codeviewset')

router4 = DefaultRouter()
router4.register('anime', AnimeViewSet, basename='animeviewset')


urlpatterns = [
    # path('productapi/', views.productlistview, name='productlistview'),
    path('productlistapif/', views.productListAPIView, name='productlistapif'),
    path('productlistapi/', views.ProductListAPIView.as_view(), name='productlistapi'),
    path('productlistcreateapi/', views.ProductListCreateAPIView.as_view(), name='productlistcreateapi'),

    path('productdetailapi/<int:pk>/', views.ProductDetailAPIView.as_view(), name='productdetailapi'),

    path('productcreateapi/', views.ProductCreateAPIView.as_view(), name='productcreateapi'),

    path('productupdateapi/<int:pk>', views.ProductUpdateAPIView.as_view(), name='productupdateapi'),

    path('productdeleteapi/<int:pk>', views.ProductDestoryAPIView.as_view(), name='productdeleteapi'),


    # generic API view -> just using 2 urls we can handle CRUD operations in geneeric + minxin view
    path('productgenericapi/', views.ProductGenericAPIView.as_view(), name='productgenericapilist'),
    path('productgenericapi/<int:pk>', views.ProductGenericAPIView.as_view(), name='productgenericapidetail'),

    # to get token ->
    path('auth/', auth_views.obtain_auth_token),

    path('sesssion/', include('rest_framework.urls')),

    path('viewset/', include('rest.routers')),

    path('viewset2/', include(router2.urls)),

    # For JWT authentication
    path('viewset3/', include(router3.urls)),
    path('obtaintoken/', TokenObtainPairView.as_view(), name='obtaintoken'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refreshtoken'),

    path('personAPIView/', views.personAPIView, name='personAPIView'),
    path('personAPIView/<int:pk>', views.personAPIView, name='personAPIView1'),

    # for search, ordering, filter functaionality
    path('viewset4/', include(router4.urls)),

]



