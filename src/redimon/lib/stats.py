# -*- coding: utf-8 -*-

import redis, datetime, simplejson

class RedisMonitor(object):

    def __init__(self, servers):
        self.servers = servers

    def getStats(self, json = False):
        response = []
        for server in self.servers:
            response.append(self.getStatsPerServer(server))

        if json:
            for item in response:
                for key, value in item.items():
                    new_key = item.get("addr") + "_" + key
                    item.update({new_key: value})

        return response

    def getStatsPerServer(self, server):

        try:
            connection = redis.Redis(host=server[0], port=server[1], db=0)
            info       =  connection.info()
            info.update({
                "server_name"        : server,
                "status"             : "up",
                "last_save_humanized": datetime.datetime.fromtimestamp(info.get("last_save_time"))
            })

            connection.connection.disconnect()

        except redis.exceptions.ConnectionError:
            info =  {
                "status"            : "down",
                "server_name"       : server,
                "connected_clients" : 0,
                "used_memory_human" : '?',
            }

        info.update({
            "addr": info.get("server_name")[0].replace(".", "-")
        })

        return info
