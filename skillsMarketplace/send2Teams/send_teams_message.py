import argparse
import json
import os
import sys
import urllib.request
from teams_payload_builders import build_basic_card

def load_config():
    config_path = os.path.join(
        os.path.dirname(__file__),
        "config.json"
    )
    if not os.path.exists(config_path):
        print(json.dumps({"ok": False, "error": "config.json no encontrado"}))
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alias", required=True)
    parser.add_argument("--title", required=False)
    parser.add_argument("--message", required=True)
    parser.add_argument("--fact", action="append")
    parser.add_argument("--button", action="append")
    parser.add_argument("--color", default="0078D7")

    args = parser.parse_args()

    title = args.title if args.title else "Notificación automática"

    if args.message:
        args.message = args.message.replace("\\n", "\n")

    config = load_config()

    if args.alias not in config.get("aliases", {}):
        print(json.dumps({"ok": False, "error": "Alias no configurado"}))
        sys.exit(1)

    webhook_url = config["aliases"][args.alias]["webhook_url"]

    payload = build_basic_card(
        title=title,
        message=args.message,
        facts=args.fact,
        buttons=args.button,
        color=args.color
    )

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        webhook_url,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(req) as response:
            response.read()
        print(json.dumps({"ok": True, "messages_sent": 1}))
    except Exception as e:
        print(json.dumps({"ok": False, "error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
