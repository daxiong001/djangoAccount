from django.db import models


# Create your models here.
class Account(models.Model):
    class Meta:
        db_table = "account"
    mobile = models.CharField(verbose_name='手机号码', max_length=11)
    price = models.DecimalField(verbose_name='价格', max_digits=11, decimal_places=2, default=0)
    lever_choice = (
        (1, "一级"),
        (2, "二级"),
        (3, "三级")
    )
    lever = models.SmallIntegerField(verbose_name="级别", choices=lever_choice, default=1)
    status_choice = (
        (1, "未占用"),
        (2, "已占用"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choice, default=1)


class Admin(models.Model):

    class Meta:
        db_table = "admin"
    userName = models.CharField(verbose_name="用户名", max_length=32)
    passWord = models.CharField(verbose_name="密码", max_length=64)