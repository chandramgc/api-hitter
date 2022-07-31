from email import header
import http.client
import platform
import csv
import json
import base64
import asyncio
import time
from aiohttp import ClientSession, ClientResponseError

def main():
    if platform.system()=='Windows':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(excuteRunbook())

async def excuteRunbook():
    with open('runbook.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        row_count = 0
        header = 1
        stats = myDict()
        resp_stats = myDict()
        tasks = []
        async with ClientSession() as session:
            for row in csv_reader:
                if line_count > 0:
                    if (str(row[0]) == "active"):
                        task = asyncio.ensure_future(callApi(session, str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5])))
                        # print("task-"+str(task.result))
                        resp_stats.add(line_count, [str(row[1]),row[6]])
                          
                        tasks.append(task)             
                line_count += 1                        
            responses = await asyncio.gather(*tasks)
            for response in responses:
                row_count += 1
                # print("resp)
                row = resp_stats[row_count]
                expect_response = "200";
                current_response = str(response)
                # print(expect_response)
                # print(current_response)
                if (expect_response == current_response):
                    stats.add(row_count, [str(row[0]),"working"])
                else:
                    stats.add(row_count, [str(row[0]),"not working"]) 
        printTable(stats)          
        
async def callApi(session,url,parameters,method,headers,payload):
    # print(url+method+headers+payload)
    try:
        async with session.get("https://"+url, timeout=60) as response:
            # resp = await response.json()
            resp = response.status 
            # print("resp-"+str(resp))
    except Exception as e:
        print("Exception : "+str(e.with_traceback))
    else:
        return resp
    return


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

