# -*- coding: utf-8 -*-
import os
import time

from scripts.filesystem_usage_report import FileSystemUsageReport
from config.hosts import USER, HOSTS
from config.email_server import SMTP_SERVER, FROM, TO
from scripts.hist_drawer import hist_drawer
from scripts.send_email import send_email_with_images

# Пути для временного хранения png файлов для гистограмм
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_USAGE_PNG = os.path.join(BASE_DIR, 'tmp/usage.png')
PATH_AVAILABLE_PNG = os.path.join(BASE_DIR, 'tmp/available.png')

if __name__ == '__main__':

    # Создание списков для осей графиков
    host_axis, usage_axis, available_axis = [], [], []

    # Получение отчета об использовании файловой системы
    report = FileSystemUsageReport(username=USER, hosts=HOSTS).run()

    # Итерация по отчету и заполнение списков для графиков
    for host, usage_values in report.items():
        host_axis.append(host)
        usage_axis.append(usage_values[1])
        available_axis.append(usage_values[0])

    # Создание и сохранение гистограммы для использования файловой системы
    hist_percent = hist_drawer(title='File System Used Capacity',
                               x_axis=usage_axis, y_axis=host_axis, x_label='%', name=PATH_USAGE_PNG)

    # Создание и сохранение гистограммы для свободного пространства файловой системы
    hist_available = hist_drawer(title='File System Free Space',
                                 x_axis=available_axis, y_axis=host_axis, x_label='ТB', name=PATH_AVAILABLE_PNG)

    # Формирование содержимого письма
    report_mail = f"<h1>File System Usage</h1>\n" \
                  f"Отчет об использовании файловых систем на {time.strftime('%d.%m.%Y')} " \
                  f"в виде гистограмм во вложении"

    # Отправка письма с вложенными изображениями
    send_email_with_images(server=SMTP_SERVER, sender=FROM, recipient=TO, subject='File System Usage (ex. VOM)',
                           text=report_mail, image_paths=[PATH_USAGE_PNG, PATH_AVAILABLE_PNG])
