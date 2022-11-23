from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Partie secrete
lien_mega = [
    "",
    "https://mega.nz/#!zERDQaYJ!tEgeEhYFjTHOftuKHXEBwZ3L98ra5HN2mYabAQIq-uM",
    "https://mega.nz/#!GMB3nSYb!YZuV-HUVn8Pb3K-8RB9Y-R0Q2vX9-H8H-Qu-iJPc11g",
    "https://mega.nz/#!yFBInALB!hF_YJ3Ot3CzrhMZwTnuSKQAUbsEj34cjzxaoEOt0hIM",
    "https://mega.nz/#!uZYVwYYS!YU2WfuL_xvANk3DxNuUNC58WqxEMpxkvAJEPuAHpBNU",
    "https://mega.nz/#!XNYFXAaA!jEU4cxFYrzFM6gzi9eFNeIa0gNRLgjAxk7tYM4hfAXY",
    "https://mega.nz/#!qRISxK5A!prwaIrSs9J4Wa6PPUEX5yt0gLtUiQfgbGMmaVtir-x8",
    "https://mega.nz/#!PBhyzSRA!QNdDlagboJ9khpPEKuzig9jj27fj8Xny5RPB6tXzpY4",
    "https://mega.nz/#!GZJjkYpD!4skOWxhEnfhKTeD7UZi2QLdjkIBVf81Ez3hXptNAm68",
    "https://mega.nz/#!DMwSjIpY!V35Zecg_vY0bT3gHu1-fLxbMtdWeHphv1r29JIPd9-Y",
    "https://mega.nz/#!bIhWhAqA!pbCCoP6MtVNeOI7DhlV9wJVrz6v3IxxTjcZImZW36QU",
    "https://mega.nz/#!WcwUjYqZ!uqUkzbQQ7r_coE8yS2MaStnERs_I249SWz5NLhNkjMU",
    "https://mega.nz/#!7Aom0AgD!5PmPrFLcK2vWa5Dpp_qCWnTxZ9lTW6hjez-FkDVe8Gw",
]

lien_mega_algo = [
    "",
    "https://mega.nz/file/SNwEELwa#tcSA02e0ZcXhNaY_b6OKGO_4bqj0J-SCkP6G8nZdaiM",
    "https://mega.nz/file/6Bw2RZjA#QFz5TVCs6RtS4d3C4pZ0rL0vZH4a-bJ9n-uEU-Vgsyg",
    "https://mega.nz/file/nMpgWT6D#5GLLyL4WS9y7Xck1g-O6zBeMD-gGT4KCzGhB37fpgq4",
    "https://mega.nz/file/2MxmkJbJ#zLRqfXPFii5inPb7mofbGabLX7aeh4I2ZPz5V2gaN1o",
    "https://mega.nz/file/7ZxCCZQL#iHTEgmUoxOYbpC8aOuV7rpZ86zBw_-7tDLZQAIO4kjI",
    "https://mega.nz/file/iQ5yWLJD#TY5umYLokSyifZkN2l6b94j5KSj24SjPLMOeFCgQkLo",
    "https://mega.nz/file/fIxEmJiA#qcNML2FUBq3jYG3iF8yc_TOwcnga-Xh2_ge4gaNWLzE",
    "https://mega.nz/file/uJgA3bzR#iB6BGK18kd826zfokNPsZ4q2A1SxodVY35QluC3sNOE",
    "https://mega.nz/file/iNg23JDL#kBZzS7_ZoJyAJvLYTetx5-HirIyUu4K7QuSAp5lfk0A",
    "https://mega.nz/file/3Uok3DZK#9zR7AAw8YN8i9xAAQlXkdesTNcVh7wVcFYV21l5F5Lw",
    "https://mega.nz/file/7cowwDgC#fnAXgYvZr3yx-2iom-AxWCi3VAD74gLq-nSwhWnVKN0",
    "https://mega.nz/file/7Fwkhbqb#LJwA2S5txDfuI7OY1gP3hHLPBbkjwqmg0wFa-6bv7I4",
]


@login_required(login_url="/login/")
def secret(request, matiere):
    path = "secret/"
    path += matiere
    path += ".html"
    return render(request, path)


@login_required(login_url="/login/")
def secret_index(request):
    return render(request, 'secret/index.html')


@login_required(login_url="/login/")
def mega_secret(request, matiere, Id):
    if matiere == "Algorithmique":
        return redirect(lien_mega_algo[Id], permanent=True)
    return redirect(lien_mega[Id], permanent=True)
