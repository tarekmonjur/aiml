import timeit

n = 1_000_000
n_list = list(range(n))
n_set = set(n_list)
n_tpl = tuple(n_list)

list_time = timeit.timeit("999999 in n_list", globals=globals(), number=1000)
set_time = timeit.timeit("999999 in n_set", globals=globals(), number=1000)
tpl_time = timeit.timeit("999999 in n_tpl", globals=globals(), number=1000)
print(f"List: {list_time:.6f} seconds")
print(f"Set: {set_time:.6f} seconds")
print(f"Tuple: {tpl_time:.6f} seconds")