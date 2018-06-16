import analysis_bus.collect.api as busapi

# test for pd_gen_url
# url = busapi.pd_gen_url('http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo', busRouteId=100100112, _type='json')
# print(url)

# test for pd_fetch_info
item = busapi.pd_fetch_info(100100112)
print(item)