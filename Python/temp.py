import numpy as np
import scipy.integrate as si	#numpy求定积分用

def f(x):
    y = 1/np.sqrt(2*np.pi)*np.exp(-0.5*x**2)
    return y

#3. numpy直接求定积分的API
#利用quad求定积分，给出函数f,积分下限和积分上限[a,b]，返回值为(积分值,最大误差)
area1 = si.quad(f,-1,1)[0]
area2 = si.quad(f,-2,2)[0]
area3 = si.quad(f,-3,3)[0]
print('1 sigma 的积分 ',area1)
print('2 sigma 的积分 ',area2)
print('3 sigma 的积分 ',area3)
