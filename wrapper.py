import distributions as D
import vocoburlary as V

class wrapper(object):
    def __init__(self, corp_t_voc_file, corp_s_voc_file, corp_lex_file_t2s, wiki_t_file, wiki_s_file, t_str, s_str):
        JD = D.joint_probability(corp_lex_file_t2s, corp_t_voc_file) 
        MD_S = D.word_probability(wiki_s_file)
        MD_T = D.word_probability(wiki_T_file)
        
        V_S = V.voc(corp_s_voc_file, s_str)
        V_S.append(wiki_s_file)
        
        V_T = V.voc(corp_t_voc_file, t_str)
        V_T.append(wiki_t_file)
