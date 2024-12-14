from tools import taipei

try:
    ubike_data:list[dict] = taipei.get_ubikes()
except Exception as e:
    print(e)
else:
    print(ubike_data)