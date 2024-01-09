import json
import csv


json_file_path = r"C:\Users\대원\Downloads\Telegram Desktop\device-25f906ea2ec41cc2 (2).json"

csv_file_path = r"C:\Users\대원\Downloads\Telegram Desktop\data.csv"

with open(json_file_path, 'r') as jsonfile:
    json_data = json.load(jsonfile)


with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = ['Range', 'Temp']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for item in json_data:
        object_json = item['payload']['objectJSON']
        decode_data_string = json.loads(json.loads(object_json)['DecodeDataString'])
        writer.writerow(decode_data_string)

print("json파일이  csv파일로 저장되었습니다")