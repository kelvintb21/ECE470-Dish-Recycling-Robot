# ECE470-Dish-Recycling-Robot
UIUC ECE470 project
The dish recycling robot will be served mainly in restaurants to help collect used plates and
bowls from customer’s table and send to dishwasher to save human labor. The robot has two
modes programmed in its system. The first is idle mode, which the robot stays in one position or
patrol around waiting for commands. The second is working mode, which the robot will goes to
one table and waiting for customers to put their tableware on robot arms, and then the robot will
contain the dishes into its body automatically. 

In both modes, the robot will remain constant speed and keep constant distance from others 
when moving in designated lane. PID algorithm is applied to help achieve the constant speed and spacing.
By recieving sensor installed on the robot, the program can know the present speed and distance from others,
and gradually change to target speed and distance.

By simulating the process, the robot can obtain optimal PID coefficients and optimal value function
to help the algorithm reduce noises.
