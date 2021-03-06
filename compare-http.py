#!/usr/bin/env python
"""
Example script for testing the response time to fetch 10 and 100 HiPS
tiles using URLlib, Grequests, and asyncio
Author: Adeel Ahmad
"""

import threading
import time

import aiohttp
import asyncio
import grequests
import urllib.request

urls = [
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
]

urls = [
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
    'https://ipwho.is/',
]


@asyncio.coroutine
def fetch_url_aiohttp(url, idx):
    response = yield from aiohttp.request('get', url)
    response.close()


start = time.time()

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(fetch_url_aiohttp(z, i)) for i, z in enumerate(urls)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

print("Elapsed Time aiohttp (with asyncio): %s" % (time.time() - start))


def fetch_url_urllib(url):
    urlHandler = urllib.request.urlopen(url)


start = time.time()

for url in urls:
    urlHandler = urllib.request.urlopen(url)

print("Elapsed Time URLLib (without concurrency): %s" % (time.time() - start))

start = time.time()

threads = [threading.Thread(target=fetch_url_urllib, args=(url,))
           for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Elapsed Time URLLib (with concurrency): %s" % (time.time() - start))

start = time.time()

rs = (grequests.get(u) for u in urls)
grequests.map(rs)

print("Elapsed Time GRequests: %s" % (time.time() - start))