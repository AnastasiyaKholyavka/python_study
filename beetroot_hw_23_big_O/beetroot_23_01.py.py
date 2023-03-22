"""
task_25

"""

# answers 
# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n
# 5 - n^2
# 6 - log n


# 1 - n - тому, що список постійно поповнюється новими даними, які йдуть одне за одним
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

# 2 - 1 тому, що є тільки одна дія
def question2(n: int) -> int:
	for _ in range(10):
		n **= 3
	return n

# 3 - n^2 бо є цикл у циклі
def question3(first_list: List[int], second_list: List[int])-> List[int]:
   temp: List[int] = first_list[:]
   for el_second_list in second_list:
      flag = False
      for check in temp:
         if el_second_list == check:
            flag = True
            break
      if not flag:
         temp.append(second_list)
   return temp

# 4 - n тому, що тільки одна дія виконується
def question4(input_list: List[int]) -> int:
  res: int = 0
  for el in input_list:
    if el > res:
      res = el
  return res
 
# 5 - n^2 бо є дві дії над n, два цикла
def question5(n: int) -> List[Tuple[int, int]]:
    res: List[Tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res

# 6 - log n тому, що відсіюється частина елемантів
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n