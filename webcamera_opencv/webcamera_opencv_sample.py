##!/usr/bin/env python
# -*- coding: utf-8 -*-
# 上記2行は必須構文のため、コメント文だと思って削除しないこと
# Python2.7用プログラム

import sys
# cv2の読み込みエラー防止
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
sys.path.remove('/home/limlab/.local/lib/python2.7/site-packages')
import cv2
#print(cv2.getBuildInformation())

# DEVICE_ID = 0
# cap = cv2.VideoCapture(DEVICE_ID)
# cap = cv2.VideoCapture(0 + cv2.CAP_V4L)
# cap = cv2.VideoCapture('/home/limlab/ビデオ/src_hirano.mp4')
cap = cv2.VideoCapture(0)
print(cap.isOpened())
# cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    if not ret:
        print('キャプチャーに失敗しました')
        break 

    cv2.imshow('frame', frame)

    # q キーを押したら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()