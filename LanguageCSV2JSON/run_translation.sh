#!/bin/bash
# 切換到腳本所在的目錄
cd "$(dirname "$0")"

# 執行 translationCSV.py 腳本並傳入當前目錄
python3 translationCSV.py "$(pwd)"

# 完成訊息
echo "CSV 轉換已完成！"