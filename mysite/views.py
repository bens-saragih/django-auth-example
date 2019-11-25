from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


class my_view(PermissionRequiredMixin,TemplateView):
    permission_required = 'auth.add_user'
    template_name = 'email.html'

class myview(UserPassesTestMixin,TemplateView):
    login_url = '/secret/'
    template_name = 'email.html' 
    def test_func(self):
        return self.request.user.email.endswith('ben@to.id')

@user_passes_test(lambda user: Group.objects.get(name='penulis') in user.groups.all(),login_url='/signup/')
def izin(request):
    return render(request,'izin.html')

def email_check(useras):
    return user.email.endswith('bento@oke.id')

@user_passes_test(email_check,login_url='/signup/')
def my_view(request):
    return render(request,'email.html')

def home(request):
	count = User.objects.count()
	return render(request,'home.html',{
		'count':count
		})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })

@login_required
def secret_page(request):
    return render(request,'secret_page.html')

class secretpage2(LoginRequiredMixin,TemplateView):
    template_name = 'secret_page2.html'
    redirect_field_name = 'secret'

"""def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
    else:
        return('change.html')

    return render(request,'change.html',{'form':form})"""