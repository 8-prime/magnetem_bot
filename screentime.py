import d3dshot
import numpy as np

d = d3dshot.create(capture_output="numpy")
image = d.screenshot()