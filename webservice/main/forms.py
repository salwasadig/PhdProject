from django import forms
from .models import ProjectFeature

class FeaturesForm(forms.ModelForm):
    class Meta:
        model = ProjectFeature
        fields = ['name', 'main_category', 'usd_pledged', 'country', 'usd_goal_real', 'duration_days']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'main_category': forms.Select(attrs={'class': 'form-control'}),
            'usd_pledged': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'usd_goal_real': forms.TextInput(attrs={'class': 'form-control'}),
            'duration_days': forms.TextInput(attrs={'class': 'form-control'}),
        }