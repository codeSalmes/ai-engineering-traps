# The Correct Engineering Solution
# Calculates effective capacitance at 12V. 
# CAP-002: 10uF * 75% = 7.5uF (Fails the 8.0uF requirement).
# CAP-003: 22uF * 50% = 11.0uF (Passes). Cheapest valid option.

with open('/app/answer.txt', 'w') as out:
    out.write("format_check: capacitor:\n")
    out.write("effective_capacitance: 11.00\n")
    out.write("part_check: CAP-003\n")
