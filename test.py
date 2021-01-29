def even():
    result = []
    for i in list(range(1, 51)):
        if i % 2 == 0:
            result.append(i)
    return result