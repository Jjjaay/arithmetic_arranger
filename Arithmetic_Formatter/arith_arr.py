import re


def arithmetic_arranger(mprob, answer=False):
  
  # ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

  
  #    32      3801      45      123
  # + 698    -    2    + 43    +  49
  # -----    ------    ----    -----

  if (len(mprob) > 5):
    return "Error: Too many problems."

  first = ""
  sec = ""
  lines = ""
  sumx = ""
  string = ""
  for problem in mprob:
    if (re.search("[^\s0-9.+-]", problem)):
      if (re.search("[/]", problem) or re.search("[*]", problem)):
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."

    firstnum = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    secnum = problem.split(" ")[2]

    if (len(firstnum) >= 5 or len(secnum) >= 5):
      return "Error: Numbers cannot be more than four digits."

    sum = ""
    if (operator == "+"):
      sum = str(int(firstnum) + int(secnum))
    elif (operator == "-"):
      sum = str(int(firstnum) - int(secnum))

    length = max(len(firstnum), len(secnum)) + 2
    top = str(firstnum).rjust(length)
    bottom = operator + str(secnum).rjust(length - 1)
    line = ""
    res = str(sum).rjust(length)
    for l in range(length):
      line += "-"

    if problem != problem[-1]:
      first += top + '    '
      sec += bottom + '    '
      lines += line + '    '
      sumx += res + '    '
    else:
      first += top
      sec += bottom
      lines += line
      sumx += res

  if answer:
    string = first + "\n" + sec + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + sec + "\n" + lines

  return string
