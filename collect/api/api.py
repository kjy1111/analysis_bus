from urllib.parse import urlencode
from .json_request import json_request
from datetime import datetime
import sys

SERVICE_KEY = 'lPho2AedT94HdWcuLEqLx%2FxutLFprTW4diIv6lp%2FylcbEtT0TFuMSfWdSiWip2LcqZ3fRfZ4tTKNyZiU%2BKUfAw%3D%3D'
EndPoint = 'http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo'


def pd_gen_url(endpoint, **params):
    url = '%s?ServiceKey=%s&%s' % (endpoint, SERVICE_KEY, urlencode(params))
    return url


def pd_fetch_info(id):
    url = pd_gen_url(EndPoint, busRouteId=id, _type='json')
    json_result = json_request(url=url)

    json_serviceresult = json_result.get('ServiceResult')
    json_msgheader = json_serviceresult.get('msgHeader')
    result_message = json_msgheader.get('headerMsg')

    if '정상적으로 처리되었습니다.' != result_message:
        print('%s: Error[%s] for Request(%s)' % (datetime.now(), result_message, url), file=sys.stderr)
        return None

    json_msgbody = json_serviceresult.get('msgBody')
    json_itemlist = json_msgbody.get('itemList')

    return json_itemlist if isinstance(json_itemlist, dict) else None