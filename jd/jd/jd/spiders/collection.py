import scrapy
from scrapy.http import Request, Response
from typing import TYPE_CHECKING, Any, Iterable, List, Optional, Union, cast
import re
import requests
import time
from jd.items import JdItem

class CollectionSpider(scrapy.Spider):
    name = "collection"
    # allowed_domains = ["list.jd.com"]
    start_urls = ["https://list.jd.com/list.html"]

    def start_requests(self) -> Iterable[Request]:
        for i in range(1, 1000):

            yield scrapy.Request(
                url=f"https://list.jd.com/list.html?cat=1318%2C12099%2C9759&isList=1&page={i}&s={(i - 1) * 30}&click=0&log_id=1699091123273.3569")

    def parse(self, response):
        # print(response)
        for i in re.search(r"wids:'(.*?)'", response.text).group(1).split(","):
            yield scrapy.Request(url=f"https://item.jd.com/{i}.html", callback=self.parse_detail, meta={'i': i})

    def parse_detail(self, response: Response):
        # print(response.text)
        # print()
        images = re.search(r"imageList: \[(.*?)\]",response.text,re.DOTALL).group(1)
        title = response.xpath("//div[@class='sku-name']//text()").extract()[0]
        # print(response.xpath("//div[@id='choose-attrs']//@data-sku").extract())
        color = response.xpath("//div[@id='choose-attr-1']//@data-value").extract()
        size = response.xpath("//div[@id='choose-attr-2']//@data-value").extract()
        detail = response.xpath("//div[@class='p-parameter']//text()").extract()
        dict_t = {
            "i": response.meta['i'],
            'title': title,
            'color': color,
            'size': size,
            'detail': detail,
            "images":images
        }
        url = "https://api.m.jd.com/?appid=item-v3&functionId=checkChat&client=pc&clientVersion=1.0.0&loginType=3&body={\"source\":\"jd_pc_item\",\"key\":\"JDPC_baf0bd4ca77d4e09847b97504b8763cf\",\"pid\":" + \
              response.meta['i'] + ",\"returnCharset\":\"utf-8\"}"
        yield scrapy.Request(url=url, callback=self.shopId_venderId_parse, meta=dict_t)

    def shopId_venderId_parse(self, response: Response):
        # print(response.json())
        shopId = response.json()["shopId"]
        venderId = response.json()["venderId"]
        value = '{"skuId":' + response.meta[
            'i'] + ',"cat":"1318,12099,9759","area":"13_1042_1051_46514","shopId":"' + str(
            shopId) + '","venderId":' + str(
            venderId) + r',"paramJson":"{\"platform2\":\"1\",\"specialAttrStr\":\"p0ppppppppp2ppppppppppppppp\",\"skuMarkStr\":\"00\"}","num":1,"bbTraffic":""}'
        tt = int(time.time() * 1000)
        res = requests.get(
            "http://localhost:3000/calculateH5st?body=" + value + "&appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&tt=" + str(tt))
        payload = {
            'appid': 'pc-item-soa',
            'functionId': 'pc_detailpage_wareBusiness',
            'client': 'pc',
            'clientVersion': '1.0.0',
            't': tt,
            'body': value,
            'h5st': res.json()['h5st'],
            'x-api-eid-token': 'jdd033UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKEAAAAMLT5FGN3QAAAAADF2XCDO5VEO3TIX',
            'loginType': '3',
            'uuid': '122270672.16989083476991332344107.1698908348.1699156909.1699180619.13',
        }
        result = '&'.join([f'{key}={value}' for key, value in payload.items()])
        yield scrapy.Request("https://api.m.jd.com/?" + result, callback=self.result_parse,meta=response.meta)

    def result_parse(self, response: Response):
        print("-------------------------------------------------------------------------------------------------------------")
        print(response.status)
        # print(response.text)
        try:
            response.meta['price'] = response.json()['price']['p']
        except KeyError as e:
            print(e)
            exit()
        print(response.meta)
        jditem = JdItem()
        jditem['title'] = response.meta['title']
        jditem['price'] = response.meta['price']
        jditem['color'] = response.meta['color']
        jditem['size'] = response.meta['size']
        jditem['sku'] = response.meta['i']
        jditem['img_urls'] = response.meta['images']
        jditem['details'] = response.meta['detail']
        yield jditem

