from jinja2 import Environment, FileSystemLoader

class JingaExample:

    def suite(self):
        name = 'Peter'
        age = 34

        tm = Template("My name is {{ name }} and I am {{ age }}")
        msg = tm.render(name=name, age=age)

        print(msg)

    def use_file(self):
        persons = [
            {'name': 'Andrej', 'age': 34},
            {'name': 'Mark', 'age': 17},
            {'name': 'Thomas', 'age': 44},
            {'name': 'Lucy', 'age': 14},
            {'name': 'Robert', 'age': 23},
            {'name': 'Dragomir', 'age': 54}
        ]

        file_loader = FileSystemLoader('templates')
        env = Environment(loader=file_loader)

        template = env.get_template('showpersons.txt')

        output = template.render(persons=persons)
        print(output)




if __name__ == "__main__":
    jingaExample = JingaExample()
    jingaExample.use_file()