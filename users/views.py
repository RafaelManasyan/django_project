from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm


class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('catalog:main')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в систему!'
        message = 'Спасибо, что зарегистрировались'
        recipient_list = [user_email]
        from_email = 'tmanasyan777@mail.ru'
        send_mail(subject, message, from_email, recipient_list)
