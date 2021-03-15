# speedingtraffic.py

"""
This is my idea for the future of speed cameras
"""
# Variables

start_time = start
end_time = end
duration = end_time - start_time
actual_speed = act_speed
maximum_speed = max_speed
start_distance = 0
travel_actual = duration * actual_speed
travel_allowed = duration * max_speed
fast_slow = actual_speed > maximum_speed

"""
At the point of  initial speed detection.
    fast_slow is a positive value
    initial time (start) is noted
    actual_speed (act_speed) fed in from the detection
    constant (max_speed) is known
"""
"""
After some time  
    duration = (end_time - start_time)
Distance travelled 
    travel_actual = duration * actual_speed
    travel_allowed = duration * max_speed

    Example: 
        travel_example_fast = 60secs * 10m/s
        travel_example_slow = 60secs * 5m/s

Distance from start:
    fast_point = travel_example_fast - start_distance
    slow_point = travel_example_slow - start_distance

Lumination:
    From slow_point to fast_point, if fast_slow positive (red), else (green)
"""
