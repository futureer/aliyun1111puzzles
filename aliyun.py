# -*- coding:utf-8 -*-
'''
solution's code for aliyun's 11`11 so-called "the most difficult red-packet to get ever ".
author: Future@nku 20151106
'''


def first_puzzle():
    print 'keayrod d  looks like keyd(b)oard'


def second_puzzle():
    sentence1 = '''of zit kggd zitkt qkt ygxk ortfzoeqs wqlatzwqssl qfr zvg
 ortfzoeqs yggzwqssl.fgv oy ngx vqfz zg hxz zitd of gft soft.piv dgfn lgsxz
ogfl qkt zitkt?zohl:hstqlt eiqfut zit ygkd gy zit fxdwtk ngx utz.zit hkgu
kqddtkl!'''
    alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keybord = 'qwertyuiopasdfghjklzxcvbnm'
    result = sentence1
    for i in range(0, len(alphas)):
        result = result.replace(keybord[i], alphas[i])
    print "second puzzle:\n", result.lower()


def third_puzzle():
    result = bin(2*3*4*5*6/(4*3*2 * 2*1))[2:]
    print "third puzzle:\n", result


if __name__ == '__main__':
    first_puzzle()
    second_puzzle()
    third_puzzle()
