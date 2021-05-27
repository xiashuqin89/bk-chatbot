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
import module_intent.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Intent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "biz_id",
                    models.PositiveIntegerField(
                        db_index=True, default=0, verbose_name="业务ID"
                    ),
                ),
                (
                    "biz_name",
                    models.CharField(default="", max_length=128, verbose_name="业务名称"),
                ),
                (
                    "intent_name",
                    models.CharField(default="", max_length=128, verbose_name="业务名称"),
                ),
                ("status", models.BooleanField(default=False, verbose_name="意图状态")),
                (
                    "available_user",
                    module_intent.models.CompressJSONField(
                        default=[], verbose_name="可执行用户"
                    ),
                ),
                (
                    "available_group",
                    module_intent.models.CompressJSONField(
                        default=[], verbose_name="可执行群组"
                    ),
                ),
                ("is_delete", models.BooleanField(default=False, verbose_name="是否已删除")),
                (
                    "create_by",
                    models.CharField(default="-", max_length=100, verbose_name="创建人"),
                ),
                (
                    "create_time",
                    models.DateTimeField(auto_now=True, verbose_name="创建时间"),
                ),
                (
                    "update_time",
                    models.DateTimeField(auto_now=True, verbose_name="更新时间"),
                ),
            ],
            options={
                "verbose_name": "【意图】",
                "verbose_name_plural": "【意图】",
            },
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "biz_id",
                    models.PositiveIntegerField(
                        db_index=True, default=0, verbose_name="业务ID"
                    ),
                ),
                ("index_id", models.BigIntegerField(default=-1, verbose_name="索引ID")),
                (
                    "platform",
                    models.CharField(
                        choices=[
                            ("JOB", "JOB"),
                            ("SOPS", "标准运维"),
                            ("DEVOPS", "蓝盾"),
                            ("DEFINE", "自定义"),
                        ],
                        default="JOB",
                        max_length=128,
                        verbose_name="平台名称",
                    ),
                ),
                (
                    "task_id",
                    models.CharField(
                        default="JOB", max_length=128, verbose_name="任务ID"
                    ),
                ),
                (
                    "slots",
                    module_intent.models.CompressJSONField(
                        default=[], verbose_name="槽位信息"
                    ),
                ),
                (
                    "source",
                    module_intent.models.CompressJSONField(
                        default={}, verbose_name="任务元数据"
                    ),
                ),
                ("script", models.TextField(default="", verbose_name="执行脚本信息")),
            ],
            options={
                "verbose_name": "【任务信息】",
                "verbose_name_plural": "【任务信息】",
            },
        ),
        migrations.CreateModel(
            name="Utterances",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "biz_id",
                    models.PositiveIntegerField(
                        db_index=True, default=0, verbose_name="业务ID"
                    ),
                ),
                ("index_id", models.BigIntegerField(default=-1, verbose_name="索引ID")),
                (
                    "content",
                    module_intent.models.CompressJSONField(
                        default=[], verbose_name="语料列表"
                    ),
                ),
            ],
            options={
                "verbose_name": "【语料库】",
                "verbose_name_plural": "【语料库】",
            },
        ),
    ]
