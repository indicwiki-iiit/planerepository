
from jinja2 import Environment, FileSystemLoader
class RenderData:
    def render(self, dictionary, glob):
        file_loader = FileSystemLoader('./')
        env = Environment(loader=file_loader)
        template = env.get_template('./templates/data.j2')
        if 'Crew' in dictionary:
            glob['crew']= dictionary['Crew']

        variantsExists = False
        variants = []
        if 'Variants' in dictionary:
            dat = dictionary['Variants']
            print('data' ,dat, type(dat))
            my_list = []
            if type(dat) == str:
                my_list = dat.split(",")
            else:
                data = eval(dat)
                for variant in data:
                    print('Variants', variant)
                    my_list.append(variant)

            if len(my_list) > 0 :
                variantsExists = True

            glob['variants'] = my_list
            glob['variantsExists'] = variantsExists

        if 'Maximum speed' in dictionary:
            glob['maximumSpeed']= dictionary['Maximum speed']
        if 'Cruise speed' in dictionary:
            glob['cruiseSpeed']= dictionary['Cruise speed']
        if 'Length' in dictionary:
            glob['length']= dictionary['Length']
        if 'Height' in dictionary:
            glob['height']= dictionary['Height']
        if 'Wingspan' in dictionary:
            glob['wingspan']= dictionary['Wingspan']
        if 'Wing area' in dictionary:
            glob['wingarea']= dictionary['Wing area']
        if 'Gross weight' in dictionary:
            glob['grossweight']= dictionary['Gross weight']
        if 'Empty weight' in dictionary:
            glob['emptyweight']= dictionary['Empty weight']
        return template.render(glob), glob


if __name__ == "__main__":
    renderData = RenderData()
    renderData.render()