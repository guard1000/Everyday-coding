import sys
import argparse
import requests

API_URL = 'https://kapi.kakao.com/v1/vision/adult/detect'
MYAPP_KEY = 'YOUR_APP_KEY'

def detect_adult(image_url):
    headers = {'Authorization': 'KakaoAK {}'.format(MYAPP_KEY)}

    try:
        data = { 'image_url' : image_url}
        resp = requests.post(API_URL, headers=headers, data=data)
        resp.raise_for_status()
        result = resp.json()['result']
        if result['adult'] > result['normal'] and result['adult'] > result['soft']:
            print("성인 이미지일 확률이 {}% 입니다.".format(result['adult']*100))
        elif result['soft'] > result['normal'] and result['soft'] > result['adult']:
            print("노출이 포함된 이미지일 확률이 {}% 입니다.".format(result['soft']*100))
        else :
            print("일반적인 이미지일 확률이 {}% 입니다.".format(result['normal']*100))

    except Exception as e:
        print(str(e))
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Classify adult image.')
    parser.add_argument('image_url', type=str, nargs='?',
        default="http://t1.daumcdn.net/alvolo/_vision/openapi/r2/images/10.jpg",
        help='image url to classify')

    args = parser.parse_args()

    detect_adult(args.image_url)