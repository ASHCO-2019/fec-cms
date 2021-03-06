# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-08 02:04
from __future__ import unicode_literals

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0107_auto_20191213_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullwidthpage',
            name='citations',
            field=wagtail.core.fields.StreamField([('citations', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock()), ('content', wagtail.core.blocks.RichTextBlock(help_text='Use Shift + Enter to add line breaks between citation and description'))])))], blank=True, null=True),
        ),
    ]
