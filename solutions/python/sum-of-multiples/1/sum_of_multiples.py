def sum_of_multiples(level, factors):
    multiples = set()  # مجموعة لتخزين المضاعفات بدون تكرار
    
    for factor in factors:  # نكرر لكل عنصر في القائمة
        if factor == 0:      # نتجنب القسمة على صفر
            continue
        # نضيف كل المضاعفات اللي أقل من level
        for i in range(factor, level, factor):
            multiples.add(i)
    
    return sum(multiples)  # نجمع كل الأرقام بعد إزالة التكرارات

# مثال للتجربة
print(sum_of_multiples(20, [3, 5]))  # الناتج: 78