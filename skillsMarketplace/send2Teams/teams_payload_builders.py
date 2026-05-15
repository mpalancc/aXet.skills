import json

def build_basic_card(title, message, facts=None, buttons=None, color="0078D7"):
    sections = []

    if facts:
        fact_list = []
        for f in facts:
            key, value = f.split("=", 1)
            fact_list.append({"name": key, "value": value})
        sections.append({"facts": fact_list})

    if message:
        sections.insert(0, {"text": message})

    card = {
        "@type": "MessageCard",
        "@context": "https://schema.org/extensions",
        "themeColor": color,
        "summary": title,
        "title": title,
        "sections": sections
    }

    if buttons:
        actions = []
        for b in buttons:
            text, url = b.split("=", 1)
            actions.append({
                "@type": "OpenUri",
                "name": text,
                "targets": [{"os": "default", "uri": url}]
            })
        card["potentialAction"] = actions

    return card
