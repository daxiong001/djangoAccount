from django.core.exceptions import ValidationError
from django import forms
from accountmanage import models

from accountmanage.forms.bootstrap import BootStrapModelForm
from accountmanage.utils.encrypt import md5


class LoginModelForm(BootStrapModelForm):

    code = forms.CharField(
        label="图片验证码",
        widget=forms.TextInput()
    )

    class Meta:
        model = models.Admin
        fields = ["userName", "passWord", "code"]

    # def clean_userName(self):
    #     user_name = self.cleaned_data.get("userName")
    #     exists = models.Admin.objects.filter(userName=user_name).exists()
    #     if not exists:
    #         raise ValidationError("用户名不存在")
    #     return user_name
    
    def clean_passWord(self):
        pwd = self.cleaned_data.get("passWord")
        return md5(pwd)
        
