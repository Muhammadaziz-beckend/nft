from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.core.paginator import Paginator
from .models import Nft, Category, UserModel
from django.db.models import Count
from random import choice
from django.contrib.auth.models import User
from math import ceil
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(req):
    nft = Nft.objects.filter(is_sold=True)
    user_cruet_py = (
        UserModel.objects.annotate(nft_count=Count("created_by"))
        .filter(nft_count__gt=0)
        .prefetch_related("created_by")
    )

    context = {"nfts": nft, "users_with_nfts": user_cruet_py[0:3]}
    if nft:
        header_nft = choice(nft)

        context["header_nft"] = header_nft

        # print(header_nft)

    return render(req, "index.html", context=context)


def marketplace(req):

    seorch = req.GET.get("seorch", None)
    nft = Nft.objects.filter(is_sold=True)
    if seorch:
        nft = nft.filter(name__icontains=seorch)

    caunt = len(nft)

    paginator = Paginator(nft, 12)

    page = req.GET.get("page", 1)

    nft = paginator.get_page(page)

    # page_obj.
    print(nft.paginator.num_pages)

    context = {
        "colection": 1,
        "nfts": nft,
        "caunt": caunt,
        "Collections": len(Category.objects.all()),
    }

    return render(req, "marketplace.html", context=context)


def marketplace_collection(req):

    collections = Category.objects.all()

    seorch = req.GET.get("seorch", None)

    if seorch:
        collections = collections.filter(name__icontains=seorch)

    pade_num = req.GET.get("page", 1)

    page_obj = Paginator(collections, 12)

    collections = page_obj.get_page(pade_num)

    caunt = len(Nft.objects.filter(is_sold=True))

    context = {
        "colection": 2,
        "nfts": collections,
        "caunt": caunt,
        "Collections": len(collections),
    }

    return render(req, "marketplace.html", context=context)


def deteil_nft(req, id):
    nft = get_object_or_404(Nft, pk=id, is_sold=True)
    nfts = Nft.objects.filter(created_by=nft.created_by)

    context = {"nft": nft, "nfts": nfts}

    return render(req, "detail_nft.html", context=context)


def deteil_user(req, id):

    user = get_object_or_404(UserModel, pk=id)

    nfts = Nft.objects.filter(created_by=user, is_sold=True)
    nfts_total = len(nfts)

    page_num = req.GET.get("page", 1)

    paginator = Paginator(nfts, 9)

    nfts = paginator.get_page(page_num)

    balans = 0

    for i in nfts:
        balans += ceil(i.prise)

    balans = balans.__str__()

    if len(balans) >= 4:
        balans = "999"

    context = {
        "user": user,
        "nfts": nfts,
        "nfts_total": nfts_total,
        "balans": balans,
    }

    return render(req, "detail_user.html", context=context)


@login_required(login_url="/workspace/login/")
def bey(req, id):

    nft = get_object_or_404(Nft, pk=id, is_sold=True)
    created_by = nft.created_by
    user = get_object_or_404(UserModel, user=req.user)

    if created_by == user:

        messages.error(req, "Вы не можите купить свой NFT")
        return redirect(f"workspace")

    if req.method == "POST":
        nft_bey = req.POST.get("nft_bey", None)

        if nft_bey:
            if user.balans >= nft.prise:
                # user.nfts_sold += 1 
                user.balans -= nft.prise
                user.save()

                # Увеличить баланс продавца
                created_by.balans += nft.prise
                created_by.nfts_sold += 1
                created_by.save() 
                
                nft.created_by = user
                nft.is_sold = True
                nft.save()  


                messages.success(req, "Поздравляем! Вы успешно купили NFT.")
                return redirect("workspace")  
            else:
                messages.warning(
                    req, f"Вам не хватает {nft.prise - user.balans} на балансе."
                )

    context = {
        "nft": nft,
    }

    return render(req, "workspace/bey.html", context=context)
