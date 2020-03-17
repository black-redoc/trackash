from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class BudgetConfig(AppConfig):
    name = "trackash.budget"
    verbose_name = _("Budget")

    def ready(self):
        try:
            import trackash.budget.signals  # noqa F401
        except ImportError:
            pass
