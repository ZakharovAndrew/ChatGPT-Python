x = ['-'] * 9



def print_field(x):

   print(x[0] + '|' + x[1] + '|' + x[2])

   print(x[3] + '|' + x[4] + '|' + x[5])

   print(x[6] + '|' + x[7] + '|' + x[8])



def check_rows_columns(x, who):

   if (x[0] == x[1] == x[2] == who) or (x[3] == x[4] == x[5] == who) or (x[6] == x[7] == x[8] == who) or (x[0] == x[3] == x[6] == who) or (x[1] == x[4] == x[7] == who) or (x[2] == x[5] == x[8] == who):
      return True
   else:
      return False



def check_diagonals(x, who):

   if x[0] == x[4] == x[8] == who or x[2] == x[4] == x[6] == who:

      return True

   else:

      return False



def check_draw(x):

   if '-' not in x:

      return True

   else:

      return False



def start_game():

   print("Let's Play X-O")

   print_field(x)

   for i in range(9):

      if i % 2 == 0:

         who = 'x'

      else:

         who = 'o'

      inp = int(input("Enter position "+who+": "))

      x[inp-1] = who

      print_field(x)

      if check_rows_columns(x, who) or check_diagonals(x, who) == True:

         print(who + " win!")

         break



      if check_draw(x) == True:

         print("Draw!")

         break

      

start_game()