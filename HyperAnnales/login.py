from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


#--------------------Begin Login-----------------------
def login_view(request):
    context = {}
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect_to = request.GET.get('next', '')
            print(request.GET)
            if redirect_to == 'None':
                redirect_to = '/'
            try:
                test_user = User.objects.get(username = user)
            except test_user.DoesNotExist:
                context['error'] = 'Pseudo non trouvé'
            if not user.is_authenticated:
                context['error'] = 'Erreur dans le mot de passe'
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        redirect_to = request.GET.get('next')
        print(redirect_to)
        form = AuthenticationForm()
    return render(request, 'authent/login.html', locals())

#------------------------End Login----------------------
