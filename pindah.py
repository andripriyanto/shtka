import os
import shutil
import pandas as pd

excel_path = 'data_siswa.xlsx'
source_folder = 'files'
target_root = 'output'

# PAKSA NISN SEBAGAI STRING
df = pd.read_excel(excel_path, dtype={'NISN': str})

mapping = {}

for _, row in df.iterrows():
    nisn = row['NISN'].strip()
    rombel = str(row['Rombel']).strip()
    mapping[nisn] = rombel

for filename in os.listdir(source_folder):
    file_path = os.path.join(source_folder, filename)

    if not os.path.isfile(file_path):
        continue

    if ' - ' not in filename:
        print(f'Format tidak sesuai, skip: {filename}')
        continue

    nisn = filename.split(' - ')[0].strip()

    if nisn in mapping:
        rombel = mapping[nisn]
        target_folder = os.path.join(target_root, rombel)
        os.makedirs(target_folder, exist_ok=True)

        dst = os.path.join(target_folder, filename)
        shutil.copy2(file_path, dst)  # pakai copy dulu biar aman
        print(f'OK: {filename} -> {rombel}')
    else:
        print(f'NISN tidak ditemukan di Excel: {filename}')
