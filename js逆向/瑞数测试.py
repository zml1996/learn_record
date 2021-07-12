import requests

api='http://www.chinadrugtrials.org.cn/clinicaltrials.searchlist.dhtml'
headers={
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9",
"Cache-Control": "max-age=0",
"Connection": "keep-alive",
"Content-Length": "27",
"Content-Type": "application/x-www-form-urlencoded",
"Cookie": "FSSBBIl1UgzbN7N80S=MeftSL_rIljvvJa.1pcb2VdeOxV.qz5wbEeGFK9LCz3lBoTZjbJrovZhGYyv2QyB; token=An6rePB_hVmqIFBX51SBsfmBbfkySL0oPcS9qGQ5XeY1afPjCnGWNAnixTg; JSESSIONID=F5EAA4525C248267CF8A75F8A67DE777; FSSBBIl1UgzbN7N80T=3gu81KxjCk1CrF4Gb4OOJWBRf5qnpJ2FUCumzMNYnhjsWs4LelPSXnoD.ozUibDl_SNAWb5GxoraAFkf1WoSx0kJzopon9l8ov72hjNEP4xyYaclDiF2..2lBZkz3v3CDm2u6ptw88TcA1Z9ZiOfFHgd4BKmIeUH8cEOErIp9oZJVhyi4VW4sC1kdM2qbvR36YMKaTXzuWL1F0wFzOdUyIVfBznIxG5jZF7tq36ciOPhudx.dVYGTTQc1va.VxGcxo_8aRS.NvZLZS1uNvEyyBvKjh3gtcVfVYty4A.qeCKSzxNoQFGhc8.pMKXbkWj7ryvmLy9l82F7XW.Y321pb7SpGcEw2mjMGesGHfILQS7hdKq",
"Host": "www.chinadrugtrials.org.cn",
"Origin": "http://www.chinadrugtrials.org.cn",
"Referer": "http://www.chinadrugtrials.org.cn/index.html",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
}

data={
"keywords":"感冒",
}
resp=requests.post(api,headers=headers,data=data)
print(resp.text)
