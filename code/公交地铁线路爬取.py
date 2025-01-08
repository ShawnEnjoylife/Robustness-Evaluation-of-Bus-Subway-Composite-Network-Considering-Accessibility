from BusNetPy import *

key_fwd='b81d6d7b78d1a0e2b7ccdb7a21b2355f'
key='cade00206d675a7f0747ae4115ad191b'
jscode='836bd65c6772dc5c9d4809eb16aed3e8'

keyword='公交'

#按照多边形范围爬取

polygon='121.525819,38.976797|121.623401,38.865065'
province='辽宁'
city='大连'

#按行政边界爬取
# region=['大连市','沙河口区']
# province='辽宁'
# city='大连'


save_path='/Users/buxiangzun/Desktop/BusNetPy/'

bustop_mul,busline_mul=buspider.businfo(province,city,keyword,key,key_fwd,jscode,save_path,polygon_mult=polygon)
# bustop_region,busline_region=buspider.businfo(province,city,keyword,key,key_fwd,jscode,save_path,region_xzq=region)

