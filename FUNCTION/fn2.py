#DECORATORS
#when we want to make modifications in our function but we can't directly access function,then we should go by this way i.e decorators

def div(a,b):
	print(a/b)


def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
        
    return inner

div=smart_div(div)

div(4,2)
div(2,4)    
         