
from jinja2 import Environment, FileSystemLoader
class RenderData:
    def render(self, dictionary, glob):
        file_loader = FileSystemLoader('./')
        env = Environment(loader=file_loader)
        template = env.get_template('./templates/data.j2')
        glob['crew']= dictionary['Crew']
        variantsExists = False
        variants = []
        if 'Variants' in dictionary:
            data = eval(dictionary['Variants'])
            print('data' ,data, type(data))
            my_list = []
            if type(data) == str:
                my_list = data.split(",")
            else:
                for variant in data:
                    print('Variants', variant)
                    my_list.append(variant)

            if len(my_list) > 0 :
                variantsExists = True

        glob['variants'] = my_list
        glob['variantsExists'] = variantsExists
        glob['maximumSpeed']= dictionary['Maximum speed']
        glob['cruiseSpeed']= dictionary['Cruise speed']
        glob['length']= dictionary['Length']
        glob['height']= dictionary['Height']
        glob['wingspan']= dictionary['Wingspan']
        glob['wingarea']= dictionary['Wing area']
        glob['grossweight']= dictionary['Gross weight']
        glob['emptyweight']= dictionary['Empty weight']
        return template.render(glob), glob


if __name__ == "__main__":
    renderData = RenderData()
    renderData.render()