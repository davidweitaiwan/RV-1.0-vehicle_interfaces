uint8 ORIGIN_TYPE_LT = 0 # Left Top
uint8 ORIGIN_TYPE_LB = 1 # Left Bottom
uint8 ORIGIN_TYPE_RT = 2 # Right Top
uint8 ORIGIN_TYPE_RB = 3 # Right Bottom
uint8 ORIGIN_TYPE_CENTER = 4 # Center

Point2f o # Origin point {x, y}
uint8 origin_type 0 # Type of origin point
Size2f size # Boundary {width, height}
uint16 label # Object category
uint16 id # Object ID
