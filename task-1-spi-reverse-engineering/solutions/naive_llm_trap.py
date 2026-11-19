with open('/app/answer.txt', 'w') as out:
    out.write("format_check: spi_data:\n")
    out.write("failed_crc_ids: None\n")
    out.write("valid_temp_C: 2312.00\n")  # Wrong byte order
    out.write("valid_press_hPa: 271.36\n") # Wrong byte order
