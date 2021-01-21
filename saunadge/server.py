import requests
import os
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)

BASE_URL = "https://sauna-ikitai.com/saunners/"


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
        "label": "sakatsu",
        "message": sakatsu,
        "color": "0051e0",
        "cacheSeconds": 1800,
    }


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0",
            port=int(os.environ.get("PORT", 8080)))
