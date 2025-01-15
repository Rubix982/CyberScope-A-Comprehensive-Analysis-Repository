# Define the build output directory
BUILD_DIR := ./target/rust_bins

# Default target
.PHONY: all
all: build

# cargo build --manifest-path ./src2/Cargo.toml
.PHONY: build
build:
	cargo build --release --manifest-path ./src/fetch_data/Cargo.toml --target-dir $(BUILD_DIR)/fetch_data

.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
