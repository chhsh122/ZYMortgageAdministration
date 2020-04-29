from django.db import models


# Create your models here.

class Record(models.Model):
    name = models.CharField(verbose_name='收支项', max_length=128, help_text='每一笔款项描述')
    money = models.DecimalField(verbose_name='金额', decimal_places=2, max_digits=9)
    file = models.FileField(verbose_name='文件',upload_to ="static/" )
    create_date = models.DateTimeField(verbose_name='时间', auto_now=True)

    type_choices = (
        (0, '收入'),
        (1, '支出'),
    )
    type = models.IntegerField(verbose_name='类型', choices=type_choices)

    class Meta:
        verbose_name = "收支"
        verbose_name_plural = "收支记录"

    # def file_link(self):
    #     return self.file
        # if self.file:
        #     return self.file.url
        # else:
        #     return "No attachment"
    # file_link.allow_tags = True
    def __str__(self):
        return self.name
