from django.shortcuts import render, redirect
from django.utils.safestring import mark_safe

from accountmanage import models
from accountmanage.forms import adminadd


def adminList(request):
    dataDict = {}
    searchData = request.GET.get('q', "")
    if searchData:
        dataDict["userName"] = searchData
    querySet = models.Admin.objects.filter(**dataDict)
    context = {
        "querySet": querySet,
        "searchData": searchData
    }
    return render(request, 'admin_list.html', context)


def adminAdd(request):
    title = "新建管理员"
    if request.method == "GET":
        form = adminadd.AdminModelForm()
        return render(request, "change.html", {"title": title, "form": form})
    form = adminadd.AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, "change.html", {"title": title, "form": form})


def adminEdit(request, nid):
    title = "编辑管理员"
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, "error.html", {"msg": "数据不存在"})
    if request.method == "GET":
        form = adminadd.AdminEditModelForm(instance=row_object)
        return render(request, "change.html", {"form": form, "title": title})
    form = adminadd.AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
    return redirect('/admin/list/')


def adminDelete(request):
    nid = request.GET.get("nid")
    querySet = models.Admin.objects.filter(id=nid)
    if querySet:
        querySet.delete()
    else:
        return render(request, 'error.html', {"errors": "数据不存在", })
    return redirect("/admin/list")


def adminReset(request):
    nid = request.GET.get("nid")
    querySet = models.Admin.objects.filter(id=nid).first()
    print(querySet)
    if not querySet:
        return render(request, 'error.html', {"errors": "数据不存在", })
    if request.method == "GET":
        form = adminadd.AdminResetModelForm()
        return render(request, "change.html", {"form": form, "title": "重置密码"})

    form = adminadd.AdminResetModelForm(data=request.POST, instance=querySet)
    print(querySet.passWord)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, "change.html", {"form": form, "title": "重置密码"})

