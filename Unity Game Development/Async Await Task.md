The Async Away Task structure is a helpful toolset for running asynchronous code. The general structure is illustrated in the following code. 
```C#
using UnityEngine;
using System.Threading.Tasks; // Necessary to use Task
public class AsyncTesting : MonoBehaviour
{
    void Start(){
        test(); // Begins our asynchronous Function
        
        // Illustrates that test is running in the background
        Debug.Log("We Are now Waiting for Test to finish"); 
    }
    private async void test(){
        Debug.Log("Operation Starting");
        await Task.Run(() => waitThreeSeconds());
        Debug.Log("Operation Finished");
    }
    private void waitThreeSeconds(){
        System.Threading.Thread.Sleep(3000);
    }
}
```

```
Output:
Operation Starting
We Are now Waiting for Test to finish
Operation Finished
```

### Walkthrough
1. Import `System.Threading.Tasks`
2. Define an `async` function test
3. Start running a `Task` on another thread
	1. Task takes a  [[Lambda Expressions and Delegates|lambda expression]] as an argument
	2. In our case our lambda takes no arguments and executes the `waitThreeSeconds` function
3. We return to the code just after the point at which we started the async function and print our "we are waiting" statement.
4. `waitThreeSeconds` finishes executing on the other thread and so we proceed to the next line and print "Operation Finished"

