# Generated by Django 2.0.7 on 2020-07-14 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('in_stock', models.IntegerField(blank=True, null=True)),
                ('out_of_stock', models.IntegerField(blank=True, null=True)),
                ('admission', models.IntegerField()),
                ('decommission', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'Приход',
            },
        ),
        migrations.CreateModel(
            name='EquipmentWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('inven_num', models.CharField(max_length=50, null=True, unique=True)),
                ('eq_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admission_e', to='inventory.Admission')),
            ],
            options={
                'db_table': 'ЗакрепленноеЗаСотрудником',
            },
        ),
        migrations.CreateModel(
            name='Relocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('inven_num', models.CharField(max_length=50, null=True)),
                ('relocation_date', models.DateField()),
                ('movereason', models.CharField(max_length=50, null=True)),
                ('id_type', models.CharField(max_length=50)),
                ('eq_name', models.CharField(max_length=50)),
                ('id_previous_room', models.CharField(max_length=50)),
                ('previous_user', models.CharField(blank=True, max_length=50)),
                ('current_user', models.CharField(blank=True, max_length=50, null=True)),
                ('upload', models.CharField(blank=True, max_length=50, null=True)),
                ('id_current_room', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'ИсторияПеремещений',
                'ordering': ['-relocation_date'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'db_table': 'Кабинет',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
            options={
                'db_table': 'Тип',
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to='media')),
                ('date', models.DateField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'Накладные',
            },
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('full_name', models.CharField(blank=True, db_index=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Сотрудники',
                'ordering': ['full_name'],
            },
        ),
        migrations.AddField(
            model_name='equipmentworker',
            name='id_room',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='room_e', to='inventory.Room'),
        ),
        migrations.AddField(
            model_name='equipmentworker',
            name='id_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type_e', to='inventory.Type'),
        ),
        migrations.AddField(
            model_name='equipmentworker',
            name='id_workers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workers_e', to='inventory.Workers'),
        ),
        migrations.AddField(
            model_name='equipmentworker',
            name='upload',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='upload_e', to='inventory.Upload'),
        ),
        migrations.AddField(
            model_name='admission',
            name='id_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='type', to='inventory.Type'),
        ),
        migrations.AddField(
            model_name='admission',
            name='upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Upload'),
        ),
    ]
