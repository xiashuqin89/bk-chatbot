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
        ("module_intent", "0003_auto_20201009_2222"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExecutionLog",
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
                ("intent_id", models.BigIntegerField(default=-1, verbose_name="意图ID")),
                (
                    "intent_name",
                    models.CharField(default="", max_length=128, verbose_name="技能名称"),
                ),
                (
                    "bot_name",
                    models.CharField(default="", max_length=128, verbose_name="机器人名称"),
                ),
                (
                    "bot_type",
                    models.CharField(
                        default="default", max_length=128, verbose_name="机器人类型"
                    ),
                ),
                (
                    "platform",
                    models.CharField(
                        default="JOB", max_length=128, verbose_name="平台名称"
                    ),
                ),
                (
                    "task_id",
                    models.CharField(
                        default="JOB", max_length=128, verbose_name="任务ID"
                    ),
                ),
                (
                    "sender",
                    models.CharField(default="", max_length=128, verbose_name="执行人"),
                ),
                ("msg", models.TextField(default="", verbose_name="调用信息")),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("0", "初始状态"),
                            ("1", "执行中"),
                            ("2", "执行成功"),
                            ("3", "执行失败"),
                            ("4", "执行暂停"),
                            ("5", "异常|终止"),
                        ],
                        default="0",
                        max_length=128,
                        verbose_name="任务状态",
                    ),
                ),
                (
                    "start_time",
                    models.CharField(default="", max_length=256, verbose_name="开始时间"),
                ),
                (
                    "end_time",
                    models.CharField(default="", max_length=256, verbose_name="结束时间"),
                ),
            ],
            options={
                "verbose_name": "【任务日志】",
                "verbose_name_plural": "【任务日志】",
            },
        ),
        migrations.AlterField(
            model_name="bot",
            name="bot_type",
            field=models.CharField(
                choices=[
                    ("qq", "QQ"),
                    ("xwork", "企业微信"),
                    ("wechat", "微信"),
                    ("default", "OPSBOT"),
                    ("slack", "Slack"),
                ],
                default="default",
                max_length=128,
                verbose_name="机器人类型",
            ),
        ),
        migrations.AlterField(
            model_name="intent",
            name="intent_name",
            field=models.CharField(default="", max_length=128, verbose_name="技能名称"),
        ),
    ]
