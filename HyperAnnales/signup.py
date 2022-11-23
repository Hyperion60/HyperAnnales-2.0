from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from HyperAnnales.forms import SignUpForm
from HyperAnnales.tokens import account_activation_token

#----------------Begin Signup---------------------
def test_ptvirg_email(email):
    for i in email:
        if i == ';':
            return False
    return True

def user_mail(email):
    mail = ""
    for i in email:
        if i == '@':
            return mail
        mail += i
    return ""

def signup_view(request):
    if request.method == 'POST':
        print("Debut process")
        form = SignUpForm(request.POST)
#        print(form)
        if form.is_valid():
            print("Debut form")
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            mail_subject=""
            current_site = get_current_site(request)
            subject = 'Activation de votre compte sur HyperAnnales'
            message = render_to_string('authent/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject="Activez votre compte HyperAnnales"
            to_email = form.cleaned_data.get('email')
            print("Debut mail")
            mail = user_mail(to_email)
            if not test_ptvirg_email(mail) or not mail:
                return HttpResponse("Erreur dans l'email entrÃ©e")
            to_email = mail + "@epita.fr"
            #print(to_mail)
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'authent/ante_valid.html')
#            return HttpResponse('Veuillez confirmer votre adresse email pour complÃ©ter votre inscription. Attention l\'email de validation a pu Ãªtre dÃ©placÃ© dans les spams !')
    else:
        form = SignUpForm()
    return render(request, 'authent/connexion.html', {'form': form})

def match_uid(uid):
    length = len(uid)
    ruid = ""
    for i in range (2, length - 1):
        ruid += uid[i]
    return ruid

def activate(request, uidb64, token):
    try:
        #uidb64 = match_uid(uidb64)
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request, 'authent/post_valid.html')
#        return HttpResponse('Merci pour la validation de votre email. Vous pouvez maintenant vous connecter.')
    else:
        return render(request, 'authent/fail_valid.html')
#        return HttpResponse("Lien d'activation invalide !")

#---------------------End Signup-----------------------
