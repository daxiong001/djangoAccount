from django import forms
from django.core.exceptions import ValidationError

from accountmanage.forms.bootstrap import BootStrapModelForm
from accountmanage import models
from accountmanage.utils.encrypt import md5


class AdminModelForm(BootStrapModelForm):
    confirmPassword = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["userName", "passWord", "confirmPassword"]
        widgets = {
            "passWord": forms.PasswordInput(render_value=True)
        }

    def clean_passWord(self):
        pwd = self.cleaned_data.get("passWord")
        return md5(pwd)

    def clean_confirmPassword(self):
        pwd = self.cleaned_data.get("passWord")
        print(pwd)
        confirmPassword = md5(self.cleaned_data.get("confirmPassword"))
        print(confirmPassword)
        if confirmPassword != pwd:
            raise ValidationError("两次密码输入不一致")
        return confirmPassword


class AdminEditModelForm(BootStrapModelForm):
    userName = forms.CharField(min_length=3, max_length=15, label='用户名')

    class Meta:
        model = models.Admin
        fields = ["userName"]


class AdminResetModelForm(BootStrapModelForm):
    confirmPassword = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["passWord", "confirmPassword"]
        widgets = {
            "passWord": forms.PasswordInput(render_value=True)  # 提交后保留输入框数据
        }

    def clean_passWord(self):
        pwd = self.cleaned_data.get("passWord")
        # 校验新密码与当前密码是否一致
        exist = models.Admin.objects.filter(id=self.instance.pk, passWord=md5(pwd)).exists()
        if exist:
            raise ValidationError("新密码不能与当前密码一致")
        return md5(pwd)

    def clean_confirmPassword(self):
        pwd = self.cleaned_data.get("passWord")
        print(pwd)
        confirmPassword = md5(self.cleaned_data.get("confirmPassword"))
        print(confirmPassword)
        if confirmPassword != pwd:
            raise ValidationError("两次密码输入不一致")
        return confirmPassword
