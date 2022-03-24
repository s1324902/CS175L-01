#Average From Input
#Ryan Basile
#CS-175

def main():
    number_file = open('numbers.txt','r')
    average=0
    total=0
    count=0

    for n in number_file:
        num=float(n)
        total = total + num
        count = count + 1
        print('I read in', count, 'number(s) Current number is:', float(num), \
              'total is:', total)
        average = total / count
        print('Average:',average)
    number_file.close()

if __name__ == '__main__':
              main()
