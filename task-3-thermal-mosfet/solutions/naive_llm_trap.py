# The Naive LLM Trap
# Assumes Rds_on stays at 0.008 Ohms. 
# P = 1.80W, Tj = 127.70C. Thinks it passes because 127.70 < 175.
# Completely misses the iterative feedback loop and the power limit.

with open('/app/answer.txt', 'w') as out:
    out.write("format_check: thermal:\n")
    out.write("nominal_power: 1.80\n")
    out.write("actual_power: 1.80\n")
    out.write("junction_temp: 127.70\n")
    out.write("status: PASS\n")
