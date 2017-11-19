#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: huanglizhuo 
# @Date:   Sat Nov 18 16:57:23 CST 2017

'''
  _____ __      __ ___    _  _     ___    _____
 |_   _|\ \    / // __|  | || |   /   \  |_   _|
   | |   \ \/\/ /| (__   | __ |   | - |    | |
  _|_|_   \_/\_/  \___|  |_||_|   |_|_|   _|_|_
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'
WeChat in terminal       create by huanglizhuo
'''
from setuptools import setup, find_packages

setup(
    name='TWchat',
    version='0.0.6.1',
    packages=find_packages(),
    install_requires=[
        'itchat',
        'urwid',
        'Pillow',
    ],

    entry_points={
        'console_scripts': [
            'twchat= TWchat:start'
        ],
    },

    license='MIT',
    author='huanglizhuo',
    author_email='huanglizhuo1991@gmail.com',
    url='https://github.com/huanglizhuo/TWchat',
    description='A Geek style client for WeChat',
    keywords=['wechat', 'Geek', 'cli', 'terminal'],
)
