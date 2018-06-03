from django import forms
from .models import ProjectFeature

class FeaturesForm(forms.ModelForm):
    class Meta:
        model = ProjectFeature
        fields = ['name', 'main_category', 'backers', 'country', 'usd_goal_real', 'duration_days']

