from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from sendfile import sendfile
from django.shortcuts import render

# Vues de pdf

def Error404(request):
    raise Http404

def views_docs(request, title):
    path = "/home/static/pdf/docs/"
    path = path + str(title)
    print(path)
    return sendfile(request, path, attachment=False)

@login_required(login_url="/login/")
def views_files(request, annee, semestre, matiere, titre):
    #if (matiere == 'Mathematiques' or matiere == 'Physique') and semestre != 'S4' and semestre != 'S3':
    #return render(request, 'warning.html', locals())
    path = "/home/static/pdf/"
    path = path + str(annee) + "/" + str(semestre) + "/" + str(matiere) + "/"
    path = path + str(titre)
    return sendfile(request, path, attachment=False, attachment_filename=titre)

@login_required(login_url="/login/")
def download_files(request, annee, semestre, matiere, titre):
    path = "/home/static/pdf/"
    #if annee == '2023' or semestre == 'S1' or semestre == 'S2':
    #    return render(request, 'warning.html', locals())
    path = path + str(annee) + "/" + str(semestre) + "/" + str(matiere) + "/"
    path = path + str(titre)
    return sendfile(request, path, attachment=True, attachment_filename=titre)

@login_required(login_url="/login/")
def Gconfs(request, annee, matiere, titre):
    path = "/home/static/pdf/"
    path = path + str(annee) + "/" + str(matiere) + "/" + str(titre)
    return sendfile(request, path, attachment=True, attachment_filename=titre)

@login_required(login_url="/login/")
def print_code_file(request, annee, semestre, matiere, titre):
    path = "/home/static/pdf/"
    path = path + str(annee) + "/" + str(semestre) + "/" + str(matiere) + "/"
    path = path + str(titre)
    with open(path, 'r', encoding="cp1252") as pdf:
        response = HttpResponse(pdf.read(), content_type='text/plain')
        response['Content-Disposition'] = 'filename=%s' % pdf.name
        return response
    pdf.closed

@login_required(login_url="/login/")
def views_option(request, annee, option, titre):
   path = "/home/static/pdf/"
   path = path + annee + "/" + option + "/" + titre
   return sendfile(request, path, attachment=False, attachment_filename=titre)
