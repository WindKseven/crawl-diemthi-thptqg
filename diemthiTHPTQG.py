import requests
from bs4 import BeautifulSoup
from time import sleep

x =  input("Nhap sbd: ")
results = []
# a = open('diemthi.csv', mode='w', encoding='utf-8')
for sbd in range(int(x), int(x)+1):
    url =  'https://diemthi.vnexpress.net/index/detail/sbd/'+str(sbd)+'/year/2023'
    headers = {'User-Agent': 'Hihihi/5.0'}
    re = requests.get(url = url, headers = headers)
    soup = BeautifulSoup(re.text, "html.parser")
    data = soup.find('table')

    if data is not None: 
        __diemthi_thisinh = f"""
        {data}
        """

        soup__ = BeautifulSoup(__diemthi_thisinh, 'html.parser')

        # Tìm bảng chứa điểm thi
        table = soup__.find('table', class_='e-table')

        sbd_result = f"SBD: {sbd}"
        sleep(0.1)
        # Lặp qua các hàng trong tbody của bảng

        for row in table.find('tbody').find_all('tr'):
            cells = row.find_all('td')
            subject = cells[0].get_text(strip=True)
            score = cells[1].get_text(strip=True)
            sbd_result += f" {subject}: {score}"

        sleep(0.2)
        results.append(sbd_result)

        sleep(0.2)
        # a.write(sbd_result + '\n')

    else: 
        print("Khong tim thay ket qua!") 
        break

if len(results) > 0:
    print("Diem thi cua thi sinh la:",'\n'.join(results))
