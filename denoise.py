# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 18:15:36 2022

@author: LTC
"""

import cv2
import os
import datetime
import sys

filename = sys.argv[1]
print('filename'+filename)
dirr = os.path.dirname(__file__)+'\\pic\\'
print(dirr)
src = dirr+filename
print(src)
imgType = '.'+filename.split('.',1)[1]
img = cv2.imread(src)
h,w,d = img.shape
ratio = 4
hs = [0]
ws = [0]
delta = 10
for i in range(0,ratio):
    if i<ratio-1:
        hs.append(int(h/ratio)+hs[i])
        ws.append(int(w/ratio)+ws[i])
    else:
        hs.append(h)
        ws.append(w)


count = -1
for i in range(0,ratio):
    for j in range(0,ratio):  
        img0 = 0
        if i == 0:
            if j == 0:
                img0 = img[hs[i]:hs[i+1]+delta,ws[j]:ws[j+1]+delta,:]
            elif j == ratio-1:
                img0 = img[hs[i]:hs[i+1]+delta,ws[j]-delta:ws[j+1],:]
            else:
                img0 = img[hs[i]:hs[i+1]+delta,ws[j]-delta:ws[j+1]+delta,:]
        elif i == ratio-1:
            if j == 0:
                img0 = img[hs[i]-delta:hs[i+1],ws[j]:ws[j+1]+delta,:]
            elif j == ratio-1:
                img0 = img[hs[i]-delta:hs[i+1],ws[j]-delta:ws[j+1],:]
            else:
                img0 = img[hs[i]-delta:hs[i+1],ws[j]-delta:ws[j+1]+delta,:]
        else:
            if j == 0:
                img0 = img[hs[i]-delta:hs[i+1]+delta,ws[j]:ws[j+1]+delta,:]
            elif j == ratio-1:
                img0 = img[hs[i]-delta:hs[i+1]+delta,ws[j]-delta:ws[j+1],:]
            else:
                img0 = img[hs[i]-delta:hs[i+1]+delta,ws[j]-delta:ws[j+1]+delta,:]
        cv2.imwrite(dirr +'im' + str(i)+'_'+str(j)+ imgType, img0)
        os.system('Denoiser.exe -i '+dirr +'im' + str(i)+'_'+str(j)+'.png -o '+dirr +'imm' + str(i)+'_'+str(j)+imgType)  
        os.remove(dirr +'im' + str(i)+'_'+str(j)+ imgType)

        count += 1
        p = count/ratio/ratio*100
        print('%'+str(p)+' has been finished --------------------------------------------------------------------------')

newImg = img
for i in range(0,ratio):
    for j in range(0,ratio):
        img0 = cv2.imread(dirr +'imm' + str(i)+'_'+str(j)+imgType)
        h0,w0,d0 = img0.shape  
        if i == 0:
            if j == 0:
                img0 = img0[0:h0-delta,0:w0-delta,:]
            elif j == ratio-1:
                img0 = img0[0:h0-delta,0+delta:w0,:]
            else:
                img0 = img0[0:h0-delta,0+delta:w0-delta,:]
        elif i == ratio-1:
            if j == 0:
                img0 = img0[0+delta:h0,0:w0-delta,:]
            elif j == ratio-1:
                img0 = img0[0+delta:h0,0+delta:w0,:]
            else:
                img0 = img0[0+delta:h0,0+delta:w0-delta,:]
        else:
            if j == 0:
                img0 = img0[0+delta:h0-delta,0:w0-delta,:]
            elif j == ratio-1:
                img0 = img0[0+delta:h0-delta,0+delta:w0,:]
            else:
                img0 = img0[0+delta:h0-delta,0+delta:w0-delta,:]
        newImg[hs[i]:hs[i+1],ws[j]:ws[j+1],:] = img0
        os.remove(dirr +'imm' + str(i)+'_'+str(j)+imgType)

print('%100 has been finished --------------------------------------------------------------------------')
nowTime = datetime.datetime.now()
cv2.imwrite(dirr+'result_'+filename.split('.',1)[0]+imgType, newImg)
print('success,result is '+dirr+'result_'+filename.split('.',1)[0]+imgType)

        
        
        
        
        
