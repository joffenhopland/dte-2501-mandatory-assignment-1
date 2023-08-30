def coin_change(s, denominations):
    # we use `coin_change_list` to store the minimum number of coins required
    # for every value up to s. As a starting point, assume each value requires s coins
    # to ensure that these initial values can be replaced by a smaller number.
    coin_change_list = [s] * (s + 1)
    # Base case: 0 NOK requires 0 coins
    coin_change_list[0] = 0
    # loop through each value from 1 to s to find the minimum number of coins required.
    for i in range(1, s + 1):
        # for each value i, we go through each coin in denominations to see
        # if it can be used to form the value i.
        for coin in denominations:
            # If the current coin can be subtracted from i
            # then check if using this denomination provides a more optimal solution, meaning fewer coins.
            if i - coin >= 0:
                coin_change_list[i] = min(
                    coin_change_list[i], 1 + coin_change_list[i - coin]
                )
    # returning the minimum number of coins required for the sum s
    return coin_change_list[s]


s = 1040528
denominations = [1, 5, 10, 20]
result = coin_change(s, denominations)
print(f"Minimum number of coins needed for {s} NOK is {result}")
