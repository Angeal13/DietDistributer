from Calories import Calories
from CleanBulking import CleanBulking
from AtkinDistribution import AtkinDistribution
from ketodiet import ketoDistribution
from DirtyBulking import DirtyBulking
from RegularBulking import RegularBulking
from MacroCount import MacroCount

if __name__ == '__main__':
    height=int(input('You height is : '))
    age=int(input('Curreent Age is : '))

    person=Calories(height,age)
    person.healthy_weight()
    person.BMR()
    person.cals()
    info=person.information()
    min_cals=person.get_min_cal()
    max_cals=person.get_max_cal()
    min_weight=person.get_min_weight()
    max_weight=person.get_max_weight()
    
    choice=input('Choose c/to Cutting or b/ to Bulk ')
    if choice.lower()=='c':
        min_cals=0.8*min_cals
        max_cals=0.8*max_cals

        diet=input('Choose a Diet : K/Keto,A/Atkin or M/Macrocount ')
        
        if diet.upper()=='K':
            meal=ketoDistribution(min_cals,max_cals,min_weight,max_weight)
            meal.carb()
            meal.prot()
            meal.fat()
            info=meal.information()
            print(info)

        if diet.upper()=='A':
            meal=AtkinDistribution(min_cals,max_cals,min_weight,max_weight)
            meal.carb()
            meal.prot()
            meal.fat()
            info=meal.information()
            print(info)

        if diet.upper()=='M':
            meal=MacroCount(min_cals,max_cals,min_weight,max_weight)
            meal.carb()
            meal.prot()
            meal.fat()
            info=meal.information()
            print(info)
    
    if choice.lower()=='b':
        diet=input('What type of Bulking (D/Dirty,R/Regular or C/Clean): ')

        if diet.upper()=='D':
            meal=DirtyBulking(min_cals,max_cals,min_weight,max_weight)
            meal.calories()
            meal.prot()
            meal.carb()
            meal.fat()
            info=meal.information()
            print(info)

        if diet.upper()=='R':
            meal=RegularBulking(min_cals,max_cals,min_weight,max_weight)
            meal.calories()
            meal.prot()
            meal.carb()
            meal.fat()
            info=meal.information()
            print(info)

        if diet.upper()=='C':
            meal=CleanBulking(min_cals,max_cals,min_weight,max_weight)
            meal.calories()
            meal.prot()
            meal.carb()
            meal.fat()
            info=meal.information()
            print(info)

                    
        

