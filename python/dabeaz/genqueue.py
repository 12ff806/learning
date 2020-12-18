#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def genfrom_queue(thequeue):
    """
    Generate a sequese of items that put onto a queue
    """
    while True:
        item = thequeue.get()
        if item is StopIteration:
            break
        yield item

def sendto_queue(items, thequeue):
    for item in items:
        thequeue.put(item)
    thequeue.put(StopIteration)

if __name__ == "__main__":
    import queue, threading
    def consumer(q):
        for item in genfrom_queue(q):
            print("Consumed", item)
        print("done")

    in_q = queue.Queue()
    con_thr = threading.Thread(target=consumer, args=(in_q,))
    con_thr.start()

    sendto_queue(range(100), in_q)

