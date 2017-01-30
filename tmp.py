from ast import literal_eval as make_tuple
import ast
print(make_tuple("(1,2,3,4,5)"))
mylist = ast.literal_eval('''(9140,'aa','Category:User de'),(25539,'aa','Category:User de-1'),(98724,'aa','Main Page')''')
for l in mylist:
    print(l)