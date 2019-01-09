from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "inst_apps_demo/index.html"

    def get_context_data(self, **kwargs):
        return {
            "home_link": "https://www.jetbrains.com",
            "home_title": "JetBrains"
        }
