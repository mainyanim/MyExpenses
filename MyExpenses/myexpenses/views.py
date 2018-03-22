from django.views import generic
from .models import *
from django.shortcuts import render

def index(request):
    num_exp = Expense.objects.all().count()
    expenses = Expense.objects.all()

    return render(
        request,
        'index.html',
        context={'num_exp': num_exp,
                 'expenses': expenses},
    )
