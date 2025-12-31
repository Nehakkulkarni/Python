list=[1,6,3]
copy_list=list.copy()
copy_list.reverse()

if(copy_list == list):
    print("Palindrome.")
else:
    print("Not a palindrome.")