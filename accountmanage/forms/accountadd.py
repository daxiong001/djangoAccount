from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from accountmanage import models
from accountmanage.forms.bootstrap import BootStrapModelForm


class AccountModelForm(BootStrapModelForm):
    # #   校验：方式1
    mobile = forms.CharField(
        label="手机号",
        validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')]
    )

    price = forms.CharField(min_length=0.00, max_length=9999999.99, label="价格")

    class Meta:
        model = models.Account
        """所有字段"""
        fields = "__all__"
        # fields = ["mobile", "price"]自定义字段
        # exclude = ['level]排除某些字段

    # 校验方式2
    # def clean_mobile(self):
    #     mobile = self.cleaned_data["mobile"]
    #     if 0 <= len(mobile) <= 11 and round(float(mobile), 2) is True:
    #         return mobile
    #     else:
    #         raise ValidationError("格式错误")
    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        exists = models.Account.objects.filter(mobile=mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return mobile


class AccountEditModelForm(BootStrapModelForm):
    # #   校验：方式1

    price = forms.CharField(min_length=0.00, max_length=9999999.99, label="价格")
    mobile = forms.CharField(disabled=True, label="手机号", validators=[RegexValidator(r'^1\d{10}$', '手机号格式错误')])

    class Meta:
        model = models.Account
        """所有字段"""
        fields = "__all__"
        # fields = ["price", "lever", "status"]    # 自定义字段
        # exclude = ['mobile']  # 排除某些字段

    def clean_mobile(self):
        mobile = self.cleaned_data["mobile"]
        '''排除当前的id'''
        exists = models.Account.objects.exclude(id=self.instance.pk).filter(mobile=mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return mobile
