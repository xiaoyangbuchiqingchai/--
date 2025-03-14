import requests
import json

url = "https://api.bilibili.com/x/web-interface/popular"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Referer": "https://www.bilibili.com/",
    "Cookie": "buvid3=4BDB35ED-B6B1-6D92-466A-F472CE026D6763704infoc; b_nut=1714732263; _uuid=F3A6ABE3-2F107-C8109-9553-FC8C7A513C7364404infoc; enable_web_push=DISABLE; buvid4=4F4A339A-D849-7326-F074-1A8AABC684EE64871-024050310-AW8C6k5SsrBEtBoASFLtjQ%3D%3D; rpdid=|(J|~|)JmuYY0J'u~uR~J~YYu; buvid_fp_plain=undefined; PVID=5; header_theme_version=CLOSE; DedeUserID=271286917; DedeUserID__ckMd5=40d2d563a3da4810; fingerprint=d5697d4c8147d4fe7598394b234ac41d; match_float_version=ENABLE; hit-dyn-v2=1; LIVE_BUVID=AUTO9717331492496713; buvid_fp=d5697d4c8147d4fe7598394b234ac41d; SESSDATA=9c782e53%2C1751299028%2Cf4277%2A11CjALtuh5JCqQnOsFaGITku51ZyiWT3IDA21FXuyR8HMbWeRTFyS7_XLZTN0kCgXulogSVnlCbVpfeW1FR1NxLTlfREYzamduemp0Q0ZNU19LSG5HbTJDRVhmUktLdHZTcU1CRDhOZFpBZXlYRWRLM21CT2pQS0ZCWmJjX0RjZ0QtWTZsSkRSLVBRIIEC; bili_jct=e8d5815ef4680eb26ec93c7f0a84f955; sid=8nbythj9; share_source_origin=copy_web; bsource=search_bing; CURRENT_QUALITY=80; enable_feed_channel=ENABLE; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NDIwNDYzMTQsImlhdCI6MTc0MTc4NzA1NCwicGx0IjotMX0.p2Q1cVXzm2cCwcTH4pppBytouU8nKO_ML5Hmz1FheMo; bili_ticket_expires=1742046254; home_feed_column=5; b_lsid=86C5429F_19593EBAD59; CURRENT_FNVAL=4048; browser_resolution=1912-926; bp_t_offset_271286917=1044132972296404992",  # 从浏览器复制
    "Accept-Language": "zh-CN,zh;q=0.9"
}

try:
    response = requests.get(url, headers=headers, timeout=5)
    response.raise_for_status()  # 检查HTTP状态码
    
    data = response.json()
    if data['code'] == 0:  # 接口返回成功标识
        videos = data['data']['list']
        for idx, video in enumerate(videos, 1):
            print(f"{idx}. {video['title']} (BV:{video['bvid']})")
    else:
        print(f"API错误：{data['message']}")
        
except Exception as e:
    print(f"请求失败：{str(e)}")