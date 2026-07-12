import socket


def scan_port(target, port):
    """Check whether a single port is open."""

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    try:
        result = scanner.connect_ex((target, port))

        if result == 0:
            return True

        return False

    except socket.gaierror:
        print("Error: The hostname could not be resolved.")
        return False

    except socket.error:
        print("Error: Could not connect to the target.")
        return False

    finally:
        scanner.close()


def run_port_scanner():
    """Ask the user for a target and scan a range of ports."""

    print("\n--- Port Scanner ---")

    target = input("Enter an IP address or website: ").strip()

    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))

        if start_port < 1 or end_port > 65535:
            print("Ports must be between 1 and 65535.")
            return

        if start_port > end_port:
            print("The starting port cannot be greater than the ending port.")
            return

    except ValueError:
        print("Please enter valid port numbers.")
        return

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            print(f"Port {port} is OPEN")
            open_ports.append(port)

    if open_ports:
        print(f"\nScan complete. Open ports: {open_ports}")
    else:
        print("\nScan complete. No open ports were found.") 