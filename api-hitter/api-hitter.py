from email import header
import http.client
import csv
import json
import base64
import time

def main():
    excuteRunbook()

def excuteRunbook():
    with open('runbook.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        header = 1
        stats = myDict()
        for row in csv_reader:
            if line_count > 0:
                if (str(row[0]) == "active"):
                    response = callApi(str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]))
                    expect_response = convertBase64(row[6])
                    current_response = convertBase64(response)
                    if (expect_response == current_response):
                        stats.add(line_count, [str(row[1]),"working"])
                    else:
                        stats.add(line_count, [str(row[1]),"not working"])                
            line_count += 1
        printTable(stats)

def callApi(url,parameters,method,headers,payload):
    # print(url+method+headers+payload)
    conn = http.client.HTTPSConnection(str(url))
    parameters_val = "/?"+ parameters if str(parameters) != "" else "/"
    headers_val = json.loads(headers) if str(headers) != "" else json.loads("{}")
    payload_val = json.loads(payload) if str(payload) != "" else json.loads("{}")
    conn.request(method, parameters_val, payload_val, headers_val)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    # print(data.decode("utf-8"))
    return data

def convertBase64(value):
    message = str(value)
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

def printTable(myDict):
    print ("{:<8} {:<15} {:<15}".format("Index","Status","API"))
    for k, v in myDict.items():
        api, status = v
        print ("{:<8} {:<15} {:<15}".format(k, status, api))

class myDict(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        #self[key] = value # add new key and value overwriting any exiting same key
        if self.get(key)!=None:
            print('key', key, 'already used') # report if key already used
        self.setdefault(key, value) # if key exit do nothing

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f'Process takes {time.time() - start_time} seconds')

