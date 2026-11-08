print("hello world")

print("read the log and push chnages")

#decorators

def fun1(fun):
    def wrapper():
        print("start of session")
        fun()
        print("end of sessions")

    return wrapper



@fun1
def fun_test():
    print("hellow world")

fun_test()

def fun_test2():
    print("changing to miss world")

fun_test2()

print("decortor learned")
