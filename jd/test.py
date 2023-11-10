# import requests
#
# url = "https://api.m.jd.com/?functionId=pc_detailpage_wareBusiness&client=pc&clientVersion=1.0.0&t=1699241512084&body=%7B%22skuId%22%3A10070549742146%2C%22cat%22%3A%221318%2C12099%2C9759%22%2C%22area%22%3A%2213_1042_1051_46514%22%2C%22shopId%22%3A%2212581701%22%2C%22venderId%22%3A13249360%2C%22paramJson%22%3A%22%7B%5C%22platform2%5C%22%3A%5C%221%5C%22%2C%5C%22colType%5C%22%3A0%2C%5C%22specialAttrStr%5C%22%3A%5C%22p0pppppppppppppppppppppppp%5C%22%2C%5C%22skuMarkStr%5C%22%3A%5C%2200%5C%22%7D%22%2C%22num%22%3A1%2C%22bbTraffic%22%3A%22%22%7D&h5st=20231106113152148%3B3imn56zzt9t99gj8%3Bfb5df%3Btk03wb6ae1c7018n3ciYd6HaMruDXkLA_i-a9ODeyR09__oqzDU_YRUXfZ_rmlt3gm_L_DMZ8mctFsK95b_7q4n8MFMn%3Bbcd9ed62f9c9c755e4f6a00cec924a74%3B4.1%3B1699241512148%3Bee3cf7f6b94dc20e9265d83066bb9ceece4bb89e2b7e8bf5afb1bfd928788174bfa06c210ddd4437d8a2e234330c3a3980b96c3953b1ab788029ae792b39e11358116f6c49a24cd7f34d0699b0fd2712b875cf21995ed4ee51e920acfbc11c5b0f3e58c3767d519a15e8c7cc60ab888b48771701912899fb95cea19d20c204ba16f89725b67ebbb6301a7ad0aa032b4d4ca62813e2f7a8086a9c16c519b359ff16415e130479aec20666817d7d8d3a52691a405ff352afe48e610d492308298a55b324f9c01d74520c81b86de2e621b5ddc95cc889ec7e3faef61401235e564e9663a28436b570cb177bbf76175c1b3e18a2bdf025ebcc2cb865036f7766c78c1524f0fa5dcdb26d375921ac970330904dd511e1509699d710f345e0e0c529e834fdcdb4ba6118a41b39ca73d595c8f0&x-api-eid-token=jdd033UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKEAAAAMLUKTNFEIAAAAADK5FBV2C3IBKQQX&loginType=3&uuid=122270672.16989083476991332344107.1698908348.1699236904.1699240924.18"
#
# payload = {
# "appid":"pc-item-soa"
# }
# headers = {
#   'authority': 'api.m.jd.com',
#   'accept': 'application/json, text/javascript, */*; q=0.01',
#   'accept-language': 'zh,zh-CN;q=0.9',
#   'cache-control': 'no-cache',
#   'cookie': '__jdv=122270672|direct|-|none|-|1698908347700; shshshfpa=2f231df7-ba4c-b951-d2ee-1ca2c79c5963-1698908350; shshshfpx=2f231df7-ba4c-b951-d2ee-1ca2c79c5963-1698908350; areaId=13; __jdu=16989083476991332344107; pinId=ryEHD9SUKe4hNqcyUKFnNrV9-x-f3wj7; pin=jd_76a3102d80b22; unick=1_%E7%8E%9B%E5%8D%A1%E5%B7%B4%E5%8D%A1--; _tp=%2BTwEK1XPS5%2BAE%2FhDaiEuUWqs0VyliUkuFlGRpf%2B%2Fphw%3D; _pst=jd_76a3102d80b22; ipLoc-djd=13-1042-1051-46514; user-key=063066cd-7dfd-4ce5-b332-94ffef35b670; cn=4; TrackID=1akqzy2QKRQECMekeQpj9xiR0Is6F_FriG-Uh0CBn78YZ62aVfK9HvlQ13JhYMqyJMwI2Kt3XXginOv8zcbgmEt2A8W8vVKoWoszByfjhS4A; thor=9A8EC803B91A5FB9B3FBFFD1D5BC5DF4AE8631EEE8E1EC23C1BDA72BB42B477BDD8F988E6AFC19249621091C5F15072F965DB1903CB2CE1F6DCC183A5668A66C386BDE6B633ACFA943E96B169E7D33D69F9D1862B5218ECA2A54F0F65EF0A65EA1F21249DD3D7CABE4FC05FCADE87E637DDD7A30F02240296715A771BB5AD8415A9AF7ABF697D968F7D33CA8B34B4AEBACFFC8EBC8C1E3F41394E9E814244129; flash=2_Iv4onq81bFbOoh80pNChq9vefiSVx91xvcdYmjARZTMwlZCTpE4wSR6DPXB-0JWskL7p8xChxcLzm-UTiPOyr1UJpgJLH2Uy_fPZQyMyNhD*; ceshi3.com=201; jsavif=1; __jdc=122270672; 3AB9D23F7A4B3C9B=3UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKE; __jda=122270672.16989083476991332344107.1698908348.1699236904.1699240924.18; shshshfpb=AAqTUpqKLEiMd97pMuVHS7hyix5xZYxaYkINQfwAAAAA; token=467cfdce684ea4c6ff1a0d5d313ca30a,3,944023; __tk=rUaDqua5rUVF1AqB1YSFqAsArANXrzTsKcrYrUsA2wSFrwSDqcxnrV,3,944023; __jdb=122270672.2.16989083476991332344107|18.1699240924; 3AB9D23F7A4B3CSS=jdd033UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKEAAAAMLUKX5BRAAAAAADORKA5O7G5MOE4X; _gia_d=1; shshshsID=ce41a9c886c1ab10b99ebf8381b3f548_2_1699241515853; ipLoc-djd=13-1042-0-0',
#   'origin': 'https://item.jd.com',
#   'pragma': 'no-cache',
#   'referer': 'https://item.jd.com/',
#   'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
#   'sec-ch-ua-mobile': '?0',
#   'sec-ch-ua-platform': '"Windows"',
#   'sec-fetch-dest': 'empty',
#   'sec-fetch-mode': 'cors',
#   'sec-fetch-site': 'same-site',
#   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
#   'x-referer-page': 'https://item.jd.com/10070549742146.html',
#   'x-rp-client': 'h5_1.0.0'
# }
#
# response = requests.request("GET", url, headers=headers, params=payload)
#
# print(response.text)
query_params = {
            'param1': 'value1',
            'param2': 'value2',
        }
query_string = '&'.join([f'{key}={value}' for key, value in query_params.items()])
print(query_string)