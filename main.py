import requests

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
        if r.status_code == 200:
            open(dump_base + info["name"] + ".jpg", "wb").write(r.content)
        result = True
    finally:
        return result


def post_picture(info: dict) -> bool:
    data = {
        "name": info["title"],
        "url": dump_base + info["name"] + ".jpg"
    }

    r = requests.post("https://api.gaein.cn/SeeTheWorld/Pictures", data)
    return r.status_code == 200


if __name__ == '__main__':
    try:
        bing_pic_info = get_picture()
        if bing_pic_info["result"]:
            print("Success get info from Bing.")
            dump_result = dump_picture(bing_pic_info)
            if dump_result:
                post_result = post_picture()
                print("Dump picture success.")
                if post_result:
                    print("Post to API success.")
            else:
                print(f"Dump picture to {dump_base} error!")
        else:
            print("Get picture info from Bing API error!")
    except Exception as e:
        print("Error!" + e)
