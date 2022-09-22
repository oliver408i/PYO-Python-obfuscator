# PYO Python Obfuscator
A simple yet strong python obfuscator that makes code unreadable. This obfuscator isn't like others that just replace parts of the code with weird variable names. This obfuscator completely scrambles the code. It makes the source code very hard (if even possible) to get to, even if you are really good at python.
### Why PYO?
- Simple & fast
- 4 layers of protection, each getting harder reverse
- No extra files needed, just the code
- Works on all computers that support Python 3.8+ unlike python exe compilers
- Python 3.8+
- No packages needed for you and the user
- No installation for you, just download and run
- Not much of the side difference (for larger scripts)
## Example
**INPUT**
```py
print("hello world")
```
**OUTPUT**  
*Note: There is much more behind this than just base64, read the next section to learn more*
```py
import base64 as b;exec(b.b64decode('X19QWU9fXzAyNTQgPSBsYW1iZGEgeDp4LnJlcGxhY2UoIl9fUFlPX18zOTYzIiwibSIpLnJlcGxhY2UoIl9fUFlPX185NjUxIiwgInAiKS5yZXBsYWNlKCJfX1BZT19fMDc1NCIsICJhIikucmVwbGFjZSgiX19QWU9fXzkzNjQiLCAicyIpLnJlcGxhY2UoIl9fUFlPX184NTQxIiwiZSIpLnJlcGxhY2UoIl9fUFlPX18xMzQ3IiwgInIiKS5yZXBsYWNlKCJfX1BZT19fODY1MyIsImIiKS5yZXBsYWNlKCJfX1BZT19fMjUxNCIsICJvIikucmVwbGFjZSgiX19QWU9fXzI3NTQiLCAidCIpLnJlcGxhY2UoIl9fUFlPX184NDEzIiwiaSIpLnJlcGxhY2UoIl9fUFlPX18wOTg1IiwgImMiKS5yZXBsYWNlKCJfX1BZT19fNDcwMSIsICIuIikucmVwbGFjZSgiX19QWU9fXzgwNTEiLCAibCIpLnJlcGxhY2UoIl9fUFlPX18zODYiLCAiKCIpLnJlcGxhY2UoIl9fUFlPX18zMzUiLCAiKSIpCmV4ZWMoX19QWU9fXzAyNTQoIl9fUFlPX184NDEzX19QWU9fXzM5NjNfX1BZT19fOTY1MV9fUFlPX18yNTE0X19QWU9fXzEzNDdfX1BZT19fMjc1NCBfX1BZT19fMzk2M19fUFlPX18wNzU0X19QWU9fXzEzNDdfX1BZT19fOTM2NGhfX1BZT19fMDc1NF9fUFlPX184MDUxIF9fUFlPX18wNzU0X19QWU9fXzkzNjQgX19QWU9fXzM5NjMsIF9fUFlPX184NjUzX19QWU9fXzA3NTRfX1BZT19fOTM2NF9fUFlPX184NTQxNjQgX19QWU9fXzA3NTRfX1BZT19fOTM2NCBfX1BZT19fODY1MyIpKQpleGVjKF9fUFlPX18wMjU0KCJfX1BZT19fODU0MXhfX1BZT19fODU0MV9fUFlPX18wOTg1X19QWU9fXzM4Nl9fUFlPX18zOTYzX19QWU9fXzQ3MDFfX1BZT19fODA1MV9fUFlPX18yNTE0X19QWU9fXzA3NTRkX19QWU9fXzkzNjRfX1BZT19fMzg2X19QWU9fXzg2NTNfX1BZT19fNDcwMV9fUFlPX184NjUzODVkX19QWU9fXzg1NDFfX1BZT19fMDk4NV9fUFlPX18yNTE0ZF9fUFlPX184NTQxX19QWU9fXzM4NlwnO3tYNXYwMDAwMDAwMDAwMDAwMDAwMElDMjA2K2kkMENObGcwMDNuR1dCYEshMFJVdEhRdmZMZmRKQVl9WTsxMkpjVy1pUldLSm1vKzY4Y09YPk4zPjBDRUJWMDA0M1YwMDAybTVubz9XU3g7WUlaKD9TM2I3TnQyV258aDJKWioxZWIhPXJtMFJSOTFeOGYkPDAwXCdfX1BZT19fMzM1X19QWU9fXzMzNV9fUFlPX18zMzUiKSk='))
```
### Usage
1. Download everything onto your computer
2. Put the code you want to obfuscate into input.py
3. Run main.py
4. Get the obfuscated code in output.py
### How it works
There are 4 layers of protection:
1. Base64 - This is the first and least protective layer (can be decoded online). Exists only to confuse non-python/coding people
2. .replace - Replaces a unreadable string with letters to make it readable so it can be executed. Someone who knows python can decode this, but it takes some time, but it's harder to decode than base64. You can see this in template.py
3. Base85 - The code from the fourth layer is encoded in base85 to prevent code from breaking as well as to stop some python coders.
4. compile() - The fourth layer is basically un-decode-able. The code is made into binary and marshalled (so that it can be represented in text). There is no way to decode this as it is binary. The best applications packaged to this (think Chrome: did anyone get the source code of chrome? -NOT Chromeium)
### Bugs and future plans
I'm planning protecting the code from #3 (see above) with the .replace method (#2).
There might be bugs... Please open an issue... BUT make sure to run source code first to see if the source code works

## Make sure to star this repo!