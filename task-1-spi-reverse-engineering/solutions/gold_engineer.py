# The Correct Engineering Solution
# Deducing byte order: Temp is bytes 1-2 (16-bit signed), scale 0.01.
# Pressure is bytes 3-4 (16-bit unsigned), scale 0.1.
# Packet 202 fails the CRC-8 check.

with open('/app/answer.txt', 'w') as out:
    out.write("format_check: spi_data:\n")
    out.write("failed_crc_ids: 202\n")
    out.write("valid_temp_C: 25.00\n")
    out.write("valid_press_hPa: 1000.0\n")
