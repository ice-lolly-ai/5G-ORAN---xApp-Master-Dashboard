import random

def generate_interface_data():
    return {
        "E1": {
            "throughput": random.uniform(100, 1000),  # Mbps
            "latency": random.uniform(10, 100),       # ms
            "spec_ref": "https://www.3gpp.org/ftp/Specs/archive/38_series/38.463/38463-g00.zip"
        },
        "F1": {
            "throughput": random.uniform(100, 1000),
            "latency": random.uniform(10, 100),
            "spec_ref": "https://www.3gpp.org/ftp/Specs/archive/38_series/38.473/38473-g00.zip"
        },
        "Xn": {
            "throughput": random.uniform(100, 1000),
            "latency": random.uniform(10, 100),
            "spec_ref": "https://www.3gpp.org/ftp/Specs/archive/38_series/38.423/38423-g00.zip"
        },
        "NG-C": {
            "throughput": random.uniform(100, 1000),
            "latency": random.uniform(10, 100),
            "spec_ref": "https://www.3gpp.org/ftp/Specs/archive/38_series/38.413/38413-g00.zip"
        },
        "NG-U": {
            "throughput": random.uniform(100, 1000),
            "latency": random.uniform(10, 100),
            "spec_ref": "https://www.3gpp.org/ftp/Specs/archive/38_series/38.415/38415-g00.zip"
        },
        "S1": {
            "throughput": random.uniform(100, 1000),
            "latency": random.uniform(10, 100),
            "spec_ref": "https://www.3gpp.org/ftp/Specs/archive/36_series/36.413/36413-g00.zip"
        }
    }
