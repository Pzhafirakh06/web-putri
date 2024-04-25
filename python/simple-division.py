try:     

          num1 = float (input('Enter Number 1:'))
          num2 =float (input('Enter Number 2:'))

          if num2 == 0:
                    raise ZeroDivisionError('Number  2 Cannot 0')
          hasil =num1/num2
          print(hasil)
except ZeroDivisionError as e:
          print(e)
except ValeError:
          print("Hanya bisa input angka")