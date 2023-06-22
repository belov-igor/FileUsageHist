# -*- coding: utf-8 -*-
from scripts.FileUsageReport import FileSystemUsageHist

hosts = ['host1', "host2", "host3", 'host4', 'host5']
user = 'root'
# all_reports = {}
#
report = FileSystemUsageHist(username=user, hosts=hosts)
print(report)
