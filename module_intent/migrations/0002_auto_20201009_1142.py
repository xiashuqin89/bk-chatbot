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

    dependencies = [
        ("module_intent", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bot",
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
                    "bot_id",
                    models.CharField(default="", max_length=128, verbose_name="机器人ID"),
                ),
                (
                    "bot_name",
                    models.CharField(default="", max_length=128, verbose_name="机器人名称"),
                ),
                (
                    "bot_type",
                    models.CharField(
                        choices=[
                            ("qq", "QQ"),
                            ("xwork", "企业微信"),
                            ("wechat", "微信"),
                            ("default", "OPSBOT"),
                        ],
                        default="default",
                        max_length=128,
                        verbose_name="机器人类型",
                    ),
                ),
                (
                    "config",
                    module_intent.models.CompressJSONField(
                        default={}, verbose_name="机器人配置"
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
                "verbose_name": "【机器人】",
                "verbose_name_plural": "【机器人】",
            },
        ),
        migrations.RemoveField(
            model_name="intent",
            name="biz_name",
        ),
        migrations.AddField(
            model_name="intent",
            name="index_id",
            field=models.BigIntegerField(default=-1, verbose_name="索引ID"),
        ),
    ]
