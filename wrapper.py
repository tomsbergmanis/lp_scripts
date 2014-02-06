import distributions as D
import vocobulary as V
import gzip as G

# a = w.wrapper("../data/en_unigrams", "../data/lv_unigrams", "../data/lex.e2f", "../data/wiki_eng_unigrams","../data/wiki_lv_unigrams", "t", "s" )


class wrapper(object):
    def __init__(self, corp_t_voc_file, corp_s_voc_file, corp_lex_file_t2s, wiki_t_file, wiki_s_file, t_str, s_str, out_file):
        self.JD = D.joint_probability(corp_lex_file_t2s, corp_t_voc_file) 
        self.MD_S = D.word_probability(wiki_s_file)
        self.MD_T = D.word_probability(wiki_t_file)
        
        self.V_S = V.voc(corp_s_voc_file, s_str)
        self.V_S.append(wiki_s_file)
        
        self.V_T = V.voc(corp_t_voc_file, t_str)
        self.V_T.append(wiki_t_file)
        self.out_file = out_file
      
    
    def create_objective(self):
        s_vs = self.V_S.voc_items()
        t_vs = self.V_T.voc_items()
        with open(self.out_file, "a") as o:
            c = "min: "
            for sw, sv in self.V_S.voc_items():
                for tw, tv in self.V_T.voc_items():
                    c  += "x" + sv + tv +"+"
            c += "0;\n"
            o.write(c)
                
    def create_of_c(self):
        s_vs = self.V_S.voc_items()
        t_vs = self.V_T.voc_items()
        with open(self.out_file, "a") as o:
            c4 = ""
            for sw, sv in self.V_S.voc_items():
                for tw, tv in self.V_T.voc_items():
                    old_jp = self.JD.getter(sw, tw)
                    c1 = sv + tv + "-" + str(old_jp) + "<=x" + sv + tv + ";\n"
                    c2 = "-" + sv + tv + "+" + str(old_jp) + "<=x" + sv + tv + ";\n"
                    c3 = sv + tv +">=0;\n"
                    o.write(c1)
                    o.write(c2)
                    o.write(c3)
                    c4 += sv + tv + "+"
            c4 += "0=1;\n"
            o.write(c4)
                
    def create_s_m(self):
        s_vs = self.V_S.voc_items()
        t_vs = self.V_T.voc_items()
        with open(self.out_file, "a") as o:
            for sw, sv in self.V_S.voc_items():
                a = ""
                for tw, tv in self.V_T.voc_items():
                    a += sv + tv + "+"
                a += "0 =" + str(self.MD_S.getter(sw))+";"
                o.write(a+"\n")

                
    def create_t_m(self):
        s_vs = self.V_S.voc_items()
        t_vs = self.V_T.voc_items()
        with open(self.out_file, "a") as o:
            for tw, tv in self.V_T.voc_items():
                a = ""
                for sw, sv in self.V_S.voc_items():
                    a += sv + tv + "+"
                a += "0 =" + str(self.MD_T.getter(sw))+";"
                o.write(a+"\n")

            
if __name__ == "__main__":
    a = wrapper("../data/en_unigrams", "../data/lv_unigrams", "../data/lex.e2f", "../data/wiki_eng_unigrams","../data/wiki_lv_unigrams", "t", "s", "out" )
    a.create_objective()
    a.create_s_m()
    a.create_t_m()
    a.create_of_c()
    
    
