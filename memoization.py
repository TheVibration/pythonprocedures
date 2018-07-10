# cached_execution uses memoization which
# which saves previously run results. cache is
# a dictionary in which the previous results 
# are stored. proc is a procedure that will
# return a result, and proc_input is the input 
# that will be used as a key in cache.

def cached_execution(cache, proc, proc_input):
    if proc_input in cache:
        return cache[proc_input]
    else:
        cache[proc_input] = proc(proc_input)
        return cache[proc_input]
