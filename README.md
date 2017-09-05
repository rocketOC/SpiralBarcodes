# Spiral Barcodes
Make spiral, circular, x-locked, y-locked, and standard movie barcodes

# Use
Find the average color of frames in a video. Use these averages to color an output image progressively. The output images often resemble colorful barcodes.

# Types of Barcodes
1. Spiral: The average frame colors are used to produce a spiral. Time runs clockwise from noon by default.
2. Circular (donut): The average frame colors are used to produce a donut. Time runs clockwise from noon by default.
3. x-locked (vertical): Find the average color of each column in the frame. This average row will form one horizontal slice of the output image. Time runs from top to bottom.
4. y-locked (horizontal): Find the average color of each row in the frame. This average column will form one vertical slice of the output image. Time runs from left to right.
5. Standard: The average frame colors form one vertical slice of the output image. Time runs from left to right.

# Future
1. OpenCV uses a round brush when drawing elliptical arcs. This makes the circular barcode tail overlap the head. Spiral mode is a temporary workaround. I want a proper closed circle with no overlap.
2. I would like to map or animate a trail through an hsv cone or 3D color space. It's hard to understand the quantitative jumps in color that occur in the other barcode types. I think an animation through space would help reveal gradual and sudden transitions.
3. A small tkinter GUI would be nice for those who are not used to dealing with command line interactions.

# Notes
1. If you sample too many frames when creating circular or spiral barcodes, the image will collapse to a solid circle at the center of the image.
2. Movie resolution does not matter for standard, circular, and spiral barcodes
3. I've only tested the program on mov and mp4 input files. It may work with other video types.
4. Frame count meta data may be incorrect for some input videos. In that case you may have to manually set the dimensions of the output image blanks.

# Examples
1. [spiral based on Rick and Morty episode 101](https://i.imgur.com/QoitVc9.png)
2. [x-locked based on Rick and Morty episode 101](https://i.imgur.com/c1CXf3J.png)
3. [y-locked based on Rick and Morty episode 101](https://i.imgur.com/ZX2iC3p.png)
4. [standard based on Rick and Morty episode 101](https://i.imgur.com/yMcUwkr.png)