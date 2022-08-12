#!/usr/bin/env bash
# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json
import re, os


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Referer': 'http://music.163.com',
        'Host': 'music.163.com'
    }
    try:
        response = requests.get(url, headers=headers)
        html = response.text
        return html
    except:
        print('request error')
        pass


def get_songlist(list_url):
    html = get_html(list_url)
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    # print(soup.ul)
    pattern = re.compile(r'<a href.*?</a>')
    result = pattern.findall(str(soup.ul))
    list = []
    for iterm in result:
        print(iterm)
        song_id_group = re.finditer(r"\d+", iterm)
        song_name_group = re.finditer(r">.*?</a>", iterm)
        for song_id, song_name in zip(song_id_group, song_name_group):
            # print(song_id.group())
            list.append(song_id.group())
            #    print(song_name.group()[1:-4])
    return list