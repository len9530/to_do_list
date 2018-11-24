from django.urls import path,include
from . import views


app_name = 'todolist'
urlpatterns = [
    path('home/',views.home,name = '主页'),
    path('about/',views.about,name = '关于'),
    path('edit/<forloop_counter>',views.edit,name = '编辑'),
    path('del/<forloop_counter>',views.delete,name = '删除'),
    path('finish/<forloop_counter>',views.finish,name = '划掉'),
    path('reset/<forloop_counter>',views.reset,name = '重写'),
]
