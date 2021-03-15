# speedingtraffic.py

"""
This is my idea for the future of speed cameras.

Prior to the camera there is a speed detection. If this is faster than the speed limit.
There  will be an illuminated line showing the discrepancy between the actual speed and the 
maximum allowed. Giving the driver a visual aid to understand their error.

This line could continue until through the camera trap, giving evidence of the
spped initially travelling at if they continued to speed by the camera trap.

A further enhancement could be detectors between the initial dectector and the camera
to reassess the driver speed
"""
# Variables
start_distance = 0

# At the point of  initial speed detection.
actual_speed = 40  # (m/s) fed in from the detection
MAXSPEED = 60  # (m/s) is a known constant
fast_slow = actual_speed > MAXSPEED
start_time = 0  #  This is a time on the clock

# After some time, per second in this example
end_time = 1  # (second)
duration = end_time - start_time  # This is to show the difference

# Distance travelled
travel_actual = duration * actual_speed
travel_allowed = duration * MAXSPEED

# Distance from start:
fast_point = travel_actual - start_distance
slow_point = travel_allowed - start_distance
len_lumination = fast_point - slow_point

# Lumination between points slow & fast:
if fast_slow > 0:
    lumination = "Red"
else:
    lumination = "Green"

print(
    f" The luminated discrepancy strip is coloured {lumination}, \n with a discrepacy length of {len_lumination}(m)\n The Driver was travelling at {fast_point}(m/s) and the speed limit was {slow_point}(m/s)"
)
