try:
    import requests
    import argparse

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--url", action="store")
    parser.add_argument("--out", action="store")
    args, unknown = parser.parse_known_args()
    if unknown:
        print("""Usage:\n\tcurlS --url https://example.com --out 'C:\\example'""")
        print("Error: Unknown argument(s): {}".format(unknown))
        exit()
    else:
        if args.url and args.out:
            req = requests.get(args.url, timeout=30)
            text = req.text
            with open(args.out, "w+") as f:
                f.write(text)
            print("made by: Request Timeout(GitHub: https://github.com/RequestTimeout)")
        else:
            print("""Usage:\n\tcurlS --url https://example.com --out 'C:\\example'""")
            print("Error: Please enter the needed argument(s)")
            exit()
except requests.exceptions.Timeout:
    print("Error: Request timed out. Please check your internet connection and try again.")
except requests.exceptions.ConnectionError:
    print("Error: Connection error. Please check your internet connection and try again.")
except requests.exceptions.InvalidURL:
    print("Error: Invalid URL.")
except Exception as e:
    print("Unknown error: {}".format(e))
