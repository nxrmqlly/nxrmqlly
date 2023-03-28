import re
import pathlib
from datetime import date

root = pathlib.Path(__file__).parent.resolve()
readme_file = root / "README.md"


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def replace_chunk(content, marker, chunk, inline=False):
    r = re.compile(
        r"<!\-\- {} starts \-\->.*<!\-\- {} ends \-\->".format(marker, marker),
        re.DOTALL,
    )
    if not inline:
        chunk = f"\n{chunk}\n"
    chunk = f"<!-- {marker} starts -->{chunk}<!-- {marker} ends -->"
    return r.sub(chunk, content)


if __name__ == "__main__":
    readme = readme_file.open("r", encoding="utf-8").read()

    # Update Age
    age = replace_chunk(readme, "age", calculate_age(date(2009, 10, 31)), inline=True)
    readme_file.open("w", encoding="utf-8").write(age)
