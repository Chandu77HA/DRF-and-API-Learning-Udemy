
from django.urls import path, include
from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (MovieListAV, MovieDetailAV, WatchListAV, WatchDetailAV, 
                                     StreamPlatformAV, StreamPlatformDetailAV, ReviewList, ReviewDetail,
                                     ConcreteReviewList, ConcreteReviewDetail, ConcreteWatchList,
                                     ConcreteWatchListDetail, ConcreteStreamPlatform, ConcreteStreamPlatformDetail,
                                     ConcreteWatchReviewList, ConcreteWatchReviewDetail, ConcreteWatchReviewCreate,
                                     StreamPlatformViewset, StreamPlatformMV, ReviewMV, ReviewROMV)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('routerstreamplatform', StreamPlatformViewset, basename = 'router-stream-platform'),
router.register('routerstreamplatformmv', StreamPlatformMV, basename = 'router-stream-platform-mv'),
router.register('routerreviewmv', ReviewMV, basename = 'router-review-mv'),
router.register('routerreviewromv', ReviewROMV, basename = 'router-review-romv'),



urlpatterns = [

    #function views
    path('list/', movie_list, name = 'movie_list'),
    path('detail/<int:pk>/', movie_details, name = 'movie_detail'),

    #class based viewsConcreteWatchListDetail
    path('classlist/', MovieListAV.as_view(), name = 'class_movie_list'),
    path('classmoviedetail/<int:pass_pk>/', MovieDetailAV.as_view(), name = 'class_movie_detail'),

    #after updated model
    path('watchlist/', WatchListAV.as_view(), name = 'watch_list'),
    path('watchdetail/<int:pk>/', WatchDetailAV.as_view(), name = 'watch_detail'),
    path('streamplatform/', StreamPlatformAV.as_view(), name = 'stream_platform'),
    path('streamdetail/<int:pk>/', StreamPlatformDetailAV.as_view(), name = 'stream_detail'),

    #Generic API Views and Mixins
    path('review/', ReviewList.as_view(), name = 'review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(), name = 'review_detail'),

    #Concrete view classes for Review Model
    path('reviewconcrete/', ConcreteReviewList.as_view(), name = 'review_list_concrete'),
    path('reviewconcrete/<int:pk>/', ConcreteReviewDetail.as_view(), name = 'review_detail_concrete'),

    #Concrete view classes for Watchlist and StreamPlatform Model
    path('watchlistconcrete/', ConcreteWatchList.as_view(), name = 'watch_list_concrete'),
    path('watchdetailconcrete/<int:pk>/', ConcreteWatchListDetail.as_view(), name = 'watch_detail_concrete'),
    path('streamplatformconcrete/', ConcreteStreamPlatform.as_view(), name = 'stream_platform_concrete'),
    path('streamdetailconcrete/<int:pk>/', ConcreteStreamPlatformDetail.as_view(), name = 'stream_detail_concrete'),

    # Concrete view classes to get reviews of particular movie

    # Authentication Views
    path('watch/<int:trykey>/review-create/', ConcreteWatchReviewCreate.as_view(), name = 'watch_list_review_create'),
    path('watch/<int:passkey>/review/', ConcreteWatchReviewList.as_view(), name = 'watch_list_review'),
    path('watch/review/<int:pk>/', ConcreteWatchReviewDetail.as_view(), name = 'watch_list_review'),

    # url for include router
    path('', include(router.urls)),


]