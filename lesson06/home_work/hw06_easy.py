# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


import math
#Общий класс
class figure:
    def __init__(self):
        pass
    def storona(self,t1,t2):
        return math.sqrt((int(t1[0])- int(t2[0]))**2 + (int(t1[1]) - int(t2[1]))**2)
#Класс треугольник
class treugolnik(figure):
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
        self.AB = self.storona(self.A, self.B)
        self.BC = self.storona(self.B, self.C)
        self.AC = self.storona(self.A, self.C)
    @property
    def Ploschad(self):
        semip = (self.AB + self.BC + self.AC) / 2
        S = math.sqrt(semip * (semip - self.AB) * (semip - self.BC) * (semip - self.AC))
        return S
        
    @property
    def Perimetr(self):
        return self.AB + self.BC + self.AC
    
    def Visota(self, osnovanie):
        return self.Ploschad * 2 / osnovanie

tr1 = treugolnik((1,1),(1,4),(5,1))
print('Строна AB:', str(tr1.AB))
print('Строна BC:', str(tr1.BC))
print('Строна AC:', str(tr1.AC))
print('Площадь треугольника: ', str(tr1.Ploschad))
print('Периметр треугольника: ', str(tr1.Perimetr))
print('Высота по основанию : ', str(tr1.Visota(tr1.BC)))
print('\n')

#Класс трапеция
class trapecia(figure):
    def __init__(self,A,B,C,D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.AB = self.storona(self.A,self.B)
        self.BC = self.storona(self.B,self.C)
        self.CD = self.storona(self.C,self.D)
        self.AD = self.storona(self.A,self.D)
    @property
    def isravnob(self):
        if self.storona(self.A,self.C) == self.storona(self.B,self.D):
            return True
        else:
            return False
    @property
    def Ploschad(self):
        if self.isravnob:
            S = ((self.BC + self.AD) / 2) * math.sqrt(self.AB **2 - ((self.BC - self.AD) **2) / 4 )
            return S
        else:
            print('Трапеция не равнобедренная')
            return 0
    
    @property
    def Perimetr(self):
        return self.AB + self.BC + self.CD + self.AD
    
trap1 = trapecia((1,1),(2,4),(5,4),(6,1))
if trap1.isravnob:
    print('Трапеция равнобедренная')
else:
    print('Трапеция НЕ равнобедренная')
print('Периметр трапеции: ', str(trap1.Perimetr))    
print('Площадь трапеции: ', str(trap1.Ploschad))
