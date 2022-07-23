import random

from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from accountmanage import models
from accountmanage.forms import accountadd


# Create your views here.
def accountList(request):

    page = int(request.GET.get('page', 1))
    pageSize = 10
    start = (page-1)*pageSize
    end = page*pageSize

    """靓号列表"""
    data_dict = {}
    searchData = request.GET.get("q", "")
    if searchData:
        data_dict["mobile__contains"] = searchData
    accountAllObject = models.Account.objects.filter(**data_dict).order_by("-lever")[start:end]
    totalCount = models.Account.objects.filter(**data_dict).order_by("-lever").count()
    totalPageCount, div = divmod(totalCount, pageSize)
    if div:
        totalPageCount += 1
    pageStrList = []
    for i in range(1, totalPageCount+1):
        ele = '<li><a href="?page={}">{}</a><li>'.format(i, i)
        pageStrList.append(ele)
    pageString = mark_safe("".join(pageStrList))
    return render(request, "account_list.html", {"allAccount": accountAllObject, "searchData": searchData,
                                                 "pageString": pageString})


def accountAdd(request):
    if request.method == "GET":
        form = accountadd.AccountModelForm()
        return render(request, "change.html", {"form": form, "title": "新建用户"})
    form = accountadd.AccountModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/account/list')
    return render(request, "change.html", {"form": form})


def accountEdit(request, nid):
    thisObject = models.Account.objects.filter(id=nid).first()
    if request.method == "GET":
        form = accountadd.AccountEditModelForm(instance=thisObject)
        return render(request, "account_edit.html", {"form": form})
    form = accountadd.AccountEditModelForm(data=request.POST, instance=thisObject)
    if form.is_valid():
        form.save()
        return redirect("/account/list")
    return render(request, "account_edit.html", {"form": form})


def accountDelete(request):
    nid = request.GET.get("nid")
    models.Account.objects.filter(id=nid).delete()
    return redirect('/account/list/')
