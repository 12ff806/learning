#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from twilio.rest import Client


account_sid = "ACd156d1766833bd39d2bc107251a539a9"
auth_token = "46a98e4a98dca32cc0786d838f9f0562"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+8618501257774",
                                             from_="+18058709600",
                                             body="您好,你得记得要去编程呐!")
