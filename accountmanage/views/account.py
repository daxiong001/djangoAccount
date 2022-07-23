from io import BytesIO

from django.shortcuts import render, redirect, HttpResponse
from django.utils.safestring import mark_safe

from accountmanage import models
from accountmanage.forms import adminadd, loginform
from accountmanage.utils.code import check_code


def login(request):
    if request.method == "GET":
        form = loginform.LoginModelForm()
        return render(request, 'login.html', {"form": form})

    form = loginform.LoginModelForm(data=request.POST)
    if form.is_valid():
        user_input_code = form.cleaned_data.pop('code')
        code = request.session.get("image_code", "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {"form": form})
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            form.add_error("passWord", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})
        request.session["info"] = {"id": admin_object.id, "name": admin_object.userName}
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/admin/list/")
    return render(request, 'login.html', {"form": form})


def logout(request):
    request.session.clear()
    return redirect("/login/")


def image(request):
    img, code_string = check_code()
    request.session["image_code"] = code_string
    request.session.set_expiry(60)
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue())
