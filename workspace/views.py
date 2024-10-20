from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .dicarator import is_login
from .forms import RegisterForm,CreateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.paginator import Paginator
from marketplace.models import Nft,UserModel
from math import ceil

@is_login
def login_fun(req):

    form = AuthenticationForm()

    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        print(1,'\n')

        if form.is_valid():
            print(2,'\n')
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(req, user)
                messages.success(req, f'Welcome "{user.get_full_name()}"')
                return redirect("/workspace/")

    context = {
        'form':form
    }

    return render(req, "workspace/login.html", context=context)


@login_required(login_url='/workspace/login/')
def logaut_user(req):
    logout(req)

    messages.success(req, f"Good bye!")

    return redirect('main')

@is_login
def register(req):

    form =  RegisterForm()

    if req.method == 'POST':
        form = RegisterForm(data=req.POST)

        if form.is_valid():

            user = form.save()

            login(req,user)
            messages.success(req,f'Вы успешно зарегистрировалст {user.username}')
            return redirect("/workspace/")

    context = {
        'form':form,
    }

    return render(req, "workspace/register.html", context=context)

@login_required(login_url='/workspace/login/')
def index(request):
    user = UserModel.objects.get(user=request.user)
    print(user)

    nfts = Nft.objects.filter(created_by=user)
    nfts_total = len(nfts)

    page_num = request.GET.get('page',1)

    paginator = Paginator(nfts,9)

    nfts = paginator.get_page(page_num)

    balans = 0

    for i in nfts:
        balans += ceil(i.prise)

    balans = balans.__str__()

    if len(balans) >= 4:
        balans = '999'
    
    print(balans,type(balans))
    context = {
        'nfts':nfts,
        'balans':balans,
        'nfts_total':nfts_total,
        'user':user
    }

    return render(request, "workspace/index.html", context=context)

@login_required(login_url='/workspace/login/')
def plas_balans(req):
    print(req.GET)

    if req.method == 'POST':

        plas_balans_cesh = int(req.POST.get('plas_balans',0))
        if plas_balans_cesh > 0:
            user = UserModel.objects.get(user=req.user)
            user.balans += plas_balans_cesh
            user.save()

            messages.success(req,'Вы паполнили баланс на {} com'.format(plas_balans_cesh))
            return redirect('workspace')
        
        messages.error(req,'Нельзя прибавить отрецательное (-) число либо 0')

    context = {

    }

    return render(req, "workspace/plas_balans.html", context=context)



@login_required(login_url='/workspace/login/')
def create_nft(req):

    form = CreateForm()

    if req.method == 'POST':

        form = CreateForm(data=req.POST,files=req.FILES)

        if form.is_valid():
            user_form = form.save(commit=False)  # Не сохраняем форму сразу
            user_form.created_by = UserModel.objects.get(user=req.user)  # Привязываем пользователя
            user_form.save()  # Сохраняем форму и данные пользователя
            
            return redirect('workspace')

    context = {
        'form':form,
    }

    return render(req,'workspace/create.html',context=context)