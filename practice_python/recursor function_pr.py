def counting(num : int):
    print('num',num)

    if num == 0:
        print('counting done')

    else:
        counting(num-1)

counting(10)
