def ft_count_harvest_recursive(days=None, cur=1):
    if days is None:
        days = int(input("Days until harvest: "))
    if cur > days:
        print("Harvest time!")
        return
    print("Day", cur)
    ft_count_harvest_recursive(days, cur + 1)
