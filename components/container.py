from vars import vars
class Container:
    see_contents = True
    open = True
    def __init__(self, name, synonyms, description, contents, **kwargs):
        self.name = name
        self.synonyms = synonyms
        self.description = description
        self.contents = contents

    def fetch_contents(self):            
        x = []
        for i in self.contents:
            for j in vars.objects:
                if i == j:
                    x.append(vars.objects[i].description)
        if len(x) > 1:
            y = '{} and {}'.format(', '.join(x[:-1]), x[-1])
        else:
            y = x[0]
        return y