.PHONY: analyze clean help

help:
	@echo "APK Security Lab - Available commands:"
	@echo "  make analyze  - Run the security audit pipelines"
	@echo "  make clean    - Clean up temporary logs and cache"

analyze:
	@echo "Running Antigravity Deepsearch Engine Analysis..."

clean:
	@echo "Cleaning up __pycache__ and logs..."
	rm -rf __pycache__ reports/*.pcap
