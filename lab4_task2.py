mydict={}
def get_count_char(str_):
   mydict={}
   str_=str_.lower()
   for letter in str_:
       if letter.isalpha():
           if letter in mydict:
               mydict[letter]+=1
           else:
               mydict[letter]=1
   return mydict
print(mydict) 