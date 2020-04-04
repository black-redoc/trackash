from django import forms
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper

from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ("concept", "value", "category",)

    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy("budget:dashboard")

