from .serializers import TransactionSerializer, UserInfoSerializer
from .models import Transaction, UserInfo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from UTD.utd import UniqueTransactionDetect
from UTD.make_parameter import *
utd_model = UniqueTransactionDetect()
# from django.http.response import HttpResponse, JsonResponse
# from rest_framework import viewsets
# from rest_framework.decorators import api_view
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from django.shortcuts import get_object_or_404
# import random

# Create your views here.


class TransactionViewAPI(APIView):
    def get(self, request):
        # queryset = UserInfo.objects.all()[0:1]
        # serializer = UserInfoSerializer(queryset, many=True)

        context = { "설명": "POST 방식으로 아래와 같은 api를 호출해주세요.",
                    "uid": "UID(ex. UID001)",
                    "tran_dt": "거래발생 시간(ex. 2020-10-12 13:42:00)",
                    "code": "업무코드 {1: 홈펌뱅킹 출금, 2: 홈펌뱅킹 입금, 3: CD/ATM 지급, 4: CD/ATM 이체출금,\
                                     5: CD/ATM 이체입금, 6: CD/ATM 입금, 7: CD/ATM 납부, 8: 오픈뱅킹 조회(사용X),\
                                     9: 오픈뱅킹 출금, 10: 오픈뱅킹 입금, 11: 지로공동망 자동이체, 12: 지로공동망 납부자자동이체 이체출금,\
                                     13: 지로공동망 납부자자동이체 이체입금, 14: CMS공동망 자동이체,}",
                    "md_type": "매체구분 {1: PC뱅킹, 2: 인터넷뱅킹, 3: 전화, 4: 휴대전화, 5: 건별이체, 6: 기타, 7: 대량이체}",
                    "wd_code": "입출구분 {0: 입금, 1: 출금}",
                    "net_code": "망구분 {0: 전자금융공동망, 1: CD/ATM, 2: 오픈뱅킹, 3: 납부자 자동이체, 4: CM 공동망}",
                    "tran_amt": "거래금액"}

        return Response(context)

    def post(self, request):
        global utd_model
        serializer = TransactionSerializer(data=request.data)  # Request의 data를 UserSerializer로 변환
        if serializer.is_valid():
            serializer.save()  # UserSerializer의 유효성 검사를 한 뒤 DB에 저장

            # 1. uid: UID(ex. UID001)
            # 2. tran_dt: 거래발생 시간(ex. 2020-10-12 13:42:00)
            # 3. code: 업무코드 {1: 홈펌뱅킹 출금, 2: 홈펌뱅킹 입금, 3: CD/ATM 지급, 4: CD/ATM 이체출금,
            #                  5: CD/ATM 이체입금, 6: CD/ATM 입금, 7: CD/ATM 납부, 8: 오픈뱅킹 조회(사용X),
            #                  9: 오픈뱅킹 출금, 10: 오픈뱅킹 입금, 11: 지로공동망 자동이체, 12: 지로공동망 납부자자동이체 이체출금,
            #                  13: 지로공동망 납부자자동이체 이체입금, 14: CMS공동망 자동이체,}
            # 4. md_type: 매체구분 {1: PC뱅킹, 2: 인터넷뱅킹, 3: 전화 4: 휴대전화, 5: 건별이체 6: 기타, 7: 대량이체}
            # 5. wd_code: 입출구분 {0: 입금, 1: 출금}
            # 6. net_code: 망구분 {0: 전자금융공동망, 1: CD/ATM, 2: 오픈뱅킹, 3: 납부자 자동이체, 4: CM 공동망}
            # 7. tran_amt: 거래금액

            # 파생변수 생성 및 전처리 순서
            # 1. 거래시간 범위 생성
            # 2. 요일 생성
            # 3. 거래시간대 생성
            # 4. 거래금액 스케일링

            data = serializer.data
            data["tran_tmrg"] = make_trantmrg(data["tran_dt"], data["net_code"])
            data["tran_weekday"] = make_tranweekday(data["tran_dt"])
            data["attime"] = make_attime(data["tran_dt"], data["net_code"])
            data["tran_amt_log"] = preprocess_amt(data["tran_amt"])
            data_list = list()
            data_list.append(data["tran_tmrg"])
            data_list.append(data["code"])
            data_list.append(data["md_type"])
            data_list.append(data["wd_code"])
            data_list.append(data["net_code"])
            data_list.append(data["tran_weekday"])
            data_list.append(data["attime"])
            data_list.append(data["tran_amt_log"])

            data_np = np.array(data_list)
            result = utd_model.predict_result(data_np)

            get_id = Transaction.objects.get(pk=serializer.data['id'])
            get_id.result = result
            get_id.save()

            get_uid = UserInfo.objects.filter(uid=data['uid']).values()[0]
            if get_uid[result] != 0:
                return Response({"tran_result": result, "adn_result": "정상"}, status=status.HTTP_201_CREATED)  # client에게 JSON response 전달
            else:
                return Response({"tran_result": result, "adn_result": "이상", "data": get_uid}, status=status.HTTP_201_CREATED)  # client에게 JSON response 전달

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
