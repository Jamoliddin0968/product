# Generated by Django 4.1.5 on 2023-03-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_alter_category_image_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(help_text="rasm o'lchami 2533x1105 nisbatda bo'lishi kerak", upload_to='category/', verbose_name='Rasm'),
        ),
    ]
