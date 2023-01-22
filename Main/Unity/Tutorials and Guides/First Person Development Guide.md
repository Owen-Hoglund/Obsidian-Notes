1. Create an Empty Object named Character
2. Add character controller component
3. Change size of controller
4. Add Cylinder to Character component
5. Remove collider on cylinder (already exists on controller)
6. Add a camera to the Character
7. Add Look Script 
Add the following script to the Camera object on the Character
```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MouseLook : MonoBehaviour
{
	public float mouseSensitivity = 1000f;
	public Transform playerBody;
	float xRotation = 0f;
	
	// Start is called before the first frame update
	void Start()
	{
		Cursor.lockState = CursorLockMode.Locked;
	}
	// Update is called once per frame
	void Update()
	{
		float mouseX = Input.GetAxis("Mouse X") * mouseSensitivity * Time.deltaTime;
		float mouseY = Input.GetAxis("Mouse Y") * mouseSensitivity * Time.deltaTime;
		xRotation -= mouseY;
		xRotation = Mathf.Clamp(xRotation, -90f, 90f);
		transform.localRotation = Quaternion.Euler(xRotation, 0f, 0f);
		playerBody.Rotate(Vector3.up * mouseX);
	}
}
```

8.  Add PlayerMovementScript

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class PlayerMovement : MonoBehaviour
{
    public CharacterController controller;
    public Transform groundCheck;
    public float groundDistance = 0.3f;
    public LayerMask groundMask;
    bool isGrounded;
    public float speed = 10f;
    public float gravity = -9.81f;
    Vector3 velocity;
    // Update is called once per frame
    void Update()
    {
	    isGrounded = Physics.CheckSphere(groundCheck.position, groundDistance, groundMask);

        if (isGrounded && velocity.y < 0) {
            velocity.y = -2f;
        }
        
        float x = Input.GetAxis("Horizontal");
        float z = Input.GetAxis("Vertical");
        Vector3 move = transform.right  * x + transform.forward * z;
        controller.Move(move * speed * Time.deltaTime);
        velocity.y += gravity * Time.deltaTime;
        controller.Move(velocity * Time.deltaTime);
    }

}
```

9. Add Gravity 
	The Script has taken care of most of the heavy lifting already, but now we need to do a couple things to our environment to make it all come together.
	1. Add empty object to Character
	2. Move it to the bottom of character
	3. Rename it GroundCheck
	4. Drag GroundCheck into the playermovement script on the character controller
	5. Change layer of all environment objects to be ground


---
# Making Hands
1. Under the camera object, create a new empty object called hands
2. Drag that object to where you want the hands to be located in the players perspective
3. Create a new object under hands called Holding Position
4. Create two new spheres under hands and make them spaced out to represent two hands
5. 