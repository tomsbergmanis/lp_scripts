import distributions as D
import vocobulary as V

class wrapper(object):
    def __init__(self, corp_t_voc_file, corp_s_voc_file, corp_lex_file_t2s, wiki_t_file, wiki_s_file, t_str, s_str):
        self.JD = D.joint_probability(corp_lex_file_t2s, corp_t_voc_file) 
        self.MD_S = D.word_probability(wiki_s_file)
        self.MD_T = D.word_probability(wiki_t_file)
        
        self.V_S = V.voc(corp_s_voc_file, s_str)
        self.V_S.append(wiki_s_file)
        
        self.V_T = V.voc(corp_t_voc_file, t_str)
        self.V_T.append(wiki_t_file)
        
#("../data/en_unigrams", "../data/lv_unigrams", "../data/lex.e2f", "../data/wiki_eng_unigrams","../data/wiki_lv_unigrams", "t", "s" )

