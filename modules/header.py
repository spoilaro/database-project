from art import text2art

def render_header() -> None:
    app_name = """Fun Tracker"""

    header = text2art(app_name)
    print(header)
