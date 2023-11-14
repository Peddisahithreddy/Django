# Generated by Django 4.2.7 on 2023-11-08 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sql', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Emp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, verbose_name='emp_name')),
                ('job_position', models.CharField(help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, verbose_name='job_post')),
                ('email', models.CharField(blank=True, max_length=254, verbose_name='email address')),
                ('gender', models.CharField(max_length=10, verbose_name='Gender')),
                ('age', models.IntegerField(default=0)),
                ('contact_no', models.IntegerField(default=0)),
            ],
        ),
    ]