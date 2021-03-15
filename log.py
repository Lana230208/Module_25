def logger(func):
    def wrapper(*args, **kwargs):
        f = open("log.txt", "a")
        f.write(args[0])
        r = func(*args, **kwargs)
        f.write(str(r))
        f.write("\n")
        f.close()
        return r
    return wrapper


@logger
def say(s):
    print(s)


# say("hello")
