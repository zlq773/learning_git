import requests
import json

class ShuCaiSpider():
    def __init__(self):
        self.url = "http://www.cncyms.cn/pages.php"
        self.headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

    def send_requset(self,form_data):
        reponse = requests.post(url=self.url,data=form_data,headers=self.headers)
        if reponse.status_code == 200:
            return reponse

    def parse_content(self,reponse):
        json_content = reponse.json()
        self.write_content(json_content)

    def write_content(self,content):
        with open('shucai.json',"w",encoding="utf8") as f:
            # data = json.dumps(content)
            json.dump(content,f,indent=4,ensure_ascii=False)

    def start(self):
        self.pname= input("请输入蔬菜名称：")
        from_data = {
                     "pageNum": 1,
                     "pname": self.pname,
                     "reltime": "蔬菜"
                     }
        reponse=self.send_requset(from_data)
        if reponse:
            self.parse_content(reponse)





if __name__ == '__main__':
    scc = ShuCaiSpider()
    scc.start()