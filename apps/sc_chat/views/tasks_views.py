"""
@Author				: XiaoTao
@Email				: 18773993654@163.com
@Lost modifid		: 2023/9/6 14:22
@Filename			: tasks_views.py
@Description		: 
@Software           : PyCharm
"""
from rest_framework.views import APIView

from language.language_pack import RET
from sc_chat.tasks import set_ernie_access_token, set_chat_ernie_access_token, test_chat
from sv_voice.tasks import set_ali_access_token
from utils.cst_class import CstResponse


class ErnieAccessToken(APIView):
    authentication_classes = []

    def post(self, request):
        set_ernie_access_token()
        set_chat_ernie_access_token()
        return CstResponse(RET.OK)


class TestChat(APIView):
    authentication_classes = []

    def post(self, request):
        test_chat()
        return CstResponse(RET.OK)


class AliAccessToken(APIView):
    authentication_classes = []

    def post(self, request):
        set_ali_access_token()
        return CstResponse(RET.OK)
