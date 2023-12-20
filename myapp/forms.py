from django import forms
from .models import ServiceRecord
from django.forms import TextInput, Textarea, DateInput


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = ['name', 'date', 'phone', 'message', 'selected_service']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Телефон'
            }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Комментарий'
            }),
            "text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Услуга'
            })
        }