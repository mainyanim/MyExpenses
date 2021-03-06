from django import forms

from .models import *

class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ('date', 'title', 'desc', 'price')

class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ('text',)