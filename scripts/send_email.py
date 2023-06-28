# -*- coding: utf-8 -*-
import os
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_with_images(server, subject, sender, recipient, text, image_paths):
    """
    Отправляет электронное письмо с вложенными изображениями.
    :param server: SMTP-сервер для отправки письма.
    :param subject: Тема письма.
    :param sender: Адрес отправителя.
    :param recipient: Адрес получателя.
    :param text: Текст письма (в формате HTML).
    :param image_paths: Список путей к изображениям для вложения.
    :return: None.
    """

    # Создание MIMEMultipart объекта
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    # Прикрепление текста в виде HTML
    msg.attach(MIMEText(text, 'html'))

    # Прикрепление изображений
    for image_path in image_paths:
        with open(image_path, 'rb') as f:
            img_data = f.read()
        img = MIMEImage(img_data)
        img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
        msg.attach(img)

    # Отправка письма
    with smtplib.SMTP(server) as server:
        server.sendmail(sender, recipient, msg.as_string())
