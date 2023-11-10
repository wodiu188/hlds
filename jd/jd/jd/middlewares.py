# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class JdSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class JdDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        request.cookies = {
            '__jdv': '122270672|direct|-|none|-|1698908347700',
            ' shshshfpa': '2f231df7-ba4c-b951-d2ee-1ca2c79c5963-1698908350',
            ' shshshfpx': '2f231df7-ba4c-b951-d2ee-1ca2c79c5963-1698908350', ' areaId': '13',
            ' __jdu': '16989083476991332344107', ' pinId': 'ryEHD9SUKe4hNqcyUKFnNrV9-x-f3wj7',
            ' pin': 'jd_76a3102d80b22', ' unick': '1_%E7%8E%9B%E5%8D%A1%E5%B7%B4%E5%8D%A1--',
            ' _tp': '%2BTwEK1XPS5%2BAE%2FhDaiEuUWqs0VyliUkuFlGRpf%2B%2Fphw%3D',
            ' _pst': 'jd_76a3102d80b22', ' ipLoc-djd': '13-1042-1051-46514',
            ' user-key': '063066cd-7dfd-4ce5-b332-94ffef35b670', ' cn': '4',
            ' TrackID': '1akqzy2QKRQECMekeQpj9xiR0Is6F_FriG-Uh0CBn78YZ62aVfK9HvlQ13JhYMqyJMwI2Kt3XXginOv8zcbgmEt2A8W8vVKoWoszByfjhS4A',
            ' thor': '9A8EC803B91A5FB9B3FBFFD1D5BC5DF4AE8631EEE8E1EC23C1BDA72BB42B477BDD8F988E6AFC19249621091C5F15072F965DB1903CB2CE1F6DCC183A5668A66C386BDE6B633ACFA943E96B169E7D33D69F9D1862B5218ECA2A54F0F65EF0A65EA1F21249DD3D7CABE4FC05FCADE87E637DDD7A30F02240296715A771BB5AD8415A9AF7ABF697D968F7D33CA8B34B4AEBACFFC8EBC8C1E3F41394E9E814244129',
            ' flash': '2_Iv4onq81bFbOoh80pNChq9vefiSVx91xvcdYmjARZTMwlZCTpE4wSR6DPXB-0JWskL7p8xChxcLzm-UTiPOyr1UJpgJLH2Uy_fPZQyMyNhD*',
            ' ceshi3.com': '201', ' __jdc': '122270672', ' jsavif': '1',
            ' __jda': '122270672.16989083476991332344107.1698908348.1699320405.1699323360.23',
            ' mba_muid': '16989083476991332344107',
            ' 3AB9D23F7A4B3C9B': '3UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKE',
            ' token': '94ff832804bdab36b5952a69b58d8dc8,3,944070',
            ' __tk': 'lDzKYmZfTlTlSD3amCmlrKVxlBVlpLKconVkVmZflaOnmn3UmKmdZbZflAZRmnfgmD5TVcJ4,3,944070',
            ' 3AB9D23F7A4B3CSS': 'jdd033UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKEAAAAMLU7BD72IAAAAACCRG4ILNT7AEXQX',
            ' _gia_d': '1', ' mba_sid': '16993255075969387509759902150.4',
            ' __jd_ref_cls': 'LoginDisposition_Go',
            ' x-rp-evtoken': 'N-nAb5Oj6OS1u8hkvixIgPgdaU_Wr92mVMWBBjHaF89E_8YxSwfoTTjEAhhhKNQRVzQugitw5bKzc7hx4GZus8wvtH2N88_z8rpzy-pE9aC5RGwMXBnjSDBkPuBSVITEAfWWj4MZ_e6hFJw7T6hk0g6TCD_3wGzCup0HMoY1VDtYUhsL33dmiLq8dbi9i8VP42XbmZUlUqObpy7deR0qH0CKQVIMQVA-bJpURNP0gH4%3D',
            ' shshshsID': '46c84fcd8d94ab80262aee20d93a1db2_8_1699326620142',
            ' __jdb': '122270672.18.16989083476991332344107|23.1699323360',
            ' shshshfpb': 'AArZ0wqeLEiMd97pMuVHS7hyix5xZYxaYkINQfwAAAAA'
        }

        request.headers['authority'] = ['list.jd.com']
        request.headers['accept'] = [
            'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7']
        request.headers['accept-language'] = ['zh']
        request.headers['cache-control'] = ['no-cache']
        request.headers['pragma'] = ['no-cache']
        request.headers['sec-ch-ua'] = ['"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"']
        request.headers['sec-ch-ua-mobile'] = ['?0']
        request.headers['sec-ch-ua-platform'] = ['"Windows"']
        request.headers['sec-fetch-dest'] = ['document']
        request.headers['sec-fetch-mode'] = ['navigate']
        request.headers['sec-fetch-site'] = ['same-site']
        request.headers['sec-fetch-user'] = ['?1']
        request.headers['upgrade-insecure-requests'] = ['1']
        request.headers['user-agent'] = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36']

        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
