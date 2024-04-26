import tokenize

with tokenize.open("hello.py") as f:
    tokens = tokenize.generate_tokens(f.readline)
    for i in tokens:
        print(i)