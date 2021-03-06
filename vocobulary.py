class voc(object):
    def __init__(self, ifile, string):

        with open(ifile, 'r') as f:
            file_content = f.read()

        lines = file_content.split("\n")
        voc = {}
        inv_voc = {}
        i = 0
        for line in lines:
            print line            
            if line == "":
                print "tuksa linija"
                continue
            element = line.split(" ")
            if len(element) <= 1:
                print "ar speisu nesanaca"
                element = line.split("\t")
            if int(element[1]) > 0:
                i += 1
                var_name = string+str(i)
                voc[element[0]] = var_name
                inv_voc[var_name] = element[0]

        self.i = i
        self.string = string
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

    def append(self, ifile):

        with open(ifile, 'r') as f:
            file_content = f.read()

        lines = file_content.split("\n")
        voc = self.voc
        inv_voc = self.inv_voc
        string = self.string
        i = self.i
        for line in lines:
            i += 1
            if line == "":
                continue
            element = line.split(" ")
            if len(element) <= 1:
                element = line.split("\t")
            if element[0] in voc:
                continue
            var_name = string+str(i)
            voc[element[0]] = var_name
            inv_voc[var_name] = element[0]

        self.i = i
        self.voc = voc
        self.inv_voc = inv_voc

    def voc_items(self):
        return self.voc.iteritems()
        
    def inv_voc_items(self):
        return self.inv_voc.iteritems()
