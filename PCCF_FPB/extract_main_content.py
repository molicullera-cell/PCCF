import sys
from bs4 import BeautifulSoup

def extract_main_content(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Eliminar barres de navegació i menús laterals
    for tag in soup(["nav", "aside", "header", "footer"]):
        tag.decompose()

    # Buscar només el contingut principal
    main_content = soup.select_one("div.md-content article")

    if main_content:
        # 🔥 Evitar que Pandoc converteixi les taules a Markdown
        for table in main_content.find_all("table"):
            wrapper = soup.new_tag("div", attrs={"class": "keep-html"})
            table.wrap(wrapper)

        # Eliminar identificadors automàtics dels títols
        for header in main_content.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
            if header.has_attr("id"):
                del header["id"]

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(main_content))  # Guarda només el contingut filtrat sense ID

if __name__ == "__main__":
    input_html = sys.argv[1]
    output_html = sys.argv[2]
    extract_main_content(input_html, output_html)
