from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(),  name='home'),
    path('schedule', views.SchedulePageView.as_view(),  name='schedule'),
    path('arts', views.ArtsPageView.as_view(),  name='arts'),
    path('members', views.MembersPageView.as_view(),  name='members'),
    path('rules', views.RulesPageView.as_view(),  name='rules')
]
