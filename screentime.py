import d3dshot
import numpy as np
d = d3dshot.create(capture_output="numpy")

d.screenshot()

print(np.shape(d.get_latest_frame()))