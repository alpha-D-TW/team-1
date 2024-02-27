curl 'https://link.cmbchina.com/CmbFinProd/SevAjax/ProdHandler.ashx' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: zh,en;q=0.9,zh-CN;q=0.8' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
  -H 'DNT: 1' \
  -H 'Origin: https://link.cmbchina.com' \
  -H 'Pragma: no-cache' \
  -H 'Referer: https://link.cmbchina.com/CmbFinProd/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  --data-raw 'queryParam=%7B%22type%22%3A%22PD%22%2C%22isOwn%22%3A%22A%22%2C%22isPublic%22%3A%22A%22%2C%22status%22%3A%220%22%2C%22keywords%22%3A%22%E5%B9%BF%E5%8F%91%22%2C%22pageNo%22%3A1%2C%22pageSize%22%3A500%2C%22crossFinance%22%3A%22Z%22%2C%22riskLevel%22%3A%22%22%7D' \
  >data.json
