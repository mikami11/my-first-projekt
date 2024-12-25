あきざせき////////////////////////////////
import math
class Seki:
    def __init__(self,yzahyo,xzahyo,book):
        self.distance = None
        self.book = book #yoyaku 0 yoyakunashi 1
        self.xzahyo = xzahyo
        self.yzahyo = yzahyo
    
class Zaseki:#座席表のクラス

    def __init__(self,H,W,P,Q):
        self.no2list = []
        self.zaseki = []
        self.H = H
        self.W = W
        self.P = P 
        self.Q = Q
        for h in range(H):
            row = [Seki(h, w, 1) for w in range(W)]
            self.zaseki.append(row)
        
    def add_seki(self,seki):
        
        self.zaseki[seki.yzahyo][seki.xzahyo] = seki
    
    def take_distance(self,seki):
        
        seki.distance = abs(seki.xzahyo - self.Q) + abs(seki.yzahyo - self.P)
    
    def took_no2(self):
        
        min_dis = self.H + self.W
        for row in self.zaseki:
            for seki in row:
                if seki.book == 1:  # 予約がない席のみ
                    self.take_distance(seki)
                    if seki.distance < min_dis:
                        min_dis = seki.distance

        for row in self.zaseki:
            for seki in row:
                if seki.distance == min_dis:
                    self.no2list.append(seki)
                
                

input_line = input().split()

bookNo = int(input_line[0])
zasekiy = int(input_line[1])
zasekix = int(input_line[2])
sekino1y= int(input_line[3])
sekino1x = int(input_line[4])

Zaseki = Zaseki(zasekiy,zasekix,sekino1y,sekino1x)

for bookno in range(bookNo):
    book_seki = input().split()
    booky = int(book_seki[0])
    bookx = int(book_seki[1])
    
    Zaseki.zaseki[booky][bookx].book = 0

Zaseki.took_no2()

for seki in Zaseki.no2list:
    print(seki.yzahyo ,seki.xzahyo)
////////////////////////////////////
