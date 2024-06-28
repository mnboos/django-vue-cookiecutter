from django.urls import path

from . import views


app_name = 'rewards'
urlpatterns = [
    path('', views.RewardsListView.as_view(), name='list'),
    path('claim/', views.RewardsClaimView.as_view(), name='claim'),
    path('bonus/', views.RewardsBonusView.as_view(), name='bonus'),
]
