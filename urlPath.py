#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'拼接动容图片、视频url'

import hashlib
class

# 获取真人视频url
def getVideoUrl(vid, uid, fileseed, domain='http://video.idongrong.com/'):
    md5 = hashlib.md5()
    md5.update((str(uid) + str(fileseed)).encode('utf-8'))
    return domain + str(vid) + '_' + md5.hexdigest() + '.mp4'

# 获取机器人视频url
def getRobotVideoUrl(vid, domain='http://video.idongrong.com/'):
    md5 = hashlib.md5()
    md5.update((str(vid) + 'videoautoman').encode('utf-8'))
    return domain + str(vid) + '_' + md5.hexdigest() + '.mp4'

# 获取图片url
def getPhotoUrl(uid, fileseed, domain='http://img.idongrong.com/head/'):
    md5 = hashlib.md5()
    md5.update((str(uid) + str(fileseed) + 'small').encode('utf-8'))
    return domain + str(uid % 100) + '/' + md5.hexdigest() + '.jpg'

def getRobotPhotoUrl(vid, domain='http://img.idongrong.com/headext/'):
    md5 = hashlib.md5()
    md5.update((str(vid) + 'smallautoman').encode('utf-8'))
    return domain + md5.hexdigest() + '.jpg'

# 读取文件获取uid、vid信息
def get_user_info(file):
    info = {}
    with open(file, 'r') as fr:
        for line in fr:
            dic = line.split()
            info[dic[0]] = dic[3]
    return info

def write_rob_url(file, info):
    with open(file, 'w', encoding='utf8') as fw:
        fw.write('精英圈机器人数量: %s\n' % len(info), )
        for k, v in info.items():
            l = []
            vids = v.split(',')
            for vid in vids:
                l.append(getRobotVideoUrl(vid))
            fw.write('%s:\n%s\n\n' % (k, '\n'.join(l)))



if __name__ == '__main__':
    # info = get_user_info('rr.txt')
    # write_rob_url('url.txt', info)
    # print(getRobotPhotoUrl(32440))
    print(getVideoUrl(188445, 90608397, 1))
    # print(getVideoUrl(30298, 90600739, 1))
    print(getPhotoUrl(50385148, 80))
