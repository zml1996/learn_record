import requests
api='https://www.douyin.com/aweme/v1/web/channel/feed/?device_platform=webapp&aid=6383&channel=channel_pc_web&tag_id=&count=10&version_code=160100&version_name=16.1.0&_signature=_02B4Z6wo00101b7CeVAAAIDDjpROx2Hpd0m-wn3AAA9m86'
api2='https://www.douyin.com'
headers={
"sec-ch-ua":'" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
"accept":'application/json, text/plain, */*',
"withcredentials":'true',
"sec-ch-ua-mobile":'?0',
"user-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
"sec-fetch-site":'same-origin',
"sec-fetch-mode":'cors',
"sec-fetch-dest":'empty',
"referer":'https://www.douyin.com/',
"accept-encoding":'gzip, deflate, br',
"accept-language":'zh-CN,zh;q=0.9',
"cookie": 'ttwid=1%7CcuMAOlFaUgBbQjhaIdVfUHFRzQGrE5wMcO1-E9CKOVc%7C1624253313%7Cdeb468e10cbd2a39ea2917a3fdfdc54c21d17de1240754580c65a8d1139c39bd; MONITOR_WEB_ID=8bd26614-c683-4a3b-936b-54ee8d90dc89; odin_tt=98fb7e71a0d35411f61d366ceda4543e90397a229c4821f07a3abd329f34b9a3a57fb36daef5a1f0341dac5132702b72bbe8dd59ca2f2be7bb92247c22811cfd; passport_csrf_token_default=1944884c6b6d3b272aa1c9fbda07bf78; passport_csrf_token=1944884c6b6d3b272aa1c9fbda07bf78; douyin.com; s_v_web_id=verify_kqbygz3a_RqZcyT22_ONAC_4wUa_BEpm_F4rUQPpaKdPl',
}
resp=requests.get(api,headers=headers,verify=False)
print(resp.text)
