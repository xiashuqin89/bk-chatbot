"""
TencentBlueKing is pleased to support the open source community by making
蓝鲸智云PaaS平台社区版 (BlueKing PaaSCommunity Edition) available.
Copyright (C) 2017-2018 THL A29 Limited,
a Tencent company. All rights reserved.
Licensed under the MIT License (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("module_intent", "0006_task_activities"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bot",
            name="create_by",
        ),
        migrations.RemoveField(
            model_name="bot",
            name="create_time",
        ),
        migrations.RemoveField(
            model_name="bot",
            name="is_delete",
        ),
        migrations.RemoveField(
            model_name="bot",
            name="update_time",
        ),
        migrations.RemoveField(
            model_name="intent",
            name="create_by",
        ),
        migrations.RemoveField(
            model_name="intent",
            name="create_time",
        ),
        migrations.RemoveField(
            model_name="intent",
            name="is_delete",
        ),
        migrations.RemoveField(
            model_name="intent",
            name="update_time",
        ),
        migrations.AddField(
            model_name="bot",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="创建时间"
            ),
        ),
        migrations.AddField(
            model_name="bot",
            name="created_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="创建人"
            ),
        ),
        migrations.AddField(
            model_name="bot",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AddField(
            model_name="bot",
            name="deleted_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="删除人"
            ),
        ),
        migrations.AddField(
            model_name="bot",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="描述"),
        ),
        migrations.AddField(
            model_name="bot",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="是否删除"),
        ),
        migrations.AddField(
            model_name="bot",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AddField(
            model_name="bot",
            name="updated_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="更新人"
            ),
        ),
        migrations.AddField(
            model_name="executionlog",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="创建时间"
            ),
        ),
        migrations.AddField(
            model_name="executionlog",
            name="created_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="创建人"
            ),
        ),
        migrations.AddField(
            model_name="executionlog",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AddField(
            model_name="executionlog",
            name="deleted_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="删除人"
            ),
        ),
        migrations.AddField(
            model_name="executionlog",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="描述"),
        ),
        migrations.AddField(
            model_name="executionlog",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="是否删除"),
        ),
        migrations.AddField(
            model_name="executionlog",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AddField(
            model_name="executionlog",
            name="updated_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="更新人"
            ),
        ),
        migrations.AddField(
            model_name="intent",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="创建时间"
            ),
        ),
        migrations.AddField(
            model_name="intent",
            name="created_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="创建人"
            ),
        ),
        migrations.AddField(
            model_name="intent",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AddField(
            model_name="intent",
            name="deleted_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="删除人"
            ),
        ),
        migrations.AddField(
            model_name="intent",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="描述"),
        ),
        migrations.AddField(
            model_name="intent",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="是否删除"),
        ),
        migrations.AddField(
            model_name="intent",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AddField(
            model_name="intent",
            name="updated_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="更新人"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="创建时间"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="created_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="创建人"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AddField(
            model_name="task",
            name="deleted_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="删除人"
            ),
        ),
        migrations.AddField(
            model_name="task",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="描述"),
        ),
        migrations.AddField(
            model_name="task",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="是否删除"),
        ),
        migrations.AddField(
            model_name="task",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AddField(
            model_name="task",
            name="updated_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="更新人"
            ),
        ),
        migrations.AddField(
            model_name="utterances",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="创建时间"
            ),
        ),
        migrations.AddField(
            model_name="utterances",
            name="created_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="创建人"
            ),
        ),
        migrations.AddField(
            model_name="utterances",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="删除时间"),
        ),
        migrations.AddField(
            model_name="utterances",
            name="deleted_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="删除人"
            ),
        ),
        migrations.AddField(
            model_name="utterances",
            name="description",
            field=models.TextField(blank=True, null=True, verbose_name="描述"),
        ),
        migrations.AddField(
            model_name="utterances",
            name="is_deleted",
            field=models.BooleanField(default=False, verbose_name="是否删除"),
        ),
        migrations.AddField(
            model_name="utterances",
            name="updated_at",
            field=models.DateTimeField(blank=True, null=True, verbose_name="更新时间"),
        ),
        migrations.AddField(
            model_name="utterances",
            name="updated_by",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="更新人"
            ),
        ),
        migrations.AlterField(
            model_name="bot",
            name="bot_type",
            field=models.CharField(
                choices=[
                    ("xwork", "企业微信"),
                    ("qq", "QQ"),
                    ("wechat", "微信"),
                    ("slack", "SLACK"),
                    ("default", "OPSBOT"),
                ],
                default="default",
                max_length=128,
                verbose_name="机器人类型",
            ),
        ),
    ]
