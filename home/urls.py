from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('cause/', views.cause, name='cause'),
    path('cause_1/', views.cause_1, name='cause_1'),
    path('cause_2_0/', views.cause_2_0, name='cause_2_0'),
    path('cause_2_1/', views.cause_2_1, name='cause_2_1'),
    path('cause_2_2/', views.cause_2_2, name='cause_2_2'),
    path('cause_2_3/', views.cause_2_3, name='cause_2_3'),
    path('cause_2_4/', views.cause_2_4, name='cause_2_4'),
    path('cause_2_5/', views.cause_2_5, name='cause_2_5'),
    path('cause_2_6/', views.cause_2_6, name='cause_2_6'),

    path('plantif/', views.plaintiff, name='plaintiff'),
    path('defendant/', views.defendant, name='defendant'),
    path('court_hearing/', views.court_hearing, name='court_hearing'),
]