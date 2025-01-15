from utils import get_project_root
import os

# Binary paths
RUST_BIN_PATH = f"{os.path.join(get_project_root(), '/target/rust_bins/')}"
FETCH_DATA_BIN_PATH = f"{os.path.join(RUST_BIN_PATH, 'fetch_data', 'release', 'fetch_data')}"
