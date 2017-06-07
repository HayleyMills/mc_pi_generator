mc_pi_generator
A simple Monte Carlo simulation using 1000000 points to generate pi to 16 decimal places. 

The area of a circle is calculated by the area of the circle/area of the square it is inside. 

First the area of quarter of a circle with a radius of 1 is calculated using 1000000 random numbers generated between 0 and 1 
and the equation of a circle x2 + y2 = r2. As we know that the radios of the circle is 1 any radius calculated which is greater 
than 1 must be outside of the circle and any radios less than 1 must be inside the circle. 

The area of the whole circle is calculated as the total in the circle/total of the square * 4. As the radios of the circle is 1 
this is also equal to pi.
