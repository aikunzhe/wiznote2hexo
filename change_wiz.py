#coding=utf-8

import os
import time
import hashlib
import random
import codecs
from bs4 import BeautifulSoup

def process_html_file(file_path):
    # 获取文件名（不含扩展名）
    file_name = os.path.splitext(os.path.basename(file_path))[0]

    # 获取当前时间
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    # 计算文件内容的哈希值
    content_hash = str(int(hashlib.sha256(str(int(time.time() * 1000)).encode('utf-8')).hexdigest()[:8], 16))

    # 构建Markdown头部
    md_header = f"""---
title: {file_name}
date: {current_time}
categories:
abbrlink: {content_hash}
---\n"""

    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        html_content = file.read()

    # 使用 BeautifulSoup 解析 HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 找到所有的标题标签（h1到h6）
    heading_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    # 遍历每个标题标签
    for heading_tag in heading_tags:
        # 如果标签没有 id 属性，添加 id 属性
        if not heading_tag.get('id'):
            # 生成一个唯一的标识符（结合当前时间戳和随机数）
            unique_id = int(time.time() * 1000) + random.randint(10000, 99999)
            heading_tag['id'] = f'wiz-toc-{unique_id}'  # 替换 random_number 为实际的随机数值

    # 找到所有的 img 标签
    img_tags = soup.find_all('img')

    # 遍历每个 img 标签
    for img_tag in img_tags:
        src = img_tag['src']  # 获取 img 标签的 src 属性
        title = img_tag.get('title', '')  # 获取 img 标签的 title 属性，如果没有则为空字符串

        # 去除 src 属性中的 '/' 前缀
        src = src.split('/')[-1]

        # 获取Markdown格式的字符串
        markdown_img = f"\n\n![{title if title else src}]({src})\n"

        # 用 Markdown 格式替代原始的 img 标签
        new_tag = soup.new_tag('p')
        new_tag.string = markdown_img
        img_tag.replace_with(new_tag)

    # 获取替换后的 Markdown 内容
    new_md_content = str(soup)

    # 将 Markdown 头部和内容写入文件
    output_path = os.path.join(os.path.dirname(file_path), f"{file_name}.md")
    with codecs.open(output_path, 'w', encoding='utf-8-sig') as file:
        file.write(md_header + new_md_content)

    # 获取对应的 _files 文件夹路径
    files_folder_path = os.path.join(os.path.dirname(file_path), f"{file_name}_files")

    # 如果存在 _files 文件夹，将其重命名为文件名
    if os.path.exists(files_folder_path):
        renamed_files_folder_path = os.path.join(os.path.dirname(file_path), file_name)
        os.rename(files_folder_path, renamed_files_folder_path)

# 示例使用
file_path = '/mnt/d/longz/Desktop/004.htm'  # 请替换为实际的文件路径
process_html_file(file_path)
