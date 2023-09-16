import requests
import json


continuation_token = 'AQHR25K_GhGUScbiOmh7IRittu6NcfqXA_yX85vhiTVXN1MC9CiyM8PgwGw_yW_usvFBylzILJnt05wgS4M1WavZWQ'
while True:
    if not continuation_token:
        break

    url = "https://www.facebook.com/api/graphql"

    payload = f"av=61550964032031&__user=61550964032031&__a=1&__req=k&__hs=19616.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1008680585&__s=8vhme0%3Aykbpg3%3A6y90mr&__hsi=7279306350893877912&__dyn=7AzHxqUW13xt0mUyEqxenFwLBwopU98nwgUao4u5QdwSxucyUco5S3O2Saw8i2S1DwUx60DU1LVEtwMw65xO2OU7m2210wEwgolzUO0n24oaEd82lwv89kbxS2218wc61awkovwRwlE-U2exi4UaEW2au1jxS6FobrwKxm5oe8cEW4-5pUfEe872m7-8wywdG7FobpEbUGdG0HE88cA0z8c84q58jwTwNxe6Uak1xwJwxyo6J0qo4e16wWw&__csr=gL6OY5Ij7QBkZmDNad6tkAzbd9svmQyn9blPr-KIKGbSQDqHiLlltOIAyBBJeB8QiiXTHy7V9kAp9pSXy94HABt4LjgKu9yoC-nx2eQ-9XylGp6iK4oO8gyJBpGx2q_yF8xQlACHy8y4UOEhgkJ28KHByF9-8o8Ey4ooy7BAKdxyaCzogiUKV8sxe64FeAh2EaQ3m2u48sG489oW224bwFAgnx648O8wLoN1Sp1C4rKdGdzU8o8ocA1cgmx25FoW9K2O2yfggBwaa4u13wyyp8hg9o4vDxi2q6o9UG7po5idwjEK6k0zE2Myo0jAzE0cdE0d2Q01Tgw0V_AwtE0odw66we6li08C0s6exm0i10c28zo1kQ4E2Kw0zUwio0isg3qw12S8805fo0Lq1tuGJ2qa1nhA0alg0nJGbw3EE1OU1eE-0vG0nWmUy-0km0n21tg1xE72h02vE0H6&__comet_req=15&fb_dtsg=NAcMfRlFT30RjNolGKsPL08ZuUhwiTMFKyc-GF7tk165Lm0xUePm7aA%3A1%3A1694837991&jazoest=25283&lsd=o14SfsWwAFkZwkt2X2BmhU&__spin_r=1008680585&__spin_b=trunk&__spin_t=1694845583&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=ProfileCometAppCollectionListRendererPaginationQuery&variables=%7B%22count%22%3A8%2C%22cursor%22%3A%22{continuation_token}%22%2C%22scale%22%3A1%2C%22search%22%3Anull%2C%22id%22%3A%22YXBwX2NvbGxlY3Rpb246NjE1NTA5NjQwMzIwMzE6MjM1NjMxODM0OTozMg%3D%3D%22%7D&server_timestamps=true&doc_id=6515974468471236"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded",
        "X-FB-Friendly-Name": "ProfileCometAppCollectionListRendererPaginationQuery",
        "X-FB-LSD": "o14SfsWwAFkZwkt2X2BmhU",
        "X-ASBD-ID": "129477",
        "Origin": "https://www.facebook.com",
        "Alt-Used": "www.facebook.com",
        "Connection": "keep-alive",
        "Referer": "https://www.facebook.com/profile.php?id=61550964032031&sk=followers",
        "Cookie": "fr=0B2WXReqCDR6xBLnT.AWV1jNuGygttHqSdT2wg99emT7s.BlBUot.YI.AAA.0.0.BlBUot.AWWyamfk5zw; sb=o2kBZecPI7AgppvB2y-BFsQm; wd=854x672; c_user=100094654806004; xs=1%3A6-kmqmL0FZZyvQ%3A2%3A1694837991%3A-1%3A-1%3A%3AAcVECxhHvsfEqPBZhi_779put4UB_RKTB4KPs7VVVQ; datr=6ywFZdYmnpOpCywn7oqR5-ND; usida=eyJ2ZXIiOjEsImlkIjoiQXMxMmJkbTFqa2l3NjEiLCJ0aW1lIjoxNjk0ODQwOTExfQ%3D%3D; dpr=0.8955223880597015; i_user=61550964032031",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "TE": "trailers"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    response = response.json()
    if response['data']['node']['pageItems']['page_info']['has_next_page']:
        continuation_token = response['data']['node']['pageItems']['page_info']['end_cursor']
    else:
        continuation_token = None

    profiles = response['data']['node']['pageItems']['edges']

    existing_data = []
    try:
        with open('a.json', 'r', encoding='utf-8') as file:
            existing_data = json.load(file)
    except FileNotFoundError:
        existing_data = []

    # Process the new profiles and append them to the existing data
    new_data = []
    if 'data' in response and 'node' in response['data'] and 'pageItems' in response['data']['node']:
        profiles = response['data']['node']['pageItems']['edges']
        for profile in profiles:
            profile = profile['node']
            image = profile['image']['uri']
            title = profile['title']['text']
            subtitle_text = profile['subtitle_text'].get('text', 'n/a')
            url = profile['url']

            data = {'image': image, 'title': title, 'subtitle_text': subtitle_text, 'url': url}
            new_data.append(data)
        print(f"Added Profile {len(new_data)} - {title}")
    # Append the new data to the existing data
    existing_data.extend(new_data)

    # Write the updated data back to the JSON file
    with open('a.json', 'w', encoding='utf-8') as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

    print(continuation_token)