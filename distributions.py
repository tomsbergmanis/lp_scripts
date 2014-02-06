

class word_probability(object):
    def __init__(self, ifile):
        
        with open(ifile, 'r') as f:
            file_content = f.read()
            
        lines = file_content.split("\n")
        distribution = {}
        counter = 0
        for line in lines:
            if line == "":
                continue
            element = line.split(" ")
            distribution[element[0]] = float(element[1])
            counter += float(element[1])
            
        for e in distribution:
            distribution[e] = distribution[e] / counter
            
        self.distribution = distribution 
        
    def getter(self, word):

        try:
            return self.distribution[word]
        except KeyError, e:
            print 'KeyError on \"' + word +"\"\n"
            return 0
        
class conditional_probability(object):
    def __init__(self, ifile):
        with open(ifile, 'r') as f:
            file_content = f.read()
            
        lines = file_content.split("\n")
        distribution = {}
        counter = 0
        for line in lines:
            if line == "":
                continue
            element = line.split(" ")
            if not element[0] in distribution:
                distribution[element[0]] = {}
            distribution[element[0]][element[1]] = float(element[2])
        self.distribution = distribution 
        
    def getter(self, s_word, t_word):
        try:
            return self.distribution[s_word][t_word]
        except KeyError, e:
            print 'KeyError on \"' + s_word +" "+ t_word +"\"\n"
            return 0
