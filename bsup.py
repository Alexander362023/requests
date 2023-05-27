import requests
from pprint import pprint

URL = 'https://akabab.github.io/superhero-api/api/all.json'
f = requests.get(URL)
response_dict = f.json()

for p in response_dict:
    o = p['name']
    '''Подскажите почему в каком бы порядке в списке g не стояли герои выводится отсортировочное итоговое значене, герой "intelligence" '''      
    g = ['Hulk', 'Captain America', 'Thanos'] 
    if o in g:
        print(o)       
        f = p["powerstats"]    
        for u in f.keys():
            if u == "intelligence":                
                print(f[u])
print('Самый умный Thanos')

# ..............2 задача..................................

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    
    def get_headers(self):
        '''Информацию которую надо обязательно запрашивать'''
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
             
    def _get_upload_link(self, disk_file_path):
        '''получает ссылку от яндекс диска на загрузку'''

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()        

    def upload_file_to_disk(self, disk_file_path, filename):
        ''''Загружает файл на яндекс диск'''
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")       

if __name__ == '__main__':
    
    disk_file_path = "/Нетология/полигон.txt"
    token = ' ' 
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(disk_file_path, 'полигон.txt')

    