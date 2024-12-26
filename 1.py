
# Screenshot_1
# 1. 
# a =[2,3,4,5,3,5,5,23,3,4]
# b = len (a) 
# c = []
# for i in range(b-1, -1,-1):
#     c.append(a[i])
# print(c)

# 2.
# def change(lst):
#     result = lst[:]
#     result[0], result[-1] = result[-1], result[0]
#     result
 

# 3.
# def to_list(*args):
#     b =[]
#     for a in args:
#         b.append(a)
#     return b


# 4.
# def useless (lst):
#     temp = lst [0]
#     for i in (0,len(lst)-1):
#         if temp < lst[i]:
#             temp = lst[i]
#     temp = temp / len(lst)
#     return temp


# 5.
# def lst_sort(lst):
#     for i in range(len(lst)):
#         for i in range (len(lst)-1):
#             if lst[i]>lst[i+1]:
#                 lst [i],lst[i+1]=lst[i+1],lst[i]
#     return lst


# 6. 
# def all_eq(lst):
#     maxword = max(lst,key = len)
#     for i, w in enumerate(lst):
#         if w != maxword:
#             l = len(maxword) - len(w)
#             nw = w + l*"_"
#             lst[i] = nw
#     return lst



# Screenshot_2
# 1.
# def to_float(num):
#     if isinstance(num, (int, float)):
#         return float(num)


# 2.
# def avg_5(a, b, c, d):
#     return round((a + b + c + d) / 4, 5)


# 3.
# def mul_to_int (a,b):
#     c = a * b
#     if (c//1)>=c:
#         return(int(c))
#     else:
#         return(float(c))


# 4.
# import math
# def radius (a):
#     return(((3*a)/(4*(math.pi)))**(1/3))


# Screenshot_3
# 1.
# def dislike_6(a):
#     if (type(a) is float or type(a) is int) and a == 6.0:
#         return 'Только не 6!'
#     return True


# 2.
# def help_bool(letter):
#     if letter == 'к': 
#         return "Коммутативность: A AND B = B AND A и A OR B = B OR A"
#     elif letter == 'a':  
#         return "Ассоциативность: (A AND B) AND C = A AND (B AND C) и (A OR B) OR C = A OR (B OR C)"
#     elif letter == 'д':  
#         return "Дистрибутивность: A AND (B OR C) = (A AND B) OR (A AND C) и A OR (B AND C) = (A OR B) AND (A OR C)"
#     elif letter == 'м':  
#         return "Правило де Моргана: NOT (A AND B) = NOT A OR NOT B и NOT (A OR B) = NOT A AND NOT B"
#     else:
#         return ("Неверный аргумент. Используйте:\n"
#                 "к - коммутативность\n"
#                 "a - ассоциативность\n"
#                 "д - дистрибутивность\n"
#                 "м - правило де Моргана")


# Screenshot_4
# 1. 
# a =[2,3,4,5,3,5,5,23,3,4]
# b = len (a) 
# c = []
# for i in range(b-1, -1,-1):
#     c.append(a[i])
# print(c)

# 2.
# def change(lst):
#     result = lst[:]
#     result[0], result[-1] = result[-1], result[0]
#     result
 

# 3.
# def to_list(*args):
#     b =[]
#     for a in args:
#         b.append(a)
#     return b


# 4.
# def useless (lst):
#     temp = lst [0]
#     for i in (0,len(lst)-1):
#         if temp < lst[i]:
#             temp = lst[i]
#     temp = temp / len(lst)
#     return temp


# Screenshot_5
# 1.
# def lst_sort(lst):
#     for i in range(len(lst)):
#         for i in range (len(lst)-1):
#             if lst[i]>lst[i+1]:
#                 lst [i],lst[i+1]=lst[i+1],lst[i]
#     return lst


# 2. 
# def all_eq(lst):
#     maxword = max(lst,key = len)
#     for i, w in enumerate(lst):
#         if w != maxword:
#             l = len(maxword) - len(w)
#             nw = w + l*"_"
#             lst[i] = nw
#     return lst


# Screenshot_6
# 1.
# def to_dict(lst):
#     return {element: element for element in lst}
#     printprint(to_dict([1, 2, 3, 4]))


# 2.
# def biggest_dict(*args):
#     main = {'first_one':'we can do it'}
#     temp = {}
#     for par in args:
#         vk = par.split(':',1)
#         key = vk[0]
#         value = vk[1]
#         temp[key] = value

#     main.update(temp)
#     return main

# print(biggest_dict('name:alex', 'age:30'))


# 3. 
# def count_it(sequence):
#     count_dict = {}
#     for char in sequence:
#         if char.isdigit():  
#             num = int(char)
#             if num in count_dict:
#                 count_dict[num] += 1
#             else:
#                 count_dict[num] = 1
#     sorted_counts = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)
#     result = {num: count for num, count in sorted_counts[:3]}
#     return result

4.
# colors = {'color1':'green',
#         'color2':'yellow',
#         'color3':'blue',
#         'color4':'black',
#         'color5':'red',
#         }
# def dicter(dictionary):
#     keys = list(dictionary.keys())
#     dictionary[keys[0]], dictionary[keys[-1]] = dictionary[keys[-1]], dictionary[keys[0]]
#     del dictionary[keys[1]]
#     dictionary['new key'] = 'new value'
#     return dictionary
# print (dicter(colors))


# stroki_1 
# 1.
# def search_substr(subst,st):
#     subst = subst.lower()
#     st = st.lower()
#     if subst in st:
#         return ('Есть контакт')
#     else:
#         return ('Мимо')


# 2.
# def first_last(letter,st):
#     first = None
#     last = None
#     letter_place = []
#     st = st.lower()
#     for i in range (len(st)):
#         if st[i] == letter:
#             letter_place.append(i)
#     if letter_place != []:
#         first = letter_place[0]
#         last = letter_place[-1]
#     return first,last


# 3.
# from collections import Counter

# def top3(st):
#     st = st.replace(" ", "")
#     counter = Counter(st)
#     most_common = counter.most_common(3)
#     result = ', '.join(f"{symbol} – {count}" for symbol, count in most_common) 
#     return result
    
# 4.
# def camel(st):
#     result = []
#     upper = True  
#     for char in st:
#         if char.isalpha():  
#             if upper:
#                 result.append(char.upper())
#             else:
#                 result.append(char.lower())
#             upper = not upper  
#         else:
#             result.append(char)  
#     return ''.join(result)
# print(camel("aaaaaaaaaaaaaa"))  
# print(camel("nnnnnnnnnnnnn"))  


# stroki_2
# 5.
# def shortener(st):
#     deleter = False
#     word = ''
#     for i in st:
#         if i == '(':
#             deleter = True
#         elif i == ')':
#             deleter = False
#         elif not deleter:
#             word += i

#     return word.strip()


# 6. 
# def cleaned_str (st):
#     word = ''
#     for i in st:
#         if i =='@':
#             word = word[:-1]
#         else:
#             word += i
#     return word
# print(cleaned_str('ривс@пафыпс@@@@@@рлы@@@ва'))



# Screenshot_10
# def doter (x,y):

#     if len(x) != len(y):
#         print('Неравное количество точек')
#         return
#     dots = []
#     for i in range (len(x)):
#         dots.append(f"({x[i]};{y[i]})")

#     return dots




# Screenshot_11
# def welcomer (guests):
#     for guest in guests:
#         print (f"Hello {guest}")


# guests = ['polly', 'bob', 'helga']
# welcomer(guests)



# Screenshot_12
# def doubler (st):
#     for i in range(len(st)-1):
#         if st[i] == st [i+1]:
#             return True
#     return False

# print(doubler('dfncnsddddd'))
# print(doubler('dfncnsd'))


# 13. (это 32)
# def remove_extra_spaces(s):
#     return ' '.join(s.split())
# input_str = "  я       уже   устала, сколько    там ещё        их  "
# result = remove_extra_spaces(input_str)
# print(result)  

# 14.
# import math

# def rounder(number):
#     factor = 10 ** 2
#     integer_part = int(number * factor)
#     fractional_part = number * factor - integer_part
#     if fractional_part >= 0.5:
#         integer_part += 1
#     return integer_part / factor

# def mass (radius, height):
#     size = height * ((radius**2)* math.pi)
#     mass = size * 1000
#     mass = rounder(mass)

#     return mass

# print (mass(10,10))

# 15.
# def mult (st):
#     number = ''
#     numbers = []
#     multiple = 1
#     for i in range(len(st)):
#         if st[i]!=',':
#             number += st[i]
#         elif st[i] == ' ':
#             number += 0
#         else:
#             numbers.append(int(number))
#             number = ''
#     for i in numbers:
#         multiple *= i
#     return multiple



# 16.
# def sizer (data):

#     full_size = []
#     for i in data:
#         size = 1
#         for j in i:
#             size *= j
#         full_size.append(size)
#     res = 0
#     for i in full_size:
#         res += i
#     return res

# 17.
# import math

# def rounder(number):
#     factor = 10 ** 3
#     integer_part = int(number * factor)
#     fractional_part = number * factor - integer_part
#     if fractional_part >= 0.5:
#         integer_part += 1
#     return integer_part / factor

# def pyph(dict):
#     x = dict.get('x')[0] - dict.get('x')[1]
#     y = dict.get('y')[0] - dict.get('y')[1]

#     length = math.sqrt(x**2 + y**2)

#     length = rounder(length)
#     return length

# print(pyph({'x':[0,3],
#             'y':[0,4]}))


# 18.
# def encoder (st):
#     st.lower()
#     word = ''
#     for i in st:
#         print(i)
#         if i == "е":
#             word += "3"
#         elif i == "а":
#             word += "4"
#         else:
#             word += i
#     return word

# print(encoder('я очень устала'))

# 19.
# def masser(*args):
#     res = []
#     temp = 0
#     for num in args:
#         for i in range(0, len(res)):
#             temp += res[i]
#         temp += num
#         res.append(temp)
#         temp = 0
#     return res

# print(masser(1,2,3,4,5))

# 20.
# def stonks(numbers):
#     a = numbers[0]
#     for i in range(1, len(numbers)):
#         if a > numbers[i]:
#             return 'Не возраставет'
#         else:
#             a = numbers[i]
#     return 'Возрастает'

# print(stonks([1, 2, 3, 4, 5]))
# print(stonks([1, 2, 3, 4, 5,2]))
# print(stonks([543, 2, 3, 4,]))
# print(stonks([-15,52,987656,98765434567897347]))

# 21.
# def mid (numbers):
#     if len(numbers)%2 == 0:
#         return 'Требуется нечетное количество чисел'
#     for i in range(0, len(numbers)):
#         for j in range(0, len(numbers)-1):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j],numbers[j+1] = numbers[j+1],numbers[j]


#     return numbers[len(numbers)//2]

# print(mid([5,98765,1234567895,987,15]))

# 7.
# def counter(st):
#     alphabet = 'abcdefghiklmnopqrstuvwxyz'
#     sum = 0
#     for letter in st:
#         for i in range (len(alphabet)):
#             if letter == alphabet[i]:
#                 sum += i+1
#     return sum


# print(counter('aeg'))


# 8.
# def reverser(st):
#     word = ''

#     for i in range(len(st)-1,-1,-1):
#         word += st[i]
#     st = ''
#     for letter in word:
#         if letter.isupper():
#             st += letter.lower()
#         if letter.islower():
#             st += letter.upper()
#     return st

# print(reverser('abcDEF'))


# 9.
# def del_enem(people,enemies):
#     res = []
#     for enemy in enemies:
#         for i in range (0,len(people)-1):
#             if people[i] == enemy:
#                 res.append(people[i])

#     return res

# print(del_enem(['polly','helen','bob'], ['helen', 'bob']))

# 1.
# def rock_paper_scissors(player1, player2):
#     player1 = player1.lower()
#     player2 = player2.lower()
#     if player1 not in ['камень', 'ножницы', 'бумага'] or player2 not in ['камень', 'ножницы', 'бумага']:
#         return "Некорректный ввод. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'."
#     if player1 == player2:
#         return "Ничья!"
#     elif (player1 == 'камень' and player2 == 'ножницы') or \
#          (player1 == 'ножницы' and player2 == 'бумага') or \
#          (player1 == 'бумага' and player2 == 'камень'):
#         return "Игрок 1 выиграл!"
#     else:
#         return "Игрок 2 выиграл!"

# result = rock_paper_scissors('камень', 'ножницы')
# print(result)  

# 10.
# def coiner(coins):
#     if (len(coins)) % 3 == 0:
#         return True
#     else:
#         return False


# 2.
# def no_yelling(phrase):
#     while phrase[-2] == '!' or phrase[-2] == '?':
#         phrase = phrase[0:-1]
#     return phrase

# 3.
# def blackjack (cards):
#     sum = 0
#     a_count = 0
#     for card in cards:

#         if type(card) == int:
#             sum += int(card)
#         elif card != 'a':
#             sum += 10
#         elif card == 'a':
#             a_count += 1
#     if sum + (a_count * 11) > 21:
#         sum = sum + (a_count * 11)
#     else:
#         sum = sum + (a_count * 1)

#     if sum > 21:
#         return True
#     else:
#         return False

# 4.
# def sum_numbers_in_string(s):
#     total_sum = 0
#     current_num = ""
#     for char in s:
#         if char.isdigit():  
#             current_num += char  
#         else:
#             if current_num:  
#                 total_sum += int(current_num)  
#                 current_num = ""  
#     if current_num:
#         total_sum += int(current_num)
#     return total_sum
# result = sum_numbers_in_string("abc123def45gh6")
# print(result)

# 5.
# def plus_sign(string):
#     for char in string:
#         if char != '+':
#             return False
#     return True

# 6.
# def convert_time(time_str):
#     if 'AM' in time_str or 'PM' in time_str:
#         time_parts = time_str[:-2].strip().split(':')
#         hours = int(time_parts[0])
#         minutes = int(time_parts[1])
        
#         if time_str.endswith('AM'):
#             if hours == 12:
#                 hours = 0  
#         elif time_str.endswith('PM'):
#             if hours != 12:
#                 hours += 12 
        
#         return f"{hours:02}:{minutes:02}"
    
#     else:
#         time_parts = time_str.strip().split(':')
#         hours = int(time_parts[0])
#         minutes = int(time_parts[1])
        
#         if hours == 0:
#             return f"12:{minutes:02} AM"  
#         elif hours < 12:
#             return f"{hours}:{minutes:02} AM"
#         elif hours == 12:
#             return f"{hours}:{minutes:02} PM"
#         else:
#             return f"{hours - 12}:{minutes:02} PM"


# print(convert_time("02:30 PM"))  # 14:30
# print(convert_time("14:30"))     # 2:30 PM
# print(convert_time("12:00 AM"))  # 00:00
# print(convert_time("00:00"))     # 12:00 AM


# 7.
# def passer(st):
#     sum = 0
#     special_symbol = False
#     capital_symbol = False
#     digit = False
#     lower_symbol = False
#     length = False
#     for i in st:
#         if not i.isalpha() and not i.isdigit():
#             special_symbol = True
#         if i.isupper():
#             capital_symbol = True
#         if i.islower():
#             lower_symbol = True
#         if i.isdigit():
#             digit = True
#     if len(st) >= 16:
#         length = True
#     sum = special_symbol + capital_symbol + digit + lower_symbol + length
#     return f"Ваш пароль получает оценку: {sum}/5"



# 8.
# def number_to_russian(n):
#     if not (0 <= n <= 999):
#         raise ValueError("Число должно быть в диапазоне от 0 до 999")

#     units = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
#     teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
#              "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
#     tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", 
#             "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
#     hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", 
#                 "шестьсот", "семьсот", "восемьсот", "девятьсот"]

#     if n == 0:
#         return "ноль"

#     result = []

#     h = n // 100
#     t = (n % 100) // 10
#     u = n % 10

#     if h > 0:
#         result.append(hundreds[h])
    
#     if t == 1 and u > 0:
#         result.append(teens[u])
#     else:
#         if t > 0:
#             result.append(tens[t])
#         if u > 0:
#             result.append(units[u])

#     return ' '.join(result)


# print(number_to_russian(0))     # "ноль"
# print(number_to_russian(5))     # "пять"
# print(number_to_russian(15))    # "пятнадцать"
# print(number_to_russian(45))    # "сорок пять"
# print(number_to_russian(123))   # "сто двадцать три"
# print(number_to_russian(999))   # "девятьсот девяносто девять"

# 9.
# def lucky_ticket(n):
#     n = n/2
#     n = int(n)
#     suma = 0
#     sum_i = 0
#     sum_j = 0
#     for i in range (0,10**n):
#         for j in range (0,10**n):
#             i = str (i)
#             j = str (j)
#             for num in i:
#                 sum_i += int(num)
#             for num in j:
#                 sum_j += int(num)
#             if sum_j == sum_i:
#                 suma += 1
#             sum_i = 0
#             sum_j = 0

#     return suma

# print(lucky_ticket(4))