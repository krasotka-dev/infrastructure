# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-16 16:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_v330_activitystream_instance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credential',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'credential', 'model_name': 'credential', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='credential',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'credential', 'model_name': 'credential', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='credentialtype',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'credentialtype', 'model_name': 'credentialtype', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='credentialtype',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'credentialtype', 'model_name': 'credentialtype', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='custominventoryscript',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'custominventoryscript', 'model_name': 'custominventoryscript', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='custominventoryscript',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'custominventoryscript', 'model_name': 'custominventoryscript', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'group', 'model_name': 'group', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='group',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'group', 'model_name': 'group', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='host',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'host', 'model_name': 'host', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='host',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'host', 'model_name': 'host', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'inventory', 'model_name': 'inventory', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'inventory', 'model_name': 'inventory', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='label',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'label', 'model_name': 'label', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='label',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'label', 'model_name': 'label', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'notificationtemplate', 'model_name': 'notificationtemplate', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notificationtemplate',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'notificationtemplate', 'model_name': 'notificationtemplate', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'organization', 'model_name': 'organization', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='organization',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'organization', 'model_name': 'organization', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'schedule', 'model_name': 'schedule', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'schedule', 'model_name': 'schedule', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'team', 'model_name': 'team', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'team', 'model_name': 'team', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unifiedjob',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'unifiedjob', 'model_name': 'unifiedjob', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unifiedjob',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'unifiedjob', 'model_name': 'unifiedjob', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unifiedjobtemplate',
            name='created_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'unifiedjobtemplate', 'model_name': 'unifiedjobtemplate', 'app_label': 'main'}(class)s_created+", to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='unifiedjobtemplate',
            name='modified_by',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="{'class': 'unifiedjobtemplate', 'model_name': 'unifiedjobtemplate', 'app_label': 'main'}(class)s_modified+", to=settings.AUTH_USER_MODEL),
        ),
    ]