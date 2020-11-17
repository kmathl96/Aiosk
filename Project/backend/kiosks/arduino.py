import json, serial, requests

URL = 'http://aiosk.co.kr/wait'
arduino_port = 'COM3'

ser = serial.Serial(
    port=arduino_port,
    baudrate=9600,
)

print('아두이노와 통신 시작')
print(f'아두이노의 접속 포트는 {arduino_port}\n')

while True:
    try:
        if ser.readable():
            res = ser.readline()
            json_data = json.loads(res.decode()[:-1])
            print(json_data)

            client = requests.session()
            client.get(URL)

            response = client.post(URL, data=json_data)
            print(response)

        except serial.serialutil.SerialException:
            print('아두이노가 연결되어 있지 않음')
            break
        except requests.exceptions.ConnectionError:
            print('인터넷 전송 불가능')
            break
        except KeyboardInterrupt:
            print('아두이노 시리얼 통신 중단')
            break