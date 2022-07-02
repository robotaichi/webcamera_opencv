##!/usr/bin/env python
# -*- coding: utf-8 -*-
# 上記2行は必須構文のため、コメント文だと思って削除しないこと
# Python2.7用プログラム

import sys
# cv2の読み込みエラー防止
#sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2
import os

username = "ubuntu"
sys.path.remove('/home/{}/.local/lib/python2.7/site-packages'.format(username))
save_path = os.path.join('/home/{}/Programs'.format(username), "image1.png")
cap = cv2.VideoCapture(0)
print("cap.isOpened:{}".format(cap.isOpened()))

while True:
    ret, img = cap.read()
    if not ret:
        print('キャプチャーに失敗しました')
        break 

    cv2.namedWindow("exit and save to push Q key")
    cv2.imshow("exit and save to push Q key", img)

    # Qキーを押したら終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite(save_path ,img)
        print('{}として保存しました'.format(save_path))
        break

cap.release()
cv2.destroyAllWindows()