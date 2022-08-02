import requests

url = "https://www.indeed.com/jobs?q=Software Developer &l=Charlotte"

payload={}
headers = {
  'Cookie': 'CTK=1g9g0hnooi7mi801; __cf_bm=4GlpGFa_XdN6Xkrw64NSochXPblK5s1f73ApiyGA850-1659468570-0-AYj7OUuhnQTCl0MWmt8CAg2YMhy3aVHFVXXAGjWhjUuKdSU+HZ7NeIpAM++aZLJQKBMM0lndMY2kwQR+mnIQq18=; _cfuvid=ZwlkiIOW_BGo_j9MIt1pxeDDcbnDLxbOqq7rXTro60w-1659468570568-0-604800000; INDEED_CSRF_TOKEN=vXylKnJ6IDJocrdUgDnzcfMNHn69Pjsi; JSESSIONID=97FCE1FD670D1B931CD9D238DC5F9F50; PREF="TM=1659468570400:L=Charlotte"; RQ="q=Software+Developer+&l=Charlotte&ts=1659468570424"; UD="LA=1659468570:CV=1659468570:TS=1659468570:SG=255c593d82599602073119c7e36f276b"; ctkgen=1; indeed_rcc=""; jaSerpCount=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
