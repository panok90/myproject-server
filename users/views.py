from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket


class Login(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context['title'] = 'GeekShop- Авторизация'
        return context


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'title': 'GeekShop- Регистрация', 'form': form}
    return render(request, 'users/registration.html', context)


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно изменили личные данные!')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=user)
    context = {'title': 'GeekShop- Личный кабинет',
               'form': form,
               'baskets': Basket.objects.filter(user=user),
               'total_quantity': Basket.total_quantity(user),
               'total_sum': Basket.total_sum(user)}
    return render(request, 'users/profile.html', context)


class Logout(LogoutView):
    pass
