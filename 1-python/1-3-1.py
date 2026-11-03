# When you write a function first step
# write program
# input
# numbers = [ 2, 3, 5, 10] # 20

# # process
# total = sum(numbers) # 20
# count = len(numbers) # 4
# avg = total / count # 5.0

# # output
# print(avg) # 5.0

# Second step: re-write program into function
def average(numbers: list[float]) -> float:
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return avg

def test_avg():
    numbers = [1, 1, 1, 1]
    expect = 1.0
    actual = average(numbers)
    assert actual == expect

test_avg

