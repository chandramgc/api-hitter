import requests

url = "https://raw.githubusercontent.com/chandramgc/yaml-reader-private/main/invoice.yaml"

payload={}
headers = {
  'Authorization': 'token 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'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)