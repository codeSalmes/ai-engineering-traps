# Task 3: Thermal Analysis of a Power MOSFET

## Objective
Write a Python script to calculate the steady-state junction temperature of a power MOSFET and determine if it operates within its safe limits.

## Instructions
Read `specs.txt` for the device parameters and environmental conditions.

**Important:** The MOSFET's on-resistance (`Rds_on`) increases with temperature. You must account for this thermal feedback loop to find the true steady-state junction temperature. Furthermore, ensure that the design does not exceed ANY of the maximum limits specified in the datasheet.

Write your answers to `/app/answer.txt` EXACTLY in this format (round to 2 decimal places):

format_check: thermal:
nominal_power: <power_calculated_at_25C_Rds_on_in_W>
actual_power: <power_calculated_at_steady_state_Tj_in_W>
junction_temp: <calculated_steady_state_junction_temp_in_C>
status: <PASS_or_FAIL>
