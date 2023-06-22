# -*- coding: utf-8 -*-

from scripts.FileUsageReport import FileSystemUsageHist
from config.hosts import USER, HOSTS

if __name__ == '__main__':
    report = FileSystemUsageHist(username=USER, hosts=HOSTS)
    print(report.run())
