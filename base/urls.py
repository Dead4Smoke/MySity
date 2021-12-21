from django.urls import path
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.office, name='office'),
    path('tab0', views.tab0, name='tab0'),
    path('tab1', views.tab1, name='tab1'),
    path('tab2', views.tab2, name='tab2'),
    path('tab3', views.tab3, name='tab3'),
    path('card', views.cards, name='card'),
    path('search/', SearchResultsView.as_view(), name='search'),
    path('region/', views.region, name='region'),
    path('statistical/', views.statistical ,name='statistical'),
    path('downloadtabreg', views.downloadtabreg, name='downloadtabreg'),
    path('downloadtab0', views.downloadtab0, name='downloadtab0'),
    path('downloadtab1', views.downloadtab1, name='downloadtab1'),
    path('downloadtab2', views.downloadtab2, name='downloadtab2'),
    path('downloadtab3', views.downloadtab3, name='downloadtab3'),

]

