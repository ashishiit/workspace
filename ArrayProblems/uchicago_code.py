'''
Crenested_listted on Jun 17, 2018

@nested_listuthor: S528358
'''
def flatten_list(nested_list):
    i = 0
    while i < len(nested_list):
        while True:
            try:
                nested_list[i:i+1] = nested_list[i]
            except(TypeError, IndexError):
                break
        i = i + 1
    return nested_list
nested_list = [2, [[3, [4]], 5]]
print(flatten_list(nested_list))
 