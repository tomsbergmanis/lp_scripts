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
            if len(element) <= 1:
                element = line.split("\t")
            if len(element) <= 1:
                continue
            if float(element[1]) > 1:
                distribution[element[0]] = float(element[1])
                counter += float(element[1])

        for e in distribution:
            distribution[e] = distribution[e] / counter
        self.distribution = distribution

    def getter(self, word):

        try:
            return self.distribution[word]
        except KeyError, e:
            #print 'KeyError on \"' + word +"\"\n"
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
            if len(element) <= 1:
                element = line.split("\t")
            if not element[0] in distribution:
                distribution[element[0]] = {}
            distribution[element[0]][element[1]] = float(element[2])
        self.distribution = distribution

    def getter(self, s_word, t_word):
        try:
            return self.distribution[s_word][t_word]
        except KeyError, e:
            return 0
    
            
class joint_probability(object):
    def __init__(self, cond_i_file, word_i_file):
        self.cond_prob = conditional_probability(cond_i_file)
        self.word_prob = word_probability(word_i_file)

    def getter(self, s_word, t_word):
        return self.cond_prob.getter(s_word, t_word) * self.word_prob.getter(t_word)

