import requests

url = "https://api.m.jd.com/?appid=search-pc-java&functionId=pc_search_s_new&client=pc&clientVersion=1.0.0&t=1698974464277aaa&body=%7B%22cat%22%3A%221318%2C12099%2C9756%22%2C%22isList%22%3A1%2C%22page%22%3A%2213%22%2C%22s%22%3A%22357%22%2C%22click%22%3A%220%22%2C%22log_id%22%3A%221698974395629.8238%22%2C%22show_items%22%3A%22%22%7D&loginType=3&uuid=122270672.16989083476991332344107.1698908348.1698922277.1698973302.3&area=13_1042_1051_46514&h5st=20231103092109567%3B6g5tzimn933g63w5%3Bf06cc%3Btk03w7a2b1b8818nIGDhapO7D82bz9PuUT6zA0f-RZV5w77DswPTBfIfRYFx5T4YYHd5LeOCqBdtybgmDuKNJxwbQC7L%3B3040d0ad1225d9ce78e011c29894abf8%3B4.1%3B1698974469567%3Bee3cf7f6b94dc20e9265d83066bb9ceece4bb89e2b7e8bf5afb1bfd928788174bfa06c210ddd4437d8a2e234330c3a3980b96c3953b1ab788029ae792b39e11358116f6c49a24cd7f34d0699b0fd2712b875cf21995ed4ee51e920acfbc11c5b0f3e58c3767d519a15e8c7cc60ab888b48771701912899fb95cea19d20c204ba16f89725b67ebbb6301a7ad0aa032b4d4ca62813e2f7a8086a9c16c519b359ff16415e130479aec20666817d7d8d3a52574ea926313450aee8d706b72dae910fa5eb2a359b9e1a974be815f14bb69a173f1f0b4da9fba4ec5df0a2c9e2d1e571f0eb8c436ea7d5b1dbf3904367b26814469ae7993ae52ee16e27b0dab17ea9d661264027b7b044c432f85165be2931f3f653796f018c7f6716523e81e86e1e32&x-api-eid-token=jdd033UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKEAAAAMLSKZUTLQAAAAADRD2D2HJYLM5UUX"

def onebyoneTest(cookie: str):
    cookies = cookie.split(";")
    for i in cookies:
        value = cookie.replace(i + ";", "")
        print(i)
        yield value[1:] if value[0] == ' ' else value

payload = {}
for i in onebyoneTest("__jdv=122270672|direct|-|none|-|1698908347700; shshshfpa=2f231df7-ba4c-b951-d2ee-1ca2c79c5963-1698908350; shshshfpx=2f231df7-ba4c-b951-d2ee-1ca2c79c5963-1698908350; areaId=13; __jdu=16989083476991332344107; mba_muid=16989083476991332344107; wlfstk_smdl=p00broycwi2scx9jh5nbv0a78f992hks; TrackID=1lO8tF44iz5mVb7JTeGvpt6HJqxLqNyZfqU6bohzGTsee5ixpCS5szyK1BvCEqS0cjB2i-AUl03IgryxCNjuVxYDybb2xGOLxgSzNt2gVCXo; thor=9A8EC803B91A5FB9B3FBFFD1D5BC5DF4AE8631EEE8E1EC23C1BDA72BB42B477B540FB52C166C37840C15F2D1D5396DB4552A9BE9A89942C12BBE116622ED2E6FAED63EAF027A9FBDC44ED0685614F60C8E73A58CCEB944871EE80AC175CA91CD30A2B57A849D3D2134E5583210E2A9BFDFD747BDF6E513A01AE3FA4F81B771DDC0907E3EFD36A0CAFC85220F190B1132C26F6F9A093CFA8C373D1F8B26A5BD0D; flash=2_b9vUuNI2UFHomrp_nylE6zA92VV3cMaGG_mhXg7rYp7dpHFtDyDIA8eC3_uV8w4R9jL3hRClqbmP522o0kgEDkfdlmXJM8riu10DJBw0zek*; pinId=ryEHD9SUKe4hNqcyUKFnNrV9-x-f3wj7; pin=jd_76a3102d80b22; unick=1_%E7%8E%9B%E5%8D%A1%E5%B7%B4%E5%8D%A1--; ceshi3.com=201; _tp=%2BTwEK1XPS5%2BAE%2FhDaiEuUWqs0VyliUkuFlGRpf%2B%2Fphw%3D; _pst=jd_76a3102d80b22; ipLoc-djd=13-1042-1051-46514; __jda=122270672.16989083476991332344107.1698908348.1698922277.1698973302.3; __jdc=122270672; jsavif=1; 3AB9D23F7A4B3CSS=jdd033UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKEAAAAMLSKZUTLQAAAAADRD2D2HJYLM5UUX; __jdb=122270672.2.16989083476991332344107|3.1698973302; shshshsID=294b31aa667f50829e414813338c26e8_1_1698973338579; shshshfpb=AAkPbs5KLEiMd97pMuVHS7hyix5xZYxaYkINQSAAAAAA; 3AB9D23F7A4B3C9B=3UIDT7MJQD3Y4QTT6G6SFLABTL5UTF6FGOMGTLL6LJVB6HMBO73OOSRXDCMVRQCD3TEH56IAFRGLV3F6ILFAD54NKE"):
    headers = {
      'authority': 'api.m.jd.com',
      'accept': '*/*',
      'accept-language': 'zh,zh-CN;q=0.9',
      'cache-control': 'no-cache',
      'cookie': i,
      'origin': 'https://list.jd.com',
      'pragma': 'no-cache',
      'referer': 'https://list.jd.com/',
      'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-site',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
      'x-referer-page': 'https://list.jd.com/list.html',
      'x-rp-client': 'h5_1.0.0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.find("27113301494"))
