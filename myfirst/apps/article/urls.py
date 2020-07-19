from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('students_info/', views.students_info, name = 'students_info'),
    path('<int:article_id>/', views.detail, name = 'detail'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
    path('about/', views.about, name = 'about')
]
