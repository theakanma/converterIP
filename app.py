import ipaddress

def ipv4_to_decimal(ipv4_address):
     try:
         decimal_address = int(ipaddress.IPv4Address(ipv4_address))
         return decimal_address
     except ipaddress.AddressValueError:
         return None

def ipv6_to_decimal(ipv6_address):
     try:
         decimal_address = int(ipaddress.IPv6Address(ipv6_address))
         return decimal_address
     except ipaddress.AddressValueError:
         return None

# Examples of using
ipv4_address = input("Enter IPv4 address: ")
ipv6_address = input("Enter IPv6 address: ")

decimal_ipv4 = ipv4_to_decimal(ipv4_address)
decimal_ipv6 = ipv6_to_decimal(ipv6_address)

if decimal_ipv4 is not None:
     print(f"IPv4 in decimal: {decimal_ipv4}")
else:
     print("Incorrect IPv4 address")

if decimal_ipv6 is not None:
     print(f"IPv6 in decimal: {decimal_ipv6}")
else:
     print("Incorrect IPv6 address")
