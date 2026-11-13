
from django.contrib import admin
from django.urls import path
from tasks import views

app_name= 'tasks'

urlpatterns = [
    path('', views.tasks_list, name='list'),
    path('admin/', admin.site.urls),
    path('about/', views.tasks_about, name='about'),
    path('detail/<int:pk>', views.tasks_detail, name='detail')

]
