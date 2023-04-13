from django.db import models

# Create your models here.
class UserInfo(models.Model):
        name = models.CharField(max_length=32)
        password = models.CharField(max_length=64)
        age = models.IntegerField()

        # 新增字段时可以选择默认值
        # num = models.IntegerField(default=2)
        # data = models.IntegerField(null=True,blank=True)

class Department(models.Model):
        title = models.CharField(max_length=16)

class Role(models.Model):
        caption = models.CharField(max_length=16)

# 表字段写入数据库
# python manage.py makemigrations --empty app01
# 如果出现No changes detected 说明没注册则需要加入 --empty app01
# python manage.py migrate

# 新增数据 insert into
# Department.objects.create(title='销售部')