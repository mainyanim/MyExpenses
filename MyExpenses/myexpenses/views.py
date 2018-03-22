from django.views import generic
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect


def exp_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses_list.html',
                  {'expenses': expenses})

def exp_detail(request, pk):
    exp = get_object_or_404(Expense, pk=pk)
    return render(request, 'exp_detail.html',
                  {'exp': exp})

def exp_new(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.save()
            return redirect('exp_detail', pk=exp.pk)
    else:
        form = ExpenseForm()
    return render(request, 'exp_edit.html', {'form': form})


def exp_edit(request, pk):
    exp = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=exp)
        if form.is_valid():
            exp = form.save(commit=False)
            exp.save()
            return redirect('exp_detail', pk=exp.pk)
    else:
        form = ExpenseForm(instance=exp)
    return render(request, 'exp_edit.html', {'form': form})

def exp_delete(request, pk):
    exp = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = ExpenseForm(request.POST, instance=exp)
        exp.delete()
        return redirect('expenses_list.html', pk=exp.pk)
    else:
        form = ExpenseForm(instance=exp)
    return render(request, 'expenses_list.html', {'form': form})
