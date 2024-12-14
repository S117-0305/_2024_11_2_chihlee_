import tools

try:
    ubike_data:list[dict] = tools.get_ubikes()
except Exception as e:
    print(e)
else:
    print(ubike_data)