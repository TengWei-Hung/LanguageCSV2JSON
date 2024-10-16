import sys
import os
import csv
import json
from collections import defaultdict

# 檢查是否有傳入參數
if len(sys.argv) < 2:
    print("請提供腳本所在的目錄路徑！")
    sys.exit(1)

# 取得傳入的路徑
base_path = sys.argv[1]

# CSV 檔案路徑
csv_file_path = os.path.join(base_path, "languagesCSV.csv")

# 創建 languages 資料夾
languages_folder = os.path.join(base_path, "languages")
if not os.path.exists(languages_folder):
    os.makedirs(languages_folder)

# 語系列表
languages = ["en-us", "id-id", "ja-jp", "ko-kr", "th-th", "vi-vn", "zh-cn"]

# 初始化字典來存儲每個語言的翻譯
translations = defaultdict(dict)

# 讀取 CSV 檔案
with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # 遍歷每一行
    for row in csv_reader:
        key = row["String"]  # 對應你的 "String" 標籤
        
        # 將每個語言的翻譯加入對應的字典
        for language in ["zh-cn", "en-us", "vi-vn", "ja-jp", "ko-kr", "th-th", "id-id"]:
            translations[language][key] = row[language]

# 將每個語言的翻譯保存為單獨的 JSON 文件
for language, translation_data in translations.items():
    # 文件保存路徑為 languages 資料夾下的 {language}.json
    json_file_path = os.path.join(languages_folder, f'{language}.json')
    
    # 將翻譯數據保存到 lang.json 文件中
    with open(json_file_path, 'w', encoding='utf-8') as json_file:
        json.dump(translation_data, json_file, ensure_ascii=False, indent=4)

    print(f"翻譯已保存到 {json_file_path}")