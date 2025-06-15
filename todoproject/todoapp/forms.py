from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your task here...',
                'aria-label': 'Task title'
            }
        )
    )
    
    class Meta:
        model = Task
        fields = ['title', 'completed']
        widgets = {
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
            