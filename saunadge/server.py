import requests
import os
from bs4 import BeautifulSoup
from flask import Flask
import argparse

app = Flask(__name__)

BASE_URL = "https://sauna-ikitai.com/saunners/"

parser = argparse.ArgumentParser(
    description="generate sakatsu badge from SAUNA IKITAI"
)
parser.add_argument(
    "-i",
    "--id",
    required=True,
    help="sauna-ikitai id",
)


@app.route("/api/v1/badge/<int:user_id>")
def tonttu_badge(user_id):
    res = requests.get(BASE_URL + f"{user_id}")
    soup = BeautifulSoup(res.text, "html.parser")

    sakatsu = (soup.find('body').find('div', class_='l-containers js-containers').find(
        'div', class_='l-content is-noPaddingBottom').find('div', class_='p-mypage').find("ul", class_="p-localNav_links js-swipeScrollInner is-noborder")
        .find_all("li", class_="p-localNav_link")[0].find("span")
        .find("span", class_="p-localNav_count").get_text().strip()
    )

    return {
        "schemaVersion": 1,
        "label": "Sakatsu",
        "message": sakatsu,
        "color": "0051e0",
        "cacheSeconds": 1800,
        "logoSvg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 54.5 57.5"><defs><style>.cls-1{fill:#fff;}</style></defs><g id="レイヤー_2" data-name="レイヤー 2"><g id="レイヤー_1-2" data-name="レイヤー 1"><path class="cls-1" d="M6.6,36,6,46.2c7.5-3.5,13.1-6.1,16.1-7.4l.3-7.7c2.6-1.8,4.7-2.4,6.8-1.9C27.1,39.2,16.4,55,14.3,57.5,23.1,55.4,37.1,52,37.1,52A69.42,69.42,0,0,0,47.2,25.3c3.5.4,5.6-.3,6.4-1.7l.9-18.1a8.94,8.94,0,0,1-5.9,1.2L48.9,0,30.2,4.4l-.4,6.5a10.93,10.93,0,0,0-6.3,1.5l.3-6.5L8.1,9.9l-.5,7.3c-1.5.7-4,.7-6.6.4L0,36.5C2.3,37.2,4.4,37.4,6.6,36Z"/></g></g></svg>',
    }


def cli():
    args = parser.parse_args()
    id = args.id
    print(
        f"[![sakatsu badge](https://img.shields.io/endpoint.svg?url=https://saunadge-gjqqouyuca-an.a.run.app/api/v1/badge/{id}&style=flat-square)](https://sauna-ikitai.com/saunners/{id})")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
