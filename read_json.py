import json

# 从 JSON 文件读取数据
with open("./design.json", "r") as file:
    gear_data = json.load(file)

# 打印读取的数据
print("读取的齿轮参数：")
print(json.dumps(gear_data, indent=4))

# 访问具体参数
z1_small = gear_data["gear_pair_1"]["z1_small"]
m12 = gear_data["gear_pair_1"]["m12"]
print(f"z1_small: {z1_small}, m12: {m12} mm")