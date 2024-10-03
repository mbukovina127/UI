from operator import index
from queue import Queue
import random

import myUtils
from gen import neighbour_swap, random_swap, reverse_segment, move_city
from salesperson import Salesperson


class TabooGuy(Salesperson):
    def __init__(self, path: list, taboo_size: int):
        super().__init__(path)
        self.taboo = Queue(taboo_size)
        self.o_min_length = myUtils.length_of_path(self.path)
        self.o_min_path = self.path
    def add_to_queue(self, item):
        if self.taboo.full():
            self.taboo.get()
        self.taboo.put(item)

    def find_better_paths(self, amount: int):
        m_paths = list()
        # print("INFO appending paths")
        for i in range(amount):
            m_paths.append(self.find_path())
#         print("DONE")
#         print("INFO sorting paths")
        m_paths.sort(key=lambda x: myUtils.length_of_path(x[1]))
#         print("DONE")

        itt = 0
        while (m_paths[itt][0]) in self.taboo.queue:
            # print("INFO path " + str(m_paths[itt][0]) + " already in queue")
            itt += 1
        self.add_to_queue(m_paths[itt][0])
        new_best = m_paths[itt][1]
        if myUtils.length_of_path(new_best) < self.o_min_length:
            self.o_min_length = myUtils.length_of_path(new_best)
            self.o_min_path = new_best
            # print("INFO new best path length: " + str(myUtils.length_of_path(self.o_min_path)))
        self.path = new_best

        return m_paths[itt]


    def find_path(self):
        # print("INFO: mutating path")
        copy = list(self.path)

        # mutations
        neighbour_swap(copy)
        while random.randint(0,9) < 9:
            if random.randint(0,9) < 9:
                move_city(copy)
            if random.randint(0,9) < 6:
                neighbour_swap(copy)
            if random.randint(0,9) < 5:
                random_swap(copy)
        if random.randint(0, 9) < 6:
            reverse_segment(copy)


        hash_n = 0
        index = 0
#         print("INFO calculating hash")
        for n in copy:
            hash_n += ((n.x * n.y) & 511) * index
            index += 1
#         print("DONE: " + str(hash_n))
        return [hash_n, copy]