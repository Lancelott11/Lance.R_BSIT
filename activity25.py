Samsung_s26_ultra = "The Samsung Galaxy S26 Ultra features a 6.9-inch Dynamic AMOLED 2X display (3120×1440), /n /" 
" Snapdragon 8 Elite Gen 5 chipset, /n /"
" up to 16GB RAM, /n /"
" up to 1TB storage, /n /"
" a 200MP quad‑camera system, /n /"
" and a 5000mAh battery."

Samsung = ["Samsung_s25_ultra","Samsung_s26_ultra"]
Android = ["Vivo", "Samsung", "Realme", "Redmi", "poco"]
cellphone = ["Android", "IOS"]
Tablet = ["Xiomi", "IOS"]
laptop = ["windows", "mac"]
devices = {"good" : "cellphone", "great" : "Tablet", "devine" : "laptop"}

print(devices["good"][0][1])