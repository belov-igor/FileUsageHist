import copy
import os
import subprocess


class FileSystemUsageHist:
    """
    # Класс-обработчик данных, полученных с adaptec для подключенных дисков командой arcconf getsmartstats
    # Выходные данные: drives_count - количество дисков, подключенных к adaptec;
    #                 adaptec_name - имя adaptec;
    #                 report - итоговый отчет в виде словаря.
    """

    def __init__(self, username, hosts):
        """
        :param username: имя пользователя при подключении к удаленному хосту
        :param hostname: имя удаленного хоста
        """

        self.hostname = str()
        self.username = username
        self.hosts = hosts
        self.report = dict()
        self.drives_count = 0
        self.adaptec_name = str()
        self.data = None

    def get_filesystem_usage_data(self, hostname):
        """
        Подключение к хостам по ssh, получение и обработка отчета (TODO adaptec arcconf getsmartstats) по всем дискам.

        :return:
        """
        self.hostname = hostname

        # Подключение к хостам по ssh, получение данных командой "df"
        connect = subprocess.run(
            ["ssh", f"{self.username}@{self.hostname}", "df"], stdout=subprocess.PIPE)
        self.data = connect.stdout.decode().split('\n')
        # print(self.data)

    def get_report(self):
        """
        Обработка и получение необходимых данных о

        :return:
        """
        for string in self.data:
            if "vol" in string:
                vol = string.split()[-1]
                percent = int(string.split()[-2][:-1])
                # available = f'{round((int(string.split()[-3])) / (1024**2), 3)} GB'
                # available = f'{string.split()[-3]}B'
                available = round((int(string.split()[-3])) / (1024 ** 2), 2)
                self.report.update({f'{self.hostname}{vol}': [available, percent]})

    def run(self):
        """
        Запуск обработчика.
        :return: drives_count - количество дисков, подключенных к adaptec;
                 adaptec_name - имя adaptec;
                 report - итоговый отчет в виде словаря
        """
        # Получение и обработка данных
        for host in self.hosts:
            self.get_filesystem_usage_data(hostname=host)
            self.get_report()

        return self.report
