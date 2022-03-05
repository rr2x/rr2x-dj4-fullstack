try:
    print(1/0)
    # print("yo")
except IOError:
    print("you have input/output error")
except TypeError:  # specific type of error catched
    print("wrong data type used")
except:
    print("general error")
else:
    print("else block ran")  # only run if no exception
finally:  # always runs even if there is an exception
    print("finally ran, error or no error")
