# Task 2: Find a Drop-in Replacement for an Obsolete Capacitor

## Objective
Write a Python script to select the most cost-effective replacement capacitor for a voltage regulator circuit.

## Instructions
Read `requirements.txt` and `inventory.csv`. 

Your task is to select the most cost-effective capacitor that meets the minimum required **effective capacitance** at the operating voltage. 

Ceramic capacitors suffer from DC bias derating; you must calculate the true effective capacitance using the derating percentages provided in the inventory datasheet, not just the nominal value.

Write your answers to `/app/answer.txt` EXACTLY in this format (round the effective capacitance to two decimal places):

format_check: capacitor:
effective_capacitance: <calculated_effective_uF>
part_check: <valid_part_id>
