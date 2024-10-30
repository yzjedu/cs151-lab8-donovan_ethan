# Algorithm Document
#### PLEASE! PLEASE! PLEASE! THINK before you code...
- **Name: Main**
- **Parameters:**
- **Return:**
- **Algorithm:**
1. Introduce the purpose of the program
2. call display_list
3. Thank the user for using our program 



- **Name: num_rolls**
- **Parameters:**
- **Return:**
- **Algorithm:**
1. prompt the user how many times they would like to roll and save as rolls
2. while the user's input is not a digit 
   3. prompt user how many times they would like to roll
3. typecast as an int and return rolls


- **Name: dice_roll**
- **Parameters:**
- **Return: rolls_sum**
- **Algorithm: **
1. use the random module to generate a number between 1 and 6 and save as
the variable num1
2. use the random module to generate a number between 1 and 6 and save as
the variable num2
3. add num1 and num2 and set to sum
2. return rolls_sum


- **Name: match_count**
- **Parameters: num_rolls, dice_roll**
- **Return:**
- **Algorithm:**
1. count is set to 0
2. create the list: rolls_list = [0,0,0,0,0,0,0,0,0,0,0,0]
3. while count is less than or equal to num_rolls
   1. call dice_roll and store it as the variable sum
   2. dice_roll [sum - 2] += 1
   3. count += 1
4. return rolls_list


- **Name: display_result**
- **Parameters:**
- **Return:**
- **Algorithm:**
1. call match_count and set it to list
2. index = 0
3. number = 2
4. print 'Rolling 100 pairs of dice'
5. print the list
6. while index < 13
   1. print:'Sum of 0',number, ' ', list[index] * '*'
   2. index += 1
   3. number += 1
