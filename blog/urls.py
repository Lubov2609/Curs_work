
from django.urls import path,include
from django.contrib import admin
from . import views


urlpatterns =[
 # path('', views.index,name='index'),
  path('contact/',views.contact,name='contact'),
  path('menu/',views.menu,name='menu'),
  #path('blog/', views.blog, name='blog'),
 # path('reserv/',views.reserv,name='reserv'),
  path('timetable/',views.timetable,name='timetable'),
  path('reviews/',views.reviews,name='reviews'),
  path('Tur_menu/',views.MoviesView.as_view(),name='Tur_menu'),
  path('blog/',views.BlogView.as_view(),name='blog'),
  path('', views.IndexView.as_view(), name='index'),
  path("<int:pk>/",views.TurDetalView.as_view()),
  path("reviews/",views.AddReviews.as_view(),name="add_reviews"),
  path('reserv/', views.TursView.as_view(), name='reserv'),
]
