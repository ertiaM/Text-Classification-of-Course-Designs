# coding=utf-8
import requests
from bs4 import BeautifulSoup
import json
import re, os

from fontTools.afmLib import writelines

from spider import *


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


def get_lyric(song_id):
    url = 'http://music.163.com/api/song/lyric?' + 'id=' + str(song_id) + '&lv=1&kv=1&tv=-1'
    html = get_html(url)
    json_obj = json.loads(html)
    print(json_obj)
    lyric = json_obj['lrc']['lyric']
    return lyric


def get_details(song_id):
    url = 'http://music.163.com/api/song/detail/?' + 'id=' + str(song_id) + '&ids=%5B' + str(song_id) + '%5D'
    html = get_html(url)
    print(html)
    json_obj = json.loads(html)
    song_name = json_obj['songs'][0]['name']
    song_artist = json_obj['songs'][0]['artists'][0]['name']
    return song_name, song_artist


def output_file(song_id):
    song_name, song_artist = get_details(song_id)
    lyric = get_lyric(song_id)
    file_name = song_name + ' - ' + song_artist + '.txt'
    file_name = file_name.replace('/', '／')
    file_name = file_name.replace('?', '')
    file_name = file_name.replace('*', '')
    file_name = file_name.replace('（', '')
    file_name = file_name.replace('）', '')
    file_name = file_name.replace('"', '')
    file_name = file_name.replace('\t', '')
    file_name = file_name.replace('>', '')
    file_name = file_name.replace('<', '')
    file_name = file_name.replace('\\', '')

    singer = 'ZAYN'
    file_name = "../"+singer+"/"+file_name
    file = open(file_name, "w+", encoding="utf-8")
    file.writelines(lyric)
    file.close()


url = "https://music.163.com/album?id=121556815"
id_list = get_songlist(url)
print(id_list)

for iterm in id_list:
    output_file(iterm)
