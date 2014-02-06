class voc(object):
    def __init__(self, ifile, string):
        
        with open(ifile, 'r') as f:
            file_content = f.read()
            
        lines = file_content.split("\n")
        voc = {}
        inv_voc = {}
        i = 1
        for line in lines:
            if line == "":
                continue
            element = line.split(" ")
            var_name = string+str(i)
            voc[element[0]] = var_name
            inv_voc[var_name] = element[0]
            i += 1
            
        self.voc = voc
        self.inv_voc = inv_voc
        
    def getter(self, word):

        try:
            return self.voc[word]
        except KeyError, e:
            try:
                return self.inv_voc[word]
            except KeyError, e:
                return ""
