# Functional Scope

def test_fun():
    a = 10
    local_var = 34
    print("hello world")
    print(a)


test_fun()


def test1():
    print("outer function")

    def test2():
        print("inner function")
