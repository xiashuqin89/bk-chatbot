# Generated by Django 2.2.16 on 2022-08-18 20:08

import common.models.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('module_other', '0008_imtypemodel_im_type_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imtypemodel',
            name='define',
            field=common.models.json.DictCharField(blank=True, default=[], null=True),
        ),
    ]
