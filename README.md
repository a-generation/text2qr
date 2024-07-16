# text2qr

This Python script generates a QR code from a given text input and saves it as a .png file.

## Usage

1. **Clone the repository:**

   ```bash
   git clone https://github.com/a-generation/qr-code-generator.git
   cd qr-code-generator
   ```

2. **Install dependencies (if not already installed):**

   ```bash
   pip install qrcode[pil]
   ```

3. **Run the script:**

   ```bash
   python qr.py "Hello, World!" hello_world_qr
   ```

   Replace `"Hello, World!"` with your desired text and `hello_world_qr` with the desired filename (without extension).

4. **Output:**

   The script will generate a QR code based on the input text and save it as `hello_world_qr.png` in the current directory.

## Example

```bash
python qr.py "Hello, World!" hello_world_qr
QR code successfully generated and saved to: hello_world_qr.png
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
