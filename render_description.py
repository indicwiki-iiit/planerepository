import pandas as pd
import math
import ast
from jinja2 import Environment, FileSystemLoader

class RenderDescription:
    def render_desc(self, dictionary, glob):
        file_loader = FileSystemLoader('./')
        env = Environment(loader=file_loader)
        template = env.get_template('./templates/description.j2')
        return template.render(glob), glob

if __name__ == "__main__":
    renderDescription = RenderDescription()
