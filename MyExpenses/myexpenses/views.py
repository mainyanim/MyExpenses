
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy, reverse

# Function to show the list of expenses
def exp_list(request):
    expenses = Expense.objects.all()
    return render(request, 'expenses_list.html',
                  {'expenses': expenses})

# Detailes expenses
def exp_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    return render(request, 'exp_detail.html',
                  {'expense': expense})

#Create new expense
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

#Edit already existing expense
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

#Edit the note - sometimes there are issues, has to fix
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('exp_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note_edits.html', {'form': form})

# I don't like usually mix methods and classes, but just as a possible way to delete an entry is to use generic views
class ExpDelete(DeleteView):
    model = Expense
    success_url = reverse_lazy('exp_list')

#Add note if there are no notes yet
def add_note_to_post(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.expense = expense
            note.save()
            return redirect('exp_detail', pk=expense.pk)
    else:
        form = NoteForm()
    return render(request, 'add_note_to_post.html', {'form': form})
