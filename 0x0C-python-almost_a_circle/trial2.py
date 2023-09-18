def myFun(**kwargs):
    for k in args:
        print(k)


# Now we can use *args or **kwargs to
# pass arguments to this function :
args = ("Geeks", "for", "Geeks")
i = None
kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
myFun(i)
