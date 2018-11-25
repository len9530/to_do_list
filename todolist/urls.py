from django.urls import path,include
from . import views


app_name = 'todolist'
urlpatterns = [
    path('home/',views.home,name = '主页'),
    path('about/',views.about,name = '关于'),
    path('edit/<i_id>',views.edit,name = '编辑'),
    path('del/<i_id>',views.delete,name = '删除'),
    path('finish/<i_id>',views.finish,name = '划掉'),
    path('reset/<i_id>',views.reset,name = '重写'),
]
