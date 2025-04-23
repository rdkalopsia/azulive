
░█████╗░███████╗██╗░░░██╗██╗░░░░░██╗██╗░░░██╗███████╗
██╔══██╗╚════██║██║░░░██║██║░░░░░██║██║░░░██║██╔════╝
███████║░░███╔═╝██║░░░██║██║░░░░░██║╚██╗░██╔╝█████╗░░
██╔══██║██╔══╝░░██║░░░██║██║░░░░░██║░╚████╔╝░██╔══╝░░
██║░░██║███████╗╚██████╔╝███████╗██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝╚══════╝░╚═════╝░╚══════╝╚═╝░░░╚═╝░░░╚══════╝
      
AzuLive is a simple command-line tool written in Python that helps you
identify which domains or subdomains are active based on their HTTP status codes.

By default, it considers the following status codes as active:
200, 301, 302, 403, and 500. You can customize this list using arguments.

─────────────────────────────

✨ Features:
- Filter active domains from a list
- Customizable status codes
- Output results to a new file
- Colored terminal output (green/red)
- Ready for both beginner and advanced users

─────────────────────────────

🛠️ Usage:
python azulive.py -l <input_file> -o <output_file> [-i <status_codes>]

Example:
python azulive.py -l example.txt -o activesubdomain
python azulive.py -l example.txt -o activesubdomain -i 200 300 403

Arguments:
  -l, --list       Path to the file containing domains
  -o, --output     File to save active domains
  -i, --include    (Optional) Status codes to consider as active

─────────────────────────────

📁 Input File Format:
Each domain or subdomain should be written on a new line. For example:
example.com
sub.domain.com
https://anotherdomain.org

─────────────────────────────

🧑‍💻 Developer:
https://github.com/rdkalopsia
https://mebroccoli.blogspot.com

─────────────────────────────

⚠️ Notes:
- Requires internet connection.
- Works on Python 3.6+
- Ensure the input file does not contain blank lines.

─────────────────────────────

🎯 Future Plans (Coming Soon?):
- Add optional IP scanning mode
- Add timeout handling & error logging
- GUI version (maybe 😉)

─────────────────────────────

Stay crunchy, like broccoli 🥦
