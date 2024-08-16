def sum_all(*args):
    print(args)
    for i in args:
        print(2*i)
    # print(*args)
    return sum(args);

# print(sum_all(1,2));
# print(sum_all(1,2,3,4,5,6,7));
print(sum_all(1,2,3,4,5))