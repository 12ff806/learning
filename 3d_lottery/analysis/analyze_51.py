#!/usr/bin/env python3


__doc__ = "按照前5组推算下一组中奖号码"
__author__ = "12ff806"


import csv


class Analyze(object):
    """
    分析特定算法的中奖概率
    """
    def __init__(self):
        # csv文件名
        #self._csv_fn = "../data/3d_lottery.csv"
        self._csv_fn = "../data/3d_lottery_2015_2018.csv"

        # 所有的开奖数据
        self._data = []

        # 0-9的集合
        self.num_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

        # 每次中奖奖金
        self._prize_money = 2000
        
        # 每次购买的金额
        self._purchase_money = 108
        
        # 总共中奖次数
        self._prize_num = 0

        # 总共买的期数
        self._purchase_num = 0

        # 总成本投入
        self._cost = 0

        # 每一轮购买期数
        self._purchase_num_per_circle = 0

        # 中奖记录
        self._winning_record = []

    def load_data(self):
        """
        从csv载入数据
        """
        with open(self._csv_fn, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar=',')
            reader.__next__()
            for row in reader:
                t = tuple(row[0].split(","))
                #print(t)
                self._data.append(t)

            #print(self._data)

    def calc(self):
        """
        按5推1的方式计算中奖情况
        """
        for index in range(len(self._data)-5):
            one = self._data[index]
            two = self._data[index+1]
            three = self._data[index+2]
            four = self._data[index+3]
            five = self._data[index+4]
            six = self._data[index+5]
            
            six_prize_num = (int(six[2]), int(six[3]), int(six[4]))
            
            s = set()
            for i in range(2, 5):
                s.add(int(one[i]))
                s.add(int(two[i]))
                s.add(int(three[i]))
                s.add(int(four[i]))
                s.add(int(five[i]))
            
            diff_set = self.num_set - s
            # 购买
            if len(diff_set) == 2:
                # 中奖了
                if diff_set.pop() in six_prize_num and diff_set.pop() in six_prize_num:
                    self._winning_record.append((six[1], self._purchase_num_per_circle+1))
                    self._purchase_num_per_circle = 0
                    self._prize_num += 1
                    self._purchase_num += 1
                # 没中奖
                else:
                    self._purchase_num_per_circle += 1
                    self._purchase_num += 1
            # 不购买
            else:
                pass

        print("中奖记录: ", self._winning_record)
        print("总中奖次数: ", self._prize_num)
        print("总中奖金额: ", self._prize_num * self._prize_money)
        print("总购买次数: ", self._purchase_num)
        print("总成本: ", self._purchase_num * self._purchase_money)
        print("总收入: ", self._prize_num * self._prize_money - self._purchase_num * self._purchase_money)


if __name__ == "__main__":
    a = Analyze()
    a.load_data()
    a.calc()
    
