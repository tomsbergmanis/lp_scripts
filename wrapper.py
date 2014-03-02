import sys
import distributions as D
import vocobulary as V
import os

# a = w.wrapper("../data/en_unigrams", "../data/lv_unigrams", "../data/lex.e2f", "../data/wiki_eng_unigrams","../data/wiki_lv_unigrams", "t", "s" )

class wrapper(object):
    def __init__(self, corp_t_voc_file, corp_s_voc_file, corp_lex_file_t2s, wiki_t_file, wiki_s_file, t_str, s_str, out_file):
        self.JD = D.joint_probability(corp_lex_file_t2s, corp_t_voc_file)
        self.MD_S = D.word_probability(wiki_s_file)
        self.MD_T = D.word_probability(wiki_t_file)

        self.V_S = V.voc(wiki_s_file, s_str)
        self.V_T = V.voc(wiki_t_file, t_str)
        self.s_str = s_str
        self.t_str = t_str
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
                o.flush()
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
                o.flush()



    def create_t_m(self):
        s_vs = self.V_S.voc_items()
        t_vs = self.V_T.voc_items()
        with open(self.out_file, "a") as o:
            for tw, tv in self.V_T.voc_items():
                a = ""
                for sw, sv in self.V_S.voc_items():
                    a += sv + tv + "+"
                a += "0 =" + str(self.MD_T.getter(tw))+";"
                o.write(a+"\n")
                o.flush()

    def unwrap(self, wfile):
        f = open(wfile, "r")
        fst = f.read()
        vlist = fst.split("\n")
        o = open(wfile+"_UW", "w")
        for vl in vlist:
            vel = vl.split(" ")
            vn = vel[0]

            if len(vn) <1 or not vn[0] ==  'x':
                continue
            else:
                words = self.get_words(vn[1:])
                o.write(words[1] + " " + words[0] + " " + vel[-1])

    def get_words(self,s):         #xs68t10
       varl = s.split(self.t_str)
       tvar = self.t_str + varl[-1]
       svar = self.s_str+ varl[0][1:]
       tword = self.V_T.getter(tvar)
       sword = self.V_S.getter(svar)
       return (tword, sword)


if __name__ == "__main__":
    print "Wrpapping..."
    a = wrapper("/home/toms/lp/data/en_unigrams", "/home/toms/lp/data/lv_unigrams", "/home/toms/lp/data/lex.e2f", sys.argv[1], sys.argv[2], "t", "s", sys.argv[3])
    a.create_objective()
    a.create_s_m()
    a.create_t_m()
    a.create_of_c()
    print "Wrpapping is done."
    print "Solving LP..."
    os.system("/home/toms/lp/./lp_solve " + sys.argv[3] + "> " + sys.argv[3]+"_out")
    print "Done with LP"
    a.unwrap(sys.argv[3]+"_out")

