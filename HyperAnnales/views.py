from django.shortcuts import render
from django.http import Http404

# Security robot
def robot(request):
    return HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")

#-----------------------Begin Views---------------------
def index(request):
    return render(request, 'index.html')

def promo(request, annee):
    if annee==2022:
        return render(request, '2022/index.html', locals())
    raise Http404

def url_matiere(request, annee, semestre, matiere):
    url = str(annee) + "/" + str(semestre) + "/" + str(matiere) + str(semestre) + ".html"
    return render(request, url, locals())

def docs(request):
    return render(request, 'Docs/docs.html', locals())

def url_option(request, annee, option):
    print(option)
    if option == 'S1' or option == 'S2' or option == 'S3' or option == 'S4':
        return render(request, annee + '/index.html', locals())
    path = str(annee) + "/" + option + ".html"
    return render(request, path)
