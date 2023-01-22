# Run Code Concurrently Using the Threading Module
[[Threading - Example]]

In order to utilize threading you will have to `import threading` at the beginning of your program. 
Then, instead of running the `do_something` function multiple times, lets turn them into threads instead. To do so, you need to start a thread as follows
`t1 = threading.Thread(target=function_name)` where the target is the function you want to execute. Note that you are passing in the function as an argument you are not executing the function in the creation of the thread.
```python
import time
import threading


start = time.perf_counter()

def do_something():
	print ('Sleeping 1 second....')
	time.sleep(1)
	print('Done Sleeping...')

#do_something()
t1 = threading.Thread(target=do_something)
#do_something()
t2 = threading.Thread(target=do_something)

finish = time.perf_counter()
```
Now we have created two thread objects but we are not actually running those functions. In order to make those functions run we need to use the `start` method on the thread
```python
start = time.perf_counter()

t1 = threading.Thread(target=do_something)
#do_something()
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()
finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)' '')
```
 This code will make the code run concurrently, however, the print function will execute before the threads have finished running, and you will not get an accurate timing for execution time. In order to make certain threads have completed before  moving on you can use the `join` method as follows
```python
start = time.perf_counter()

t1 = threading.Thread(target=do_something)
#do_something()
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()
t1.join()
t2.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)' '')
```

You can easily see how to create many threads using a loop as follows
```Python
threads = []
for _ in range(10):
	t = threading.Thread(target=do_something)
	t.start()
	threads.append(t)
for thread in threads:
	thread.join()
```


## Passing Arguments to a thread
Now we know how to thread methods that do not take an argument, but what if the method we want to execute _does_ take arguments. We can do so as follows:
```Python
def do_something(seconds):
	print("Sleeping for " + str(seconds) + "seconds")
	time.sleep(seconds)
	print("Done Sleeping...")

for _ in range(10):
	t = threading.Thread(target=do_something, args=[1.5])
	t.start()
	threads.append(t)
for thread in threads:
	thread.join()

```

### Source Material
[link](https://www.youtube.com/watch?v=IEEhzQoKtQU)

