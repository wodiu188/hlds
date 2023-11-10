import requests
import re
import time
import json

response = requests.get("http://localhost:3000/ot").json()
ot = response['ot']
tt = response['tt']

url = "https://cactus.jd.com/request_algo?g_ty=ajax"

payload = json.dumps({
  "version": "4.1",
  "fp": tt,
  "appId": "fb5df",
  "timestamp": int(time.time()*1000),
  "platform": "web",
  "expandParams": ot,
  "fv": "v1.6.1"
})
print(ot)
print(tt)
headers = {
  'Accept-Language': 'zh,zh-CN;q=0.9',
  'Cache-Control': 'no-cache',
  'Connection': 'keep-alive',
  'Origin': 'https://item.jd.com',
  'Pragma': 'no-cache',
  'Referer': 'https://item.jd.com/',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
  'accept': 'application/json',
  'content-type': 'application/json',
  'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.json())
tk = response.json()['data']['result']['tk']
fp = response.json()['data']['result']['fp']


url = "https://list.jd.com/list.html?cat=1318%2C12099%2C9759&isList=1&page=4&s=87&click=0&log_id=1699091123273.3569"

payload = {}
headers = {
  'authority': 'list.jd.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'zh,zh-CN;q=0.9',
  'cache-control': 'no-cache',
  'pragma': 'no-cache',
  'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'same-origin',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
  'Cookie': 'ipLoc-djd=13-1042-0-0; avif=1'
}

response = requests.request("GET", url, headers=headers, data=payload)
for i in re.search(r"wids:'(.*?)'", response.text).group(1).split(","):
    print(i)
    url = "https://api.m.jd.com/?appid=item-v3&functionId=checkChat&client=pc&clientVersion=1.0.0&loginType=3&body={\"source\":\"jd_pc_item\",\"key\":\"JDPC_baf0bd4ca77d4e09847b97504b8763cf\",\"pid\":"+i+",\"returnCharset\":\"utf-8\"}"

    payload = {}
    headers = {
      'authority': 'api.m.jd.com',
      'accept': 'application/json, text/javascript, */*; q=0.01',
      'accept-language': 'zh,zh-CN;q=0.9',
      'cache-control': 'no-cache',
      'cookie': '__jdv=122270672|direct|-|none|-|1698908347700; shshshfpa=2f231df7-ba4c-b951-d2ee-1ca2c79c5963-1698908350; shshshfpx=2f231df7-ba4c-b951-d2ee-1ca2c79c5963-1698908350; areaId=13; __jdu=16989083476991332344107; pinId=ryEHD9SUKe4hNqcyUKFnNrV9-x-f3wj7; pin=jd_76a3102d80b22; unick=1_%E7%8E%9B%E5%8D%A1%E5%B7%B4%E5%8D%A1--; _tp=%2BTwEK1XPS5%2BAE%2FhDaiEuUWqs0VyliUkuFlGRpf%2B%2Fphw%3D; _pst=jd_76a3102d80b22; ipLoc-djd=13-1042-1051-46514; user-key=063066cd-7dfd-4ce5-b332-94ffef35b670; cn=4; TrackID=1akqzy2QKRQECMekeQpj9xiR0Is6F_FriG-Uh0CBn78YZ62aVfK9HvlQ13JhYMqyJMwI2Kt3XXginOv8zcbgmEt2A8W8vVKoWoszByfjhS4A; thor=9A8EC803B91A5FB9B3FBFFD1D5BC5DF4AE8631EEE8E1EC23C1BDA72BB42B477BDD8F988E6AFC19249621091C5F15072F965DB1903CB2CE1F6DCC183A5668A66C386BDE6B633ACFA943E96B169E7D33D69F9D1862B5218ECA2A54F0F65EF0A65EA1F21249DD3D7CABE4FC05FCADE87E637DDD7A30F02240296715A771BB5AD8415A9AF7ABF697D968F7D33CA8B34B4AEBACFFC8EBC8C1E3F41394E9E814244129; flash=2_Iv4onq81bFbOoh80pNChq9vefiSVx91xvcdYmjARZTMwlZCTpE4wSR6DPXB-0JWskL7p8xChxcLzm-UTiPOyr1UJpgJLH2Uy_fPZQyMyNhD*; ceshi3.com=201; __jdc=122270672; jsavif=1; shshshsID=220a6e93a05dfa71ed3117a6a3d749c1_1_1699150169363; token=4cf27f3e05ac188b5701ba1fb8224d10,3,943972; __tk=VkSEiAeETkYDVnfJVclCTUSBTka2TIKKTke4TkTLiAS,3,943972; __jda=122270672.16989083476991332344107.1698908348.1699147984.1699150178.11; 3AB9D23F7A4B3CSS=jdd033UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKEAAAAMLTU7CKZIAAAAACCGQKZT34TJIAIX; _gia_d=1; 3AB9D23F7A4B3C9B=3UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKE; __jdb=122270672.2.16989083476991332344107|11.1699150178; shshshfpb=AAtdCPp2LEiMd97pMuVHS7hyix5xZYxaYkINQZwAAAAA; ipLoc-djd=13-1042-0-0',
      'origin': 'https://item.jd.com',
      'pragma': 'no-cache',
      'referer': 'https://item.jd.com/',
      'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
      'x-referer-page': 'https://item.jd.com/100032606511.html',
      'x-rp-client': 'h5_1.0.0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.json())
    shopId = response.json()["shopId"]
    venderId = response.json()["venderId"]

    value = '{"skuId":100032606511,"cat":"1318,12099,9759","area":"13_1042_1051_46514","shopId":"'+shopId+'","venderId":'+venderId+',"paramJson":"{\"platform2\":\"1\",\"specialAttrStr\":\"p0ppppppppp2ppppppppppppppp\",\"skuMarkStr\":\"00\"}","num":1,"bbTraffic":""}'
    tt = int(time.time()*1000)
    response = requests.get("http://localhost:3000/calculateH5st?body="+value+"&appid=pc-item-soa&functionId=pc_detailpage_wareBusiness&tt="+str(tt))
    payload = {
      'appid': 'pc-item-soa',
      'functionId': 'pc_detailpage_wareBusiness',
      'client': 'pc',
      'clientVersion': '1.0.0',
      't': '1699186940877',
      'body': value,
      'h5st': response.text,
      'x-api-eid-token': 'jdd033UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKEAAAAMLT5FGN3QAAAAADF2XCDO5VEO3TIX',
      'loginType': '3',
      'uuid': '122270672.16989083476991332344107.1698908348.1699156909.1699180619.13',
    }
