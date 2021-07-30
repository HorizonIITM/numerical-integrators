import numpy as np
class integrators:
    def __init__(self,scheme):
        self.scheme = scheme
    def integrate(self, step, incon, endval, func, order):
        y = incon[1]
        x = incon[0]
        k = (endval-incon[0])/step
        k = int((k+1)//1)
        p = []
        if self.scheme == "euler":
#             for i in range(k):
            y = self.euler(func,step,incon,order,endval)
#                 incon[0] = incon[0] + h
#                 p[i] = y
           
        elif self.scheme == "heun":
         
            y = self.heun(func,step,incon,order)
                
                
        elif self.scheme == "rungekutta":
            
            y = self.rungekutta(func,step,incon,order)
               
                
        elif self.scheme == "beuler" and order == 1:
            
            y = self.beuler(func,step,incon,order)
                
                
        elif self.scheme == "midpoint" and order == 1:
            y = midpoint(func, incon, order, step, endval)
        
        return y
           
    def euler(self,fun, h, incon, order, endval):
        y = incon[1]
        x = incon[0]
        k = (endval-incon[0])/h
        k = int((k+1)//1)
        p = []
        for i in range(k):
            temp = incon[order] + h*(fun(incon))
            a = np.arange(1,order,1)
            temp1 = incon
            for i in a:
                temp1[order-i] = incon[order-i] + h*(incon[order-i+1])
            incon = temp1
            incon[order] = temp
            incon[0] = incon[0] + h
            p.append(incon[1])
        return p
    def heun (self,fun, h, incon, order,endval):
        y = incon[1]
        x = incon[0]
        k = (endval-incon[0])/step
        k = int((k+1)//1)
        p = []
        for i in range(k):
            temp4 = incon
            temp3 = incon[order]
            temp1 = incon[order] + h*(fun(incon))
            incon[order] = temp1
            temp2 = incon[0]
            incon[0] = incon[0] + h
            incon[0] = temp2
            a = np.arange(1,order,1)
            for i in a :
                temp4[order-i] = incon[order-i] + h*(incon[order-i+1])
            incon = temp4
            incon[order] = temp3 + (temp1-temp3)/2 + h*(fun(incon))/2
            p.append(incon[1])
        return p
    def rungekutta (self,fun, h, incon, order):
        y = incon[1]
        x = incon[0]
        k = (endval-incon[0])/h
        k = int((k+1)//1)
        p = []
        for i in range(k):
            k1 = fun(incon)
            temp = incon
            b = incon[0]
            c = incon[order]
            incon[0] = incon[0] + h/2
            incon[order] = incon[order] + h*(k1)/2
            k2 = fun(incon)
            incon[order] = temp[order] + h*(k2)/2
            k3 = fun(incon)
            incon[0] = incon[0] + h/2
            incon[order] = temp[order] + h*(k3)
            k4 =fun(incon)
            incon = temp
            a = np.arange(1,order,1)
            for i in a :
                temp[order-i] = incon[order-i] + h*(incon[order-i+1])
            incon = temp
            incon[order] = c + h*(k1 + (2*(k2 + k3)) + k4)/6
            p.append(incon[1])
        return p
    def beuler(self,fun, incon, h, order):
        y = incon[1]
        x = incon[0]
        k = (endval-incon[0])/h
        k = int((k+1)//1)
        p = []
        for i in range(p)
            h = -h
    
            incon[1] = incon[1] - h*(fun(incon))
            p.append(incon[1])
        return p
    def midpoint(self,fun, incon, order, h, endval):
        l = (endval-incon[0])/h
        y = np.zeros(l)
        y[0]=incon[1]
        for n in range(1, l-1):
            y[n+1] = y[n-1] + (f(y[n],t[n])*(t[n+1]-t[n-1])*2)
        h = y
        for n in range(l-1):
            h[n]=(y[n+1]+y[n-1])/2
        return h
t = np.linspace(0,2,100000)
# def f(n):
#     x = n[0]
#     y = n[1]
#     return y
# h = integrators("euler")
# c = [0,1]
# gen = h.integrate(0.001,[0,1],2,f,1)
# print(gen)