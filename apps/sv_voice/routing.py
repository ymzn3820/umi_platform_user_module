"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/8/2 15:53
@Filename			: routing.py
@Description		: 
@Software           : PyCharm
"""
from django.urls import re_path
from apps.sv_voice import consumers

websocket_urlpatterns = [
    re_path(r"ws/ali/nls-gateway", consumers.AliWebSocketConsumer.as_asgi()),
    re_path(r"ws/baidu/realtime_asr", consumers.BaiduWebSocketConsumer.as_asgi()),

    re_path(r"ws/ali/text_to_speech", consumers.AliTTSConsumer.as_asgi()),
    # re_path(r"ws/server/sd_demo", consumers.SdDemo.as_asgi()),
]
