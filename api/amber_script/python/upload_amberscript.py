import requests

url = 'https://api.amberscript.com/api/jobs/upload-media'
filepath = './finish_sample.mp3'
querystring = {"jobType":"direct","language":"fi","transcriptionType":"transcription","apiKey":"26fe6e92ac6ec36f7cb5c311dd36436fd"}
files = {'file': open(filepath, 'rb')}

response = requests.post(url, files=files, verify=False, params=querystring)

print(response.status_code)
print(response.text)
