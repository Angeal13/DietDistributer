class Calories():
    def __init__(self,height,age):
        self.height=height
        self.age=age

    def healthy_weight(self):
        self.max_new_weight=25*(self.height**2)/10000
        self.min_new_weight=19*(self.height**2)/10000
    
    def BMR(self):
        self.gender=input('Enter Gender m/f: ')
        if  self.gender=='m':
            self.max_bmr=(10*self.max_new_weight)+6.25*self.height-5*self.age+5
            self.min_bmr=(10*self.min_new_weight)+6.25*self.height-5*self.age+5
        elif  self.gender=='f':
            self.max_bmr=(10*self.max_new_weight)+(6.25*self.height)-5*self.age-161
            self.min_bmr=(10*self.min_new_weight)+6.25*self.height-5*self.age-161
        else: print('Enter a Gender')
    
    def cals(self):
        
        self.activityLevel=int(input('Enetr activity level(0=sedentary,1=light,2=moderate,3=high): '))
        if self.activityLevel==0:
            self.max_cal=1.2*self.max_bmr
            self.min_cal=1.2*self.min_bmr
        if self.activityLevel==1:
            self.max_cal=1.375*self.max_bmr
            self.min_cal=1.375*self.min_bmr
        if self.activityLevel==2:
            self.max_cal=1.55*self.max_bmr
            self.min_cal=1.55*self.min_bmr 
        if self.activityLevel==3:
            self.max_cal=1.725*self.max_bmr
            self.min_cal=1.725*self.min_bmr
    
    def get_min_cal(self):
      return self.min_cal
   
    def get_max_cal(self):
      return self.max_cal

    def get_min_weight(self):
        return self.min_new_weight

    def get_max_weight(self):
        return self.max_new_weight
        
    def information(self):
        info={
            'Height':self.height,
            'age':self.age,
            'Weight':str(self.min_new_weight) +'-' + str(self.max_new_weight)+' kg',
            #'Activity Level':self.activtyLevel,
            'Calories':str(self.min_cal)+'-'+str(self.max_cal)+' cals/day'
            }
        print(info)
