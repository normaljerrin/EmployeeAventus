from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializer import EmployeeSerializer
from .models import Employee
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.


def index(request):
    return render(request, 'index.html')


def datatable_view(request):
    return render(request, 'datatable.html')


class EmployeeListAPI(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmpList(ListView):
    model = Employee
    context_object_name = 'emp_list'
    template_name = 'emp_list.html'


class EmpCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('emp_list')
    template_name = 'emp-create.html'


class EmpUpdate(UpdateView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee')
    template_name = 'emp-create.html'


class EmpDelete(DeleteView):
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee')
    template_name = 'emp-delete.html'
