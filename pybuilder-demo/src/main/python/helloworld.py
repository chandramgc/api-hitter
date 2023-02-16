import sys
import time

def main():
    run()


def run (filter = dict({'Directory':'/Ref/user/value'}), 
cache_args = dict({'cachepath':['refdata', 'trade'], 'field': ['trade','product']})):
   print(filter['Directory'])
   print(cache_args['cachepath'])


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f'Process takes {time.time() - start_time} seconds')