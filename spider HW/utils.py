# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:24:15 2021

@author: Jinye He
"""

import requests
from bs4 import BeautifulSoup 



def ask_url(url):
    #this function is used to get the page infomation 
    head = {}
    head["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
    head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36" 
    #set head
    response = requests.get(url,headers = head)
    
    return(response)


def find_newbook(num):
    #this function is used to get the homepage of a book
    response = ask_url('https://book.douban.com/')
    bs = BeautifulSoup(response.text,'lxml')
    page_newbook = 'https://book.douban.com' + bs.select('div[class="section books-express"] > div > h2 > span a')[0].get('href')
    #get the page of new book list
    response = ask_url(page_newbook)
    bs = BeautifulSoup(response.text,'lxml')
    page_book = bs.select('li a[class="cover"]')[num].get('href')
    #get the book's homepage
    return page_book

def find_popularbook(num):
    #this function is used to get the homepage of a book
    response = ask_url('https://book.douban.com/')
    bs = BeautifulSoup(response.text,'lxml')
    if num in range(10):
        page_popularbook = 'https://book.douban.com' + bs.select('div[class="section popular-books"] > div > h2 > span a')[0].get('href')
        #get the page of popular fiction list
        response = ask_url(page_popularbook)
        bs = BeautifulSoup(response.text,'lxml')
        if num !=9:
            page_book = bs.select('li[class="media clearfix"]  h2 > a')[num].get('href')
        else:
            page_book = bs.select('li[class="media clearfix last"] h2 > a')[0].get('href')
        #get the book's homepage
    else:
        page_popularbook = 'https://book.douban.com' + bs.select('div[class="section popular-books"] > div > h2 > span:nth-child(3) > a')[0].get('href')
        #get the page of popular nonfiction list
        response = ask_url(page_popularbook)
        bs = BeautifulSoup(response.text,'lxml')
        if num != 19:
            page_book = bs.select('li[class="media clearfix"]  h2 > a')[num-10].get('href')
        else:
            page_book = bs.select('li[class="media clearfix last"]  h2 > a')[0].get('href')
        #get the book's homepage
                
    return page_book

def get_info(url):
    #this function is used to get infomation from book's homepage
    response = ask_url(url)
    bs = BeautifulSoup(response.text,'lxml')
    name = bs.select('h1 > span[property="v:itemreviewed"]')[0].get_text()
    author = bs.select('div[id="info"] > span > a')[0].get_text()
    grade = bs.select('div[class="rating_self clearfix"] > strong')[0].get_text().strip()
    if grade == '' :
        grade = '暂无评分'
    introduction = bs.select('div[class="intro"]')[0].get_text().strip()
    info = [name,author,grade,introduction]
    #get infomation respectively and package them in a vector info
    return info


class book:
    #define the class of book 
    name = ''
    author = ''
    grade = ''
    introduction = ''
    def __init__(self,n,a,g,i):
        self.name = n
        self.author = a
        self.grade = g
        self.introduction = i
        
    def info(self,url):
        info = get_info(url)
        self.name = info[0]
        self.author = info[1]
        self.grade = info[2]
        self.introduction = info[3]
        

        
        
        
        

    
        
        
    
    
        
