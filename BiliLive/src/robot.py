#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 下午 06:07
# @Author  : kamino

import os
from .config import Config
from .study import StudyExt
from .file import File
from .timer import Timer


class Robot(object):

    @staticmethod
    def text_msg(user_id, user_name, content):
        """处理文本消息"""
        # content = content.greplace('~喵', '')  # 愚人节
        File.add(Config.config('root-path') + 'BiliLive/save/danmu.log',
                 f'[{Timer.stamp2str(Timer.timestamp())}] {user_id}({user_name}): {content}\n')
        if user_name == Config.config('auth')['name']:
            return None
        if StudyExt.IsSign(content):
            rank = StudyExt.SignAdd(user_id, user_name)
            if rank != None:
                return rank
            return '打卡失败，不知道为啥'
        if content == 'sudo reboot':
            print("SUDO RESTART")
            os.system("ps -ef | grep run.py | grep -v grep | awk '{print $2}' | xargs --no-run-if-empty kill")

        return RobotReply.reply(user_id, user_name, content)

    @staticmethod
    def gift_msg(user_name, gift_name, gift_num):
        """处理礼物消息"""
        File.add(Config.config('root-path') + 'BiliLive/save/gift.log',
                 f'[{Timer.stamp2str(Timer.timestamp())}] {user_name}: {gift_name}x{gift_num}\n')
        if user_name == Config.config('auth')['username']:
            return None
        return f'感谢{user_name}的{gift_name}'


class RobotReply(object):

    @staticmethod
    def reply(user_id, user_name, content):
        """处理消息"""
        return content
