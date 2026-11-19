# Task 1: Reverse-Engineer MS-5600 SPI Sensor Data

## Objective
Write a Python script to reverse-engineer the SPI data from an MS-5600 sensor.

## Instructions
Read `reference_data.csv` and `capture.csv`. 

The `reference_data.csv` contains raw SPI bytes captured at known reference temperatures and pressures. Use this data to deduce the bit layout, byte order, and scaling formulas for the temperature and pressure fields.

Then, apply your discovered formulas to `capture.csv`. You must also verify the CRC-8 (polynomial 0x07, initial value 0x00) for each packet over bytes 1-4. 

Write your answers to `/app/answer.txt` EXACTLY in this format:

format_check: spi_data:
failed_crc_ids: <comma-separated_packet_ids_that_fail_CRC>
valid_temp_C: <decoded_temperature_of_first_valid_packet>
valid_press_hPa: <decoded_pressure_of_first_valid_packet>
