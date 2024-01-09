import json
import csv


json_file_path = r"C:\Users\대원\Downloads\Telegram Desktop\device-25f906ea2ec41cc2 (2).json"

csv_file_path = r"C:\Users\대원\Downloads\Telegram Desktop\data.csv"

with open(json_file_path, 'r') as jsonfile:
    json_data = json.load(jsonfile)


with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = json_data[0]['payload'].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for item in json_data:
        writer.writerow(item['payload'])

print("json파일이  csv파일로 저장되었습니다")