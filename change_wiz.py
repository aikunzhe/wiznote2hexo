#coding=utf-8

import os
import time
import hashlib
import random
import codecs
from bs4 import BeautifulSoup

def process_html_file(file_path):
    # ��ȡ�ļ�����������չ����
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # ��ȡ��ǰʱ��
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # �����ļ����ݵĹ�ϣֵ
    content_hash = str(int(hashlib.sha256(str(int(time.time() * 1000)).encode('utf-8')).hexdigest()[:8], 16))

    # ����Markdownͷ��
    md_header = f"""---
title: {file_name}
date: {current_time}
categories:
abbrlink: {content_hash}
---\n"""

    # ��ȡ�ļ�����
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        html_content = file.read()

    # ʹ�� BeautifulSoup ���� HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # �ҵ����еı����ǩ��h1��h6��
    heading_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # ����ÿ�������ǩ
    for heading_tag in heading_tags:
        # �����ǩû�� id ���ԣ���� id ����
        if not heading_tag.get('id'):
            # ����һ��Ψһ�ı�ʶ������ϵ�ǰʱ������������
            unique_id = int(time.time() * 1000) + random.randint(10000, 99999)
            heading_tag['id'] = f'wiz-toc-{unique_id}'  # �滻 random_number Ϊʵ�ʵ������ֵ

    # �ҵ����е� img ��ǩ
    img_tags = soup.find_all('img')

    # ����ÿ�� img ��ǩ
    for img_tag in img_tags:
        src = img_tag['src']  # ��ȡ img ��ǩ�� src ����
        title = img_tag.get('title', '')  # ��ȡ img ��ǩ�� title ���ԣ����û����Ϊ���ַ���

        # ȥ�� src �����е� '/' ǰ׺
        src = src.split('/')[-1]

        # ��ȡMarkdown��ʽ���ַ���
        markdown_img = f"\n\n![{title if title else src}]({src})\n"

        # �� Markdown ��ʽ���ԭʼ�� img ��ǩ
        new_tag = soup.new_tag('p')
        new_tag.string = markdown_img
        img_tag.replace_with(new_tag)

    # ��ȡ�滻��� Markdown ����
    new_md_content = str(soup)

    # �� Markdown ͷ��������д���ļ�
    output_path = os.path.join(os.path.dirname(file_path), f"{file_name}.md")
    with codecs.open(output_path, 'w', encoding='utf-8-sig') as file:
        file.write(md_header + new_md_content)

    # ��ȡ��Ӧ�� _files �ļ���·��
    files_folder_path = os.path.join(os.path.dirname(file_path), f"{file_name}_files")

    # ������� _files �ļ��У�����������Ϊ�ļ���
    if os.path.exists(files_folder_path):
        renamed_files_folder_path = os.path.join(os.path.dirname(file_path), file_name)
        os.rename(files_folder_path, renamed_files_folder_path)

# ʾ��ʹ��
file_path = '/mnt/d/longz/Desktop/004.htm'  # ���滻Ϊʵ�ʵ��ļ�·��
process_html_file(file_path)
