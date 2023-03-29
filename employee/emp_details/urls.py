from django.urls import path
from . import views
from .views import EmpCreate, EmpList, EmpUpdate, EmpDelete, EmployeeListAPI

urlpatterns = [
    path('api_emplist', EmployeeListAPI.as_view, name='api_emplist'),
    path('',views.index,name='home'),
    path('emp-list', EmpList.as_view(), name='emp_list'),
    path('emp-create', EmpCreate.as_view(), name='emp-create'),
    path('emp-update/<int:pk>/', EmpUpdate.as_view(), name='emp-update'),
    path('emp-delete/<int:pk>/', EmpDelete.as_view(), name='emp-delete')
]
