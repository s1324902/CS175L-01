#Ryan Basile
#CS-175L-01
#Resturant Assignment

vegetarian='False'
vegan='False'
gluten_free='False'
keep_going='yes'

while keep_going == 'yes':
    response1=(input('Is anyone in your party a vegetarian?'))
    if response1=='yes' or response1=='no':
        vegetarian=True
    response2=(input('Is anyone in your party a vegan?'))
    if response2=='yes' or response2=='no':
        vegan=True
    response3=(input('Is anyone in your party gluten free?'))
    if response3=='yes' or response3=='no':
        gluten_free=True
    (print('Here are your resturant choices.'))

    if response2=='yes':
        if response3=='yes' or response3=='no':
            print('Corner Cafe\n'+\
                  "The Chef's Kitchen\n")
    else:
        if response3=='yes':
            print('Main Street Pizza Company\n'+\
                  'Corner Cafe\n'+\
                  "The Chef's Kitchen\n")
        else:
            print("Joe's Gourmet Burgers\n"+\
                  'Main Street Pizza Company/n'+\
                  'Corner Cafe\n'+\
                  "Mama's Fine Italian\n"+\
                  "The Chef's Kitchen\n")
            keep_going=input('Would you like to do another resturant search?(Enter y for yes)')
     
                


          
      
