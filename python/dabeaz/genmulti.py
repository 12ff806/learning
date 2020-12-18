#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import queue, threading
from genqueue import genfrom_queue, sendto_queue
from gencat import gen_cat


def multiplex(sources):
    """ Generate items from multiple generators
    """
    in_q = queue.Queue()
    consumers = []
    for src in sources:
        thr = threading.Thread(target=sendto_queue,
                               args=(src, in_q))
        thr.start()
        consumers.append(genfrom_queue(in_q))
    return gen_cat(consumers)

def gen_multiplex(genlist):
    item_q = queue.Queue()
    def run_one(source):
        for item in source:
            item_q.put(item)

    def run_all():
        thrlist = []
        for source in genlist:
            t = threading.Thread(target=run_one, args=(source,))
            t.start()
            thrlist.append(t)
        for t in thrlist:
            t.join()
        item_q.put(StopIteration)

    threading.Thread(target=run_all).start()
    while True:
        item = item_q.get()
        if item is StopIteration:
            return
        yield item

if __name__ == "__main__":
    from follow import follow

    log1 = follow(open("run/foo/access-log"))
    log2 = follow(open("run/bar/access-log"))
    
    log = multiplex([log1, log2])
    
    for line in log:
        print(line, end='')

