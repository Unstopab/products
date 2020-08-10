import os # operating system，載入OS來檢查電腦是否有該檔案

# 開始讀取檔案
def read_file(filename):
    products = []
    with open(filename, "r", encoding = "utf-8") as f:
        for line in f:
            if "商品,價格" in line:
                continue #繼續
            name, price = line.strip().split(",")
            products.append([name, price])
    return products
# 讓使用者輸入商品與價格
def user_input(products):
    while True:
        name = input("請輸入商品名稱(輸入q則結束登記)：")
        if name == "q":
            break
        price = input("請輸入商品價格：")
        price = int(price)
        products.append([name, price])
    print(products)
    return products
# 印出商品與價格
def print_product(products):
    for p in products:
        print(p[0], "的價格是", p[1]) #因為此function只是印出東西，所以不用return值
# 寫入檔案
def write_file(filename, products):
    with open(filename, "w", encoding = "utf-8") as f:
        f.write("商品,價格\n")
        for p in products:
            f.write(p[0] + "," + str(p[1]) + "\n")

def main():
    filename = "products.csv"
    if os.path.isfile(filename): #檢查檔案在不在
        print("水哦!有找到檔案了!")
        products = read_file(filename)
    else:
        print("找不到檔案QQ\n但就讓我們新建立檔案吧!")

    products = user_input(products)
    print_product(products)
    write_file("products.csv", products)

main()