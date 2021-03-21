import requests
import os

dump_base = "/data/img/bing/"


def get_picture() -> dict:
    result = {
        "result": False,
        "title": str,
        "url": str,
        "name": str
    }

    url = "https://cn.bing.com/HPImageArchive.aspx?format=js&n=1&pid=hp"
    r = requests.get(url)

    if r.status_code == 200:
        print("Bing return:" + r.text)
        try:
            today_pic = r.json()["images"][0]

            result["result"] = True
            result["title"] = today_pic["copyright"]
            result["url"] = "https://cn.bing.com" + today_pic["url"]
            result["name"] = today_pic["enddate"]
        finally:
            return result


def dump_picture(info: dict) -> bool:
    result = False
    r = requests.get(info["url"])
    try:
        path = f"{dump_base}{info['name']}.jpg"
        if r.status_code == 200:
            if not os.path.exists(path):
                open(path, "wb").write(r.content)
                result = True
    finally:
        return result


def post_picture(info: dict) -> bool:
    data = {
        "name": info["title"],
        "url": dump_base + info["name"] + ".jpg"
    }

    r = requests.post("https://api.gaein.cn/SeeTheWorld/Pictures", data)
    status_code = r.status_code
    print("API return:" + str(status_code))
    return status_code == 200


if __name__ == '__main__':
    try:
        bing_pic_info = get_picture()
        if bing_pic_info["result"]:
            print("Success get info from Bing.")
            dump_result = dump_picture(bing_pic_info)
            if dump_result:
                post_result = post_picture(bing_pic_info)
                print("Dump picture success.")
                if post_result:
                    print("Post to API success.")
                else:
                    print("Post to API error!")
            else:
                print(f"Dump picture to {dump_base} error!")
        else:
            print("Get picture info from Bing API error!")
    except Exception as e:
        print("Error!" + str(e))
