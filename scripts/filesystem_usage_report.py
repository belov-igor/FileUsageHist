import subprocess


class FileSystemUsageReport:
    """
    Класс для получения отчета об использовании файловой системы на удаленных хостах.
    """

    def __init__(self, username, hosts):
        """
        :param username: имя пользователя при подключении к удаленному хосту;
        :param hosts: список удаленных хостов
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
        Получение данных об использовании файловой системы на удаленном хосте.
        :param hostname: Имя удаленного хоста.
        :return: None.
        """
        self.hostname = hostname

        # Подключение к хостам по ssh, получение данных командой "df"
        connect = subprocess.run(["ssh", f"{self.username}@{self.hostname}", "df"], stdout=subprocess.PIPE)
        self.data = connect.stdout.decode().split('\n')

    def get_report(self):
        """
        Обработка данных об использовании файловой системы и формирование отчета.
        :return: None.
        """
        for string in self.data:
            if "vol" in string:
                vol = string.split()[-1]
                percent = int(string.split()[-2][:-1])
                available = round((int(string.split()[-3])) / (1024 ** 3), 1)  # считаем в ТБ
                self.report.update({f'{self.hostname}:{vol}': [available, percent]})

    def run(self):
        """
        Запуск процесса получения отчета об использовании файловой системы на всех удаленных хостах.
        :return: Словарь с отчетом вида {<hostname:vol>: [available, percent]}.
        """
        # Получение и обработка данных
        for host in self.hosts:
            self.get_filesystem_usage_data(hostname=host)
            self.get_report()

        return self.report
