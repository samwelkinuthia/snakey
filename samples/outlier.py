def out(n):
    odd = [x for x in n if x%2 != 0]
    even = [x for x in n if x%2 is 0]
    return odd[0] if len(odd)<len(even) else even[0]

n = [212, 234, 22, 31]
print("Behold the outlier is " + str(out(n)))

# def outlier(n):
#     even = False
#     tot1 = 0
#     tot2 = 0
#     for i in n:
#         if i % 2 != 0:
#             tot1 += 1
#         elif i % 2 == 0:
#             tot2 += 1
#             if tot2 > 1:
#                 even = True
#
#     if even:
#         for i in n:
#             if i % 2 != 0:
#                 return i
#     elif not even:
#         for i in n:
#             if i % 2 == 0:
#                 return i
#
