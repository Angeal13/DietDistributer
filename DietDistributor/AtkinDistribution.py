class AtkinDistribution():
    def __init__(self,min_cal,max_cal,min_weight,max_weight):
        self.min_cal=min_cal
        self.max_cal=max_cal
        self.min_weight=min_weight
        self.max_weight=max_weight
    
    def carb(self):
        self.min_carbs=20*self.min_cal/100
        self.max_carbs=20*self.max_cal/100
    
    def prot(self):
        self.min_protein=2.2*self.min_weight*4
        self.max_protein=2.2*self.max_weight*4

    def fat(self):
        self.min_fat=self.min_cal-(self.min_carbs + self.min_protein)
        self.max_fat=self.max_cal-(self.max_carbs + self.max_protein)

    def information(self):

      choice=input('How you want your ditribution?(c/cals or g/grams): ')

      if choice=='c':
        self.info={
            'Carbs':str(int(self.min_carbs))+'-'+str(int(self.max_carbs))+' Cal',
            'Protein':str(int(self.min_protein))+'-'+str(int(self.max_protein))+' Cal',
            'Fat':str(int(self.min_fat))+'-'+str(int(self.max_fat))+ ' Cal'
        }    
        print(self.info)
      if choice=='g':
          self.info={
            'Carbs':str(int(int(self.min_carbs)/4))+'-'+str(int(int(self.max_carbs)/4))+' g',
            'Protein':str(int(int(self.min_protein)/4)) +'-'+str(int(int(self.max_protein)/4))+' g',
            'Fat':str(int(int(self.min_fat)/9))+'-'+str(int(int(self.max_fat)/9))+' g'
        }    
          print(self.info)