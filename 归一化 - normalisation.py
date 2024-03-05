# -*- coding: utf-8 -*-
# Time : 2024/1/9
# Author : ZYY, Wang
# File : 归一化.py
import pandas as pd

# 读取Excel文件
excel_file_path = 'D:\\2.xlsx'  
df = pd.read_excel(excel_file_path)

# 对每进一列行归一化（MinMax归一化）
normalized_df = (df - df.min()) / (df.max() - df.min())

# 保存归一化后的数据到新的Excel文件
normalized_excel_file_path = 'D:\\1.xlsx'  
normalized_df.to_excel(normalized_excel_file_path, index=False)

print(f"已对每一列进行归一化，并保存到 {normalized_excel_file_path}")
