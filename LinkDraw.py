import requests, json, datetime, os, time

class LinkDraw:

    def __init__(self):
        self.__headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        self.__url_list = ["https://api.vc.bilibili.com/link_draw/v2/Doc/index?type=recommend&page_num={}&page_size=45",
                           "https://api.vc.bilibili.com/link_draw/v2/Doc/list?category=all&type=hot&page_num={}&page_size=20"]
        self.__url_detail = "https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id={}"
        self.__kind = 0
        self.__range_page = 5
        self.__downCount = 0
        self.__file_path = ""
        # check flag
        self.__check_flag = {
            "view_count": 1000,
            "collect_count": 0,
            "vote_count": 0,
            "comment_count": 0
        }

    def set_kind(self, value):
        self.__kind = value

    def set_range_page(self, value):
        self.__range_page = value

    def set_check_flag(self, modify_list):
        for flag, value in modify_list.items():
            self.__check_flag[flag] = value

    def run(self):
        runTime = datetime.datetime.now()
        self.__file_path = runTime.strftime("%Y-%m-%d")
        if not os.path.exists(self.__file_path):
            os.mkdir(self.__file_path)
        for page in range(self.__range_page):
            url = self.__url_list.format(page)
            response = requests.get(url, headers=self.__headers)
            items = json.loads(response.text)["data"]["items"]
            for elem in items:
                self.__checkAttri(elem["item"]["doc_id"])
                time.sleep(1)

    def __checkAttri(self, doc_id):
        url = self.__url_detail.format(doc_id)
        response = requests.get(url, headers=self.__headers)
        if response.status_code != 200: return
        content = json.loads(response.text)["data"]
        user = content["user"]
        item = content["item"]

        for flag, value in self.__check_flag.items():
            if item[flag] < value:
                print("× 用户 {} 的 {} 不符合需求 LinkDraw！".format(user["name"], item["title"]))
                return

        print("√ 正在获取 {} 的 {} LinkDraw！".format(user["name"], item["title"]))
        for elem in item["pictures"]:
            url_img = elem["img_src"]
            kind = url_img.split(".")[-1]
            path = self.__file_path + "\\" + str(self.__downCount) + "." + kind
            img = requests.get(url_img, headers=self.__headers)
            with open(path, 'bw') as f:
                f.write(img.content)
            self.__downCount += 1
            time.sleep(0.5)
        print("\t操作完成，共获取 {} 张！".format(len(item["pictures"])))