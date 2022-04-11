class Logarithm:
    def __init__(self) -> None:
        self.one=1.0
        self.quater=0.25
        self.half=0.5
        self.LNOF2=
        self.LN2=
        self.exponent=
        self.LNERR1=1
        self.LOGCONSTANTS=[0,                                                 
         -.031748698314686,                                 
         -.064538521137592,                                 
         -.098440072813219,                                  
         -.13353139262472,                                 
         -.16989903679496,                                  
         -.20763936477852,                                  
         -.24686007793207,                                  
         -.28768207245230,                                 
         -.33024168687007,                                   
         -.37469344944111,                                  
         -.42121346507702,                                   
         -.47000362924518,                                  
         -.52129692363269,                                   
         -.57536414490278,                                  
         -.63252255874431, 
         0,                                                 
         .060624621816487,                                   
         .11778303565643,                                    
         .17185025692743,                                    
         .22314355131493,                                    
         .27193371548310,                                   
         .31845373111901,                                   
         .36290549369005,                                    
         .40546510810782,                                    
         .44628710262805,                                    
         .48550781578160,                                    
         .52324814376516,                                   
         .55961578793540,                                    
         .59470710774622,                                   
         .62860865942275,                                    
         .66139848224520] 
        self.EXPONSIGNTOSIGN=
        self.ALLEXPON=
    def LOGBODY(self,Z):
        Y, N, K, X=0,0,0,0
        X = Z ** 2;                                                   
        FUNCTION =X * 1.2512308563552 * pow(10,-2) + 8.3333316374678*pow(10,-2) *X * Z+Z+K+N
        Y=round(Z)
        N=
        if X >=self.one:
            X=Y
            if X<self.half:
                if Y < self.quater:
                    N=(N+36)*self.LN2
                    K=
                    Z=
                    Z = (Z+Z) / (Y+Y-Z)
                else:
                    N = (N+37) * self.LN2
                    K=
                    Z=
                    Z = (Z+Z) / (Y+Y-Z) 
            else:
                N = (N+38) * self.LN2
                K=
                Z=
                Z=Z / (-Z*self.half + Y)
        if X>0:
            if Y>self.quater:
                if Y > self.half:
                    N = (N + 39) * self.LN2
                    X=
                    






        



        
        

















def main():
    obj=Logarithm()
 
if __name__=="__main__":
    main()
