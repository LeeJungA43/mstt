#-*- coding: utf-8 -*-
import os

specific_folder = 'E:/multi-speaker-tacotron-tensorflow/datasets/son/assets/' #c:\ ��������()�� �ƴ� ������(/)
file_list = os.listdir(specific_folder) #os.listdir(���� ������)
cnt = 0
#���� �̸� �ϳ��� ���
for file in file_list :
    if len(file) == 14:
        cnt = cnt+1
    abp = specific_folder+file
    f = open(abp)
    linenum = f.readlines()
    if len(linenum) == 1:
        print(file)
    print(cnt)