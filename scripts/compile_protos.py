import os
import subprocess
from pathlib import Path

def main():
    # Create directories
    proto_dir = Path("celestia_proto")
    proto_dir.mkdir(exist_ok=True)

    # Create the package directory structure
    (proto_dir / "cosmos" / "params" / "v1beta1").mkdir(parents=True, exist_ok=True)

    # Create __init__.py files
    for path in [
        proto_dir,
        proto_dir / "cosmos",
        proto_dir / "cosmos" / "params",
        proto_dir / "cosmos" / "params" / "v1beta1"
    ]:
        (path / "__init__.py").touch()

    # Compile proto with correct package path
    subprocess.run([
        "python", "-m", "grpc_tools.protoc",
        f"--proto_path={proto_dir.parent}",
        f"--python_out={proto_dir.parent}",
        f"--grpc_python_out={proto_dir.parent}",
        str(proto_dir / "cosmos" / "params" / "v1beta1" / "params.proto")
    ])

if __name__ == "__main__":
    main()