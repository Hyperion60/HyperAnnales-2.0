from django.shortcuts import render
from django.contrib.auth import logout

#-----------------------Begin Logout--------------------
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'authent/logout.html', locals())

#------------------------End Logout---------------------