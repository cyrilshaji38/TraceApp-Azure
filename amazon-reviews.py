import requests
from bs4 import BeautifulSoup

def get_review(pages):

    headers = {
        'authority': 'www.amazon.com',
        'cache-control': 'max-age=0',
        'rtt': '100',
        'downlink': '9.2',
        'ect': '4g',
        'sec-ch-ua': '^\\^',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': 'session-id=140-4142375-4005405; i18n-prefs=USD; sp-cdn=^\\^L5Z9:IN^\\^; ubid-main=133-1703036-0414721; s_fid=15ACC4BA280D4F14-038C9A8E5E877985; regStatus=pre-register; aws-target-data=^%^7B^%^22support^%^22^%^3A^%^221^%^22^%^7D; aws-target-visitor-id=1623992980699-29478.31_0; lc-main=en_US; session-id-time=2082787201l; session-token=3C7FE5erzwisM4Q9VFUHzXSA/eMeK109XvSk3qGH0QACt4108/s0lKTOpDVQTEBs90M2tWq4niv7M6Qb/uP3k9iBEKg1xKTsaibq9ACUJiyvDiduYSi6Lo1A5rR3BFtb0hKq5YaiuVdgb0SctM4i6hzPr5w4P3scMT7tePHGZFUKSnw7eYAlsAD5i14Zhu7U; csm-hit=adb:adblk_no&t:1624715411612&tb:3Z2570B9GG7KJPY3JW0K+s-3Z2570B9GG7KJPY3JW0K^|1624715411612',
    }

    resp = requests.get(pages[0], headers=headers)

    soup = BeautifulSoup(resp.text, "html.parser") # html.parser, lxml

    # 10 divs
    reviews = soup.find_all("div", {"class": "a-section review aok-relative"})

    def get_review_body(soup_obj: BeautifulSoup) -> str:
        try:
            review_body = soup_obj.find('span', 
                {"class": "a-size-base review-text review-text-content"}
            ).get_text().strip()
            return review_body
        except Exception as e:
            return 'no_body'
            print(e)

    records = [get_review_body(rev) for rev in reviews]
    return records[1:]


pages = [
        "https://www.amazon.com/Heat-Storm-HS-1500-PHX-WIFI-Infrared-Heater/product-reviews/B07JXRWJ8D/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews",
    ]

print(get_review(pages))