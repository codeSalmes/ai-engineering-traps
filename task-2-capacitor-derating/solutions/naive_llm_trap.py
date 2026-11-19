# The Naive LLM Trap
# Chooses CAP-002 based on nominal 10uF, ignoring DC bias derating.
# Thinks it passes the 8.0uF requirement because 10 > 8.

with open('/app/answer.txt', 'w') as out:
    out.write("format_check: capacitor:\n")
    out.write("effective_capacitance: 10.00\n")
    out.write("part_check: CAP-002\n")
