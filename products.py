import os # operating system，載入OS來檢查電腦是否有該檔案

products = []
if os.path.isfile("product.csv"):
    print("水哦!有找到檔案了!")
	# 開始讀取檔案
    with open("product.csv", "r", encoding = "utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue #繼續
            name, price = line.strip().split(",")
            products.append([name, price])

    print(products)
else:
	print("找不到檔案QQ\n但就讓我們新建立檔案吧!")

# 讓使用者輸入商品與價格
while True:
    name = input("請輸入商品名稱(輸入q則結束登記)：")
    if name == "q":
        break
    price = input("請輸入商品價格：")
    price = int(price)
    products.append([name, price])
print(products)

# 印出商品與價格
for p in products:
    print(p[0], "的價格是", p[1])

# 寫入檔案
with open("product.csv", "w", encoding = "utf-8") as f:
    f.write("商品,價格\n")
    for p in products:
        f.write(p[0] + "," + str(p[1]) + "\n")