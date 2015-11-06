# -*- coding:utf-8 -*-
'''
solution's code for aliyun's 11`11 so-called "the most difficult red-packet to get ever ".
author: Future@nku
'''


def first_puzzle():
    sentence1 = '''of zit kggd zitkt qkt ygxk ortfzoeqs wqlatzwqssl qfr zvg
 ortfzoeqs yggzwqssl.fgv oy ngx vqfz zg hxz zitd of gft soft.piv dgfn lgsxz
ogfl qkt zitkt?zohl:hstqlt eiqfut zif ygkd gy zit fxdwtk ngx utz.zit hkgu
kqddtkl!'''
    alphas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    keybord = 'qwertyuiopasdfghjklzxcvbnm'
    result = sentence1
    for i in range(0, len(alphas)):
        result = result.replace(keybord[i], alphas[i])
    print "first puzzle:\n", result


def second_puzzle():
    print "second puzzle:\n", 2*3*4*5*6/(4*3*2 * 2*1)
    return 2*3*4*5*6/(4*3*2 * 2*1)


def third_puzzle():
    result = bin(second_puzzle())[2:]
    print "third puzzle:\n", result


if __name__ == '__main__':
    first_puzzle()
#    second_puzzle()
    third_puzzle()
