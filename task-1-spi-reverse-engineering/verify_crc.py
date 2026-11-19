def crc8(data):
    crc = 0x00
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x07
            else:
                crc = crc << 1
    return crc & 0xFF

print(f"Packet 201 CRC: {hex(crc8([0x09, 0xC4, 0x27, 0x10]))}") # Should be 0x35
print(f"Packet 202 CRC: {hex(crc8([0x0A, 0x8C, 0x27, 0x5A]))}") # Should be 0x29
print(f"Packet 203 CRC: {hex(crc8([0x09, 0x60, 0x26, 0xFC]))}") # Should be 0x49
