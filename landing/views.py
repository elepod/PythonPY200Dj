from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from landing.forms import TemplateForm


class LandingTemplView(TemplateView):
    template_name = 'landing/index.html'

    def post(self, request, *args, **kwargs):
        received_data = request.POST  # Приняли данные в словарь

        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():  # Проверили, что данные все валидные
            name = form.cleaned_data.get("name")
            message = form.cleaned_data.get("message")
            email = form.cleaned_data.get("email")
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')

            return JsonResponse(data=[name, message, email, ip, user_agent],
                                safe=False,
                                json_dumps_params={'ensure_ascii': False, 'indent': 4},
                                )

        context = self.get_context_data(**kwargs)  # Получаем контекст, если он есть
        context["form"] = form  # Записываем в контекст форму
        return self.render_to_response(context)  # Возвращаем вызов метода render_to_response

