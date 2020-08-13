#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Jul 31 2017
# by Sin

"""Query Train Tickets via CLI

Usage:
    tickets.py [-cgdztkl] <from_station_name> <to_station_name> <date>

Options:
    -h --help   显示帮助信息
    -c          城际
    -g          高铁
    -d          动车
    -z          直达
    -t          特快
    -k          快速
    -l          绿皮

"""


from docopt import docopt
from prettytable import PrettyTable
from colorama import Fore
from url_request import get_page_source
import station_list
from config import ticket_query_url_template, ticket_query_headers
import sys
import json


def get_ticket_query_url(from_station_name, to_station_name, date):
    from_station_telecode = station_list.get_station_telecode(from_station_name)
    to_station_telecode = station_list.get_station_telecode(to_station_name)
    ticket_query_url = ticket_query_url_template.format(date, from_station_telecode, to_station_telecode)
    return ticket_query_url


def get_ticket_list(ticket_query_url, ticket_query_headers):
    ticket_page = get_page_source(ticket_query_url, ticket_query_headers)
    try:
        ticket_list = json.loads(ticket_page)["data"]["result"]
    except KeyError as e:
        raise e
    except json.decoder.JSONDecodeError as e:
        raise e
    return ticket_list


def parse_ticket():
    ticket_dict = {}
    try:
        while True:
            ticket = yield ticket_dict
            ticket = ticket.split("|")
            ticket_dict = {
                "train_no": ticket[3],
                "comments": ticket[1],
                "from_station_telecode": ticket[6],
                "to_station_telecode": ticket[7],
                "from_station_name": station_list.get_station_name(ticket[6]),
                "to_station_name": station_list.get_station_name(ticket[7]),
                "start_time": ticket[8],
                "arrive_time": ticket[9],
                "total_time": ticket[10],
                "can_web_buy": ticket[11],
                "gaoji_soft_bed": ticket[21] or "--",
                "soft_bed": ticket[23] or "--",
                "soft_seat": ticket[24] or "--",
                "no_seat": ticket[26] or "--",
                "hard_bed": ticket[28] or "--",
                "hard_seat": ticket[29] or "--",
                "second_level_seat": ticket[30] or "--",
                "first_level_seat": ticket[31] or "--",
                "business_seat": ticket[32] or "--",
                "dong_bed": ticket[33] or "--"
            }
            
    except GeneratorExit as e:
        pass


def show_tickets(ticket_list, options, parse_ticket):
    table_show = PrettyTable()
    table_show.field_names = ["车次", "站点", "时间", "历时", "商务座", "一等座", "二等座", "高级软卧", "软卧", "动卧", "硬卧", "软座", "硬座", "无座", "备注"]
    
    for ticket in ticket_list:
        ticket_dict = parse_ticket.send(ticket)
        
        train_category = ticket_dict["train_no"][0].lower()
        if not options or train_category in options or (train_category not in "dgctzk" and "l" in options):
            table_show.add_row([
                ticket_dict["train_no"],
                "\n".join([Fore.GREEN + ticket_dict["from_station_name"] + Fore.RESET, Fore.LIGHTRED_EX + ticket_dict["to_station_name"] + Fore.RESET]),
                "\n".join([Fore.GREEN + ticket_dict["start_time"] + Fore.RESET, Fore.LIGHTRED_EX + ticket_dict["arrive_time"] + Fore.RESET]),
                ticket_dict["total_time"],
                ticket_dict["business_seat"],
                ticket_dict["first_level_seat"],
                ticket_dict["second_level_seat"],
                ticket_dict["gaoji_soft_bed"],
                ticket_dict["soft_bed"],
                ticket_dict["dong_bed"],
                ticket_dict["hard_bed"],
                ticket_dict["soft_seat"],
                ticket_dict["hard_seat"],
                ticket_dict["no_seat"],
                (ticket_dict["can_web_buy"] == "Y" and Fore.BLUE + ticket_dict["comments"] + Fore.RESET) or ticket_dict["comments"]
            ])

    parse_ticket.close()
    print(table_show)


if __name__ == "__main__":
    arguments = docopt(__doc__, version='cattle 1.0')
    from_station_name = arguments.get("<from_station_name>")
    to_station_name = arguments.get("<to_station_name>")
    date = arguments.get("<date>")
    options = "".join([key for key, value in arguments.items() if value is True])
    
    # 处理站名错误导致的异常
    try:
        ticket_query_url = get_ticket_query_url(from_station_name, to_station_name, date)
    except ValueError:
        print("站名输入有误!!")
        sys.exit()

    # 处理日期错误导致的异常
    try:
        ticket_list = get_ticket_list(ticket_query_url, ticket_query_headers)
    except KeyError:
        print("请检查日期是否在预售日期范围内!!")
        sys.exit()
    except json.decoder.JSONDecodeError:
        print("日期输入有误!! 格式应为: '2017-01-30'")
        sys.exit()
    if not ticket_list:
        print("没有查询到任何车次!!")
        sys.exit()

    pt = parse_ticket()
    pt.send(None)
    show_tickets(ticket_list, options, pt)


