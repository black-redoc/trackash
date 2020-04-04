from django import forms
from django.urls import reverse_lazy

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML

from .models import Income


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = (
            "concept",
            "value",
            "category",
        )
        labels = {
            "concept": "Concept (required)",
            "value": "Value (required)",
            "category": "Category (required)",
        }

    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Fieldset("", "concept", "value", "category"),
            ButtonHolder(
                Submit("submit", "Save", css_class="btn btn-primary"),
                HTML(
                    '<a class="btn btn-danger ml-3" href={% url "budget:dashboard" %}>Cancel</a>'
                ),
            ),
        )
