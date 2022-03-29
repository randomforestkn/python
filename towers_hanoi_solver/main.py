def move(fr, to):
    print(f"Move from {fr} to {to}")


def foo(n, fr, to, spare):
    if n == 1:
        move(fr, to)
    else:
        foo(n-1, fr, spare, to)
        foo(1, fr, to, spare)
        foo(n-1, spare, to, fr)


foo(14,"b","a","c")
