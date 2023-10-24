# -*- coding:utf-8 -*-
"""
voc格式xml转化为yolo中的txt
"""
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import copy
from lxml.etree import Element, SubElement, tostring, ElementTree

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ['Text', 'Figure', 'Table', 'Equation']  # 类别


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('C:\\Users\\19425\\Desktop\\1\\image\\%s.xml' % image_id, encoding='UTF-8')  # windows系统记得用双斜线， 这个是表示要转变的标签存放路径 xml

    out_file = open('C:\\Users\\19425\\Desktop\\2\\txt\\%s.txt' % image_id, 'w')  # 生成txt格式文件，存放的位置路径
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        # print(cls)
        if cls not in classes:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


with open('../label.txt', encoding='UTF-8') as f:  # 要处理的label名称文档，使用 ls label/ > label.txt 生成即可
    for ln in f:
        label_name = ln.rstrip('\n').split('.')[0]  # 只需要文件名，不要后缀
        print(label_name)
        convert_annotation(label_name)
#
# if __name__ == "__main__":  # ================================================================================================
#     classes1 = ['Text', 'Figure', 'Table', 'Equation']
#     # 2、voc格式的xml标签文件路径
#     GT_files1 = r'C:/Users/19425/Desktop/1/image/'
#     # 3、转化为yolo格式的txt标签文件存储路径
#     save_txt_files1 = r'C:/Users/19425/Desktop/2/xml'
#
#     convert_annotation(GT_files1, save_txt_files1, classes1)
