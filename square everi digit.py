# def square_digits(num):
#     final = ''
#     for item in num:
#         final = final + str(int(item) ** 2)
#     return int(final)

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
