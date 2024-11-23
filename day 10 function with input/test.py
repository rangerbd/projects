def format_name(fname,lname):
    

    formated_fname = fname.capitalize() 
    formated_lname = lname.capitalize()

    add = formated_fname + formated_lname
    print (add)
   
concate = format_name("dipto","gosswami")

#call a function within a function

def f_function(name):
    return name+name

def f_function2(name):
    return name.capitalize()

print( f_function2(f_function("dipto")))