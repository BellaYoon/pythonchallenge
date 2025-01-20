import pandas as pd
import requests
from google.colab import userdata

apikey = userdata.get('apikey')

url = 'https://ecos.bok.or.kr/api/KeyStatisticList/' + apikey + '/json/kr/1/10'
response = requests.get(url)

data = response.json()

df = pd.DataFrame(data['KeyStatisticList']['row'])
df
