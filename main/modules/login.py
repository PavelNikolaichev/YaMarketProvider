from pprint import pprint

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.urls import reverse
from django.shortcuts import redirect

from main.forms.user import UserLoginForm
from main.views import Page, get_navbar


class MyLoginFormView(FormView):
    """отображение авторизации"""

    form_class = UserLoginForm
    template_name = Page.login
    context = {'title': 'Login', 'page_name': 'Авторизация'}

    def get(self, request, *args, **kwargs):
        self.context['navbar'] = get_navbar(request)
        self.context['form'] = self.get_context_data()['form']
        pprint(self.context)
        return self.render_to_response(self.context)

    def form_invalid(self, form):
        return self.get(self.request)

    def form_valid(self, form):
        user = authenticate(username=form.data.get('username'), password=form.data.get('password'))
        login(self.request, user)
        messages.success(self.request, 'Авторизация прошла успешно')
        return redirect(reverse('index'))
