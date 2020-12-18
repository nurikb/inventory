from django.db import models


# Create your models here.
class  Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    class Meta:
        db_table = "Тип"
    def __str__(self):
        return '{}'.format(self.name)


class Room(models.Model):
    number = models.CharField(max_length=100, db_index=True)
    def __str__(self):
        return '{}'.format(self.number)
    class Meta:
            db_table = "Кабинет"

class Workers(models.Model):
    first_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    full_name = models.CharField(max_length=100, db_index=True, null=True, blank=True)
    def __str__(self):
        return '{}'.format(self.full_name)
    def save(self, *args, **kwargs):
        self.full_name = self.first_name+' '+self.name+' '+self.last_name
        super().save(*args, **kwargs)
    class Meta:
        db_table = "Сотрудники"
        ordering = ['full_name']


class Admission(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    in_stock = models.IntegerField(null=True, blank=True)
    out_of_stock = models.IntegerField(null=True, blank=True)
    admission = models.IntegerField()
    decommission = models.IntegerField(null=True, blank=True)
    upload = models.ForeignKey(
        'Upload',
        null=True,
        on_delete=models.SET_NULL,
        related_name='type'
        )
    id_type= models.ForeignKey(
    'Type',
    null=True,
    on_delete=models.SET_NULL,
    related_name='type'
    )

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        db_table = "Приход"


class Relocation(models.Model):
    count = models.IntegerField()
    inven_num = models.CharField(max_length=50, null=True)
    relocation_date = models.DateField()
    movereason= models.CharField(max_length=50, null=True)
    id_type= models.CharField(max_length=50)
    eq_name = models.CharField(max_length=50)
    id_previous_room= models.CharField(max_length=50)
    previous_user = models.CharField(max_length=50, blank=True)
    current_user= models.CharField(max_length=50, blank = True, null=True,)
    upload = models.CharField(max_length=50, blank=True, null=True)
    id_current_room= models.CharField(max_length=50)
    class Meta:
        db_table = "ИсторияПеремещений"
        ordering = ['-relocation_date']

class EquipmentWorker(models.Model):
    date = models.DateField()
    inven_num = models.CharField(max_length=50, null=True)
    upload = models.ForeignKey(
    'Upload',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='upload_e'
    )
    eq_name = models.ForeignKey(
    'Admission',
    on_delete=models.CASCADE,
    related_name='admission_e'
    )
    id_type= models.ForeignKey(
    'Type',
    blank = True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='type_e'
    )
    id_workers= models.ForeignKey(
    'Workers',
    blank = True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='workers_e'
    )
    id_room= models.ForeignKey(
    'Room',
    blank = True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='room_e'
    )
    class Meta:
        db_table = "ЗакрепленноеЗаСотрудником"

class Upload(models.Model):
    name = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='media')
    date = models.DateField(auto_now=True, null=True)
    def __str__(self):
        return '{}'.format(self.name)
    class Meta:
        db_table = "Накладные"
