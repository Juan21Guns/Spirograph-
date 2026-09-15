# Spirograph-
Drawing a spirograph in python using Turtle. Finding ways to improve time complexity through higher subdivisions. 

Through first completion of my code, I had complex shapes drawn with greatly increasing time complexity. 

At 16 circles and 18 steps per enumeration, time to render the image was: 10.120298s. 

<img width="351" height="291" alt="Screenshot 2026-09-15 163201" src="https://github.com/user-attachments/assets/54de497d-85ca-4a2d-902f-29501b675f70" />

While at 64 circles and 90 steps, time to render was: 290.6891754

<img width="388" height="313" alt="Screenshot 2026-09-15 163822" src="https://github.com/user-attachments/assets/fae9d222-2a5a-4bb3-8460-d5c0fb78d22f" />

Time complexity with rendering is O(n^2) as it is based on number of circles. Increasing resolution with the circle (steps) increases time spent per circle. I mitigated this issue as much as possible by placing any calculations done in the loops outside, as well as precomputing x-coords, but due to Turtle am still bottlenecked. 

New time w/ 18 steps, 16 circles: 9.855s
New time w/ 90 steps, 64 circles: 288.936s

Feel free to grab the code and try it for yourself! There are a lot of parameters you can toggle to change the color, definition, and size of the spirograph.
