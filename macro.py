#-*- coding: utf-8 -*-
import os

specific_folder = 'E:/multi-speaker-tacotron-tensorflow/datasets/son/assets/' #c:\ 역슬래쉬()가 아닌 슬래쉬(/)
file_list = os.listdir(specific_folder) #os.listdir(지정 폴더명)
cnt = 0
#파일 이름 하나씩 출력
for file in file_list :
    if len(file) == 14:
        cnt = cnt+1
    abp = specific_folder+file
    f = open(abp)
    linenum = f.readlines(encoding='UTF8')
    if len(linenum) == 1:
        print(file)
    print(cnt)