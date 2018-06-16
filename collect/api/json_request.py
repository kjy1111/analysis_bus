from urllib.request import Request, urlopen
from datetime import *
import json
import xmltodict

def json_request(url='', encoding='utf-8', error=lambda e: print('%s %s' % (e, datetime.now()))):
    try:
        request = Request(url)
        resp = urlopen(request)

        resp_body = resp.read().decode(encoding)

        xml_dict = xmltodict.parse(resp_body)

        xml_string = json.dumps(xml_dict)

        json_result = json.loads(xml_string)

        print('%s: success for request[%s]' % (datetime.now(), url))

        return json_result

    except Exception as e:
                error(e)