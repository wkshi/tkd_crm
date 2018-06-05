from django.db import models

# Create your models here.


class Gym(models.Model):
    # 默认道馆编号
    # id = models.AutoField()
    # 道馆名称
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Member(models.Model):
    # 默认成员编号
    # id = models.AutoField()
    # 登记成员编号
    serial = models.CharField(max_length=8)
    # 注册日期
    registration_date = models.DateField(auto_now=True)
    # 有效日期
    validity_date = models.DateField()
    # 有效次数
    validity_count = models.IntegerField(default=0)
    # 不限制次数
    unlimited_count = models.BooleanField(default=False)
    # 照片
    # photograph = models.ImageField()
    # 姓名
    name = models.CharField(max_length=32)
    # 性别
    GENDER_CHOICES = (
        (u'M', u'Male'),
        (u'F', u'Female'),
    )
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=None)
    # 出生日期
    birthday = models.DateField()
    # 电话号码
    phone_number = models.CharField(max_length=16)
    # 所属道馆
    gym = models.ForeignKey(Gym, null=True, on_delete=models.SET_NULL)
    # 腰带级别
    BELT_CHOICES = (
        (u'-10', u'10th Gup White Belt 十级白带'),
        (u'-9', u'9th Gup White Belt With Yellow Stripe 九级白黄带'),
        (u'-8', u'8th Gup Yellow Belt 八级黄带'),
        (u'-7', u'7th Gup Yellow Belt With Green Stripe 七级黄绿带'),
        (u'-6', u'6th Gup Green Belt 六级绿带'),
        (u'-5', u'5th Gup Green Belt With Blue Stripe 五级绿蓝带'),
        (u'-4', u'4th Gup Blue Belt 四级蓝带'),
        (u'-3', u'3rd Gup Blue Belt With Red Stripe 三级蓝红带'),
        (u'-2', u'2nd Gup Red Belt 二级红带'),
        (u'-1', u'1st Gup Red Belt With Black Stripe 一级红黑带'),
        (u'1', u'1st Dan (Il Dan) Black Belt 黑带一段'),
        (u'2', u'2nd Dan (Ee Dan) Black Belt 黑带二段'),
        (u'3', u'3rd Dan (Sam Dan) Black Belt 黑带三段'),
        (u'4', u'4th Dan (Sa Dan) Black Belt 黑带四段'),
        (u'5', u'5th Dan (Oh Dan) Black Belt 黑带五段'),
        (u'6', u'6th Dan (Yook Dan) Black Belt 黑带六段'),
        (u'7', u'7th Dan (Chil Dan) Black Belt 黑带七段'),
        (u'8', u'8th Dan (Pal Dan) Black Belt 黑带八段'),
        (u'9', u'9th Dan (Koo Dan) Black Belt 黑带九段')
    )
    belt = models.CharField(max_length=4, choices=BELT_CHOICES, default=None)
    password = models.CharField(max_length=32, default=None)

    def __str__(self):
        return self.serial \
               + ' ' + self.name \
               + ' ' + self.gender \
               + ' ' + str(self.birthday) \
               + ' ' + self.phone_number \
               + ' ' + self.belt \
               + ' ' + self.gym.name \
               + ' ' + str(self.registration_date) \
               + ' ' + str(self.validity_date) \
               + ' ' + str(self.validity_count)


class Roster(models.Model):
    # 默认训练记录编号
    # id = models.AutoField()
    # 训练成员
    member = models.ForeignKey(Member, null=True, on_delete=models.SET_NULL)
    # 训练道馆
    training_gym = models.ForeignKey(Gym, null=True, on_delete=models.SET_NULL)
    # 训练日期
    training_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.member.name \
               + ' ' + self.training_gym.name \
               + ' ' + str(self.training_date)
