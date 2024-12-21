import requests
import streamlit as st
from requests import Response
from requests.exceptions import RequestException,HTTPError
from io import StringIO
from csv import DictReader

@st.cache_data
def get_ubikes()->list[dict]:
    url = "https://data.ntpc.gov.tw/api/datasets/010e5b15-3823-4b20-b401-b1cf000550c5/csv?page=0&size=1000"
    try:
        r:Response = requests.request("GET",url)
        r.raise_for_status()
    except HTTPError as e :
        raise Exception("伺服器錯誤")
    except RequestException as e :
        raise Exception("連線錯誤")
    else:
        print("下載成功")
        file = StringIO(r.text)
        reader = DictReader(file)
        list_reader : list[dict] = list(reader)
        return list_reader