_author_ = 'dev'

# number = "9,233,372,036,854,775,807"
# cleanedNumber = ''
#
# for char in number:
#     if char in '0123456789':
#         cleanedNumber = cleanedNumber + char
#
# newNumber = int(cleanedNumber)
# print("The number is {} \n".format(newNumber))
#
#
#
# for state in ["not pinin'", "no more", "a stiff", "bereft of lift"]:
#     print("This parrot is " + state)
#     #in place of
#     #print("This parrot is {}".format(state))
#
# for i in range(0,100, 5):
#     print("i is {}".format(i))

for i in range(1,13):
    for j in range(1,13):
        print("{0} times {1} is {2}".format(i,j,i*j, end='\t'))
    print("======================================")
    print('')