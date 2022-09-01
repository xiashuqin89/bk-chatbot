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
import datetime
from rest_framework.response import Response
from rest_framework.decorators import action

from common.drf.validation import validation
from common.drf.view_set import BaseViewSet
from common.perm.permission import login_exempt_with_perm
from src.manager.module_notice.proto.notice import (
    ReqPostTaskBroadStratGWViewSerializer,
    ReqPostTaskBroadShareGWViewSerializer,
)
from src.manager.module_notice.models import TaskBroadcast
from src.manager.module_notice.tasks.broadcast_timer import task_broadcast


class TaskBroadcastGwViewSet(BaseViewSet):
    schema = None

    @login_exempt_with_perm
    @action(detail=False, methods=["POST"])
    @validation(ReqPostTaskBroadStratGWViewSerializer)
    def start(self, request, *args, **kwargs):
        payload = request.payload
        broadcast_params = {
            "start_user": payload.get("operator"),
            "biz_id": payload.get("biz_id"),
            "session_id": payload.get("session_id"),
            "platform": payload.get("platform"),
            "task_id": payload.get("task_id"),
            "share_group_list": payload.get("share_group_list", []),
        }
        broadcast_obj = TaskBroadcast.objects.create(**broadcast_params)
        task_broadcast.apply_async(kwargs={"broadcast_id": broadcast_obj.id})
        return Response({"data": []})

    @login_exempt_with_perm
    @action(detail=True, methods=["POST"])
    def stop(self, request, pk, *args, **kwargs):
        broadcast_obj = TaskBroadcast.objects.get(pk=pk)
        broadcast_obj.is_stop = True
        broadcast_obj.stop_time = datetime.datetime.now()
        broadcast_obj.save()
        return Response({"data": []})

    @login_exempt_with_perm
    @action(detail=True, methods=["POST"])
    @validation(ReqPostTaskBroadShareGWViewSerializer)
    def share(self, request, pk, *args, **kwargs):
        payload = request.payload
        share_group_list = payload.get("share_group_list")
        broadcast_obj = TaskBroadcast.objects.get(pk=pk)
        broadcast_obj.share_group_list = list({*broadcast_obj.share_group_list, *share_group_list})
        broadcast_obj.save()
        return Response({"data": []})
