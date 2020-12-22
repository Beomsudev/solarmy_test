from PIL import Image
import sys
import numpy as np
import logging as log
import matplotlib.pyplot as plt
from clt import CentralLimitTheorem as clt

log.basicConfig(stream=sys.stdout, level=log.INFO, format="%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s] %(message)s")

image = Image.open('./data/python/lena_gray.gif')
saved_path = './saved_data/'

arrVal2D = np.array(image)
arrVal1D = arrVal2D.flatten()

log.info("===== 문제 1 =====")
log.info(f"모집단 크  기 : {arrVal1D.size}")
log.info(f"모집단 평  균 : {round(np.mean(arrVal1D), 2)}")
log.info(f"모집단 분  산 : {round(np.var(arrVal1D), 2)}")
log.info(f"모집단 최대값 : {np.max(arrVal1D)}")
log.info(f"모집단 최소값 : {np.min(arrVal1D)}")
log.info(f"모집단 중앙값 : {np.median(arrVal1D)}")

log.info("===== 문제 2 =====")
plt.hist(arrVal1D)
plt.plot()
plt.savefig(saved_path + '문제2.png')

log.info("===== 문제 3 =====")
binList = [10, 100, 1000]

for i in binList:
    plt.figure()
    plt.hist(arrVal1D, bins=i)
    plt.title(f'Bin List : {i}')
    plt.savefig(saved_path + f'문제3-구간수{i}.png')

log.info("===== 문제 4 =====")
calClt = clt(arrVal1D)
sampleList = [5, 10, 20, 30, 50, 100]
for sample in sampleList:
    calClt.run_sample(N=sample, plot=True, num_bins=None)
    