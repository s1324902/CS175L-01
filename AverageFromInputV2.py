#Average From Input with execption handeling
#Ryan Basile
#CS-175

def main():
    try:
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
    except IOError:
        print('Error: The file could not be found.')
    except ValueError:
        print('Error: There is a detected non-valid number.')

if __name__ == '__main__':
              main()
