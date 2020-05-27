# <!-- // Code Author:-
# // Name: Shivam Gupta
# // Net ID: SXG190040
# // Information Retrieval (CS 6322.001) Assignment 3 (Relevance Model) -->

import glob
import os
import re
import math
import sys
import time
from datetime import datetime
import pprint
from collections import Counter
from collections import OrderedDict
from bs4 import BeautifulSoup
import nltk
nltk.download("wordnet")
nltk.download("punkt")
from nltk.stem import WordNetLemmatizer
from nltk import PorterStemmer




cran_doc_paths ="/people/cs/s/sanda/cs6322/Cranfield/*"
# cran_doc_paths = r"Cranfield/*"
cran_doc_pathname = os.path.join(cran_doc_paths)
cranfield_files=sorted(glob.glob(cran_doc_pathname))
queries_file = "/people/cs/s/sanda/cs6322/hw3.queries"
# queries_file = r"hw3.queries"
stopwords = []
stopword_file = r"/people/cs/s/sanda/cs6322/resourcesIR/stopwords"
# stopword_file = r"stopwords"
file_stop_words = open(stopword_file, "r")
for word in file_stop_words:
    stopwords.append(word.strip("\n"))
file_stop_words.close() 


# function for preprocessing the documents
def preprocess(words):
    doc = re.sub(r'<.*?>',"", words)   # Removes SGML Tags
    doc = re.sub(r'[,-]'," ", doc)     # Removes comma and hyphen, replaces with space
    doc1 = re.sub(r'[^\w\s]','',doc)    # Removes punctuation marks
    result=doc1.lower()                    # Lower-case the tokens
    return result

def preprocess_documents(text):
    result = text.replace(".","").replace(":","").replace("/","").replace("'","").replace(";","").replace("(","").replace(")","").replace("*","").replace("+","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("0","").replace("+","").replace("=","").strip(" ").lower()
    return result

# Function for creating a dictionary for every Query
def extract_queries(file):
    query_file = open(file, "r").read()	
    text = re.split("Q[0-9]+:\r\n",query_file)
    queries = {key : value.replace("\r\n"," ").strip() for key, value in enumerate(text) if value != ""}
    return queries

# Function for getting lemmatized tokens for the queries 
def extract_tokens_queries(queries, stopwords):
    wordNet_Lemmatizer = WordNetLemmatizer()

    for index, query in queries.items():
    
        
        result = preprocess(query)
        tokens=result.split()
        tokens = [t for t in tokens]

        query_tokens = []

        for word in tokens:
            if word not in stopwords and word != "":
                query_tokens.append(wordNet_Lemmatizer.lemmatize(word))

        queries[index] = query_tokens

    return queries



# Function for getting the information like tokens, doc IDs and titles
def extract_cranfield_info(files):

    tokens_docs = []   # It stores tokens for all the  cranfield files
    document_IDs = []
    titles = {}
    for i in range(len(files)):
        cran_file = open(files[i], "r")
    
        doc_text = cran_file.read()
        doc_soup = BeautifulSoup(doc_text,"html.parser")
        title = doc_soup.find_all('title')[0].string
        titles.update({i+1 : title.replace("\n", " ").strip()})
        
        doc_no = doc_soup.find_all('docno')
        document_IDs.append(int(doc_no[0].string))
        text = doc_soup.findAll('text')   
        text_info = text[0].string      
        

        tokens = []
        for text in text_info.split("\n"):
            tokens.extend([ preprocess_documents(i) for i in text.replace("-"," ").replace(","," ").split(" ")])
        
        # Append the file tokens discarding all the empty characters in the list  
        tokens_docs.append([t for t in tokens if t!=""])    
    return tokens_docs, document_IDs, titles


# Function for generating dictionary for the documents
def create_doc_dict(lemmas, stopwords_list):
    document_dict = {}
    for l in range(len(lemmas)):
        most_common, num_most_common = Counter([a for a in lemmas[l] if a not in stopwords_list]).most_common(1)[0]
        document_dict.update({ l+1 : {"total_terms": len(lemmas[l]), "most_common": most_common, "num_most_common" : num_most_common, "document_length" : len(lemmas[l]) }})

    return document_dict

# Function for initializing ordered postings for the documents by removing stopwords
def get_postings_dict(lemmas, stopwords_list):
    postings_dict = {}
    for lemma in lemmas:
        for l in lemma:
            if l not in stopwords_list:
                if l not in postings_dict.keys():
                    postings_dict[l] = {"posting_list": {}, "term_freq": 0, "document_freq" : 0 }
    return OrderedDict(sorted(postings_dict.items()))

# Function for generating ordered postings for the documents    
def create_Postings(lemmas, postings_dict, Doc_IDs, stopwords_list, documents_dict):	

    for i in range(len(lemmas)):
        for x in lemmas[i]:
            if x not in stopwords_list:
                postings_dict[x]["posting_list"].update({ Doc_IDs[i] : { "term_freq": lemmas[i].count(x), "most_common_term_freq" : lemmas[i].count(documents_dict[i+1]["most_common"]) , "document_length" : documents_dict[i+1]["total_terms"], "most_common" : documents_dict[i+1]["most_common"] }})
                
    for d in postings_dict.keys():
        doc_freq = len(postings_dict[d]["posting_list"].keys())
        total_count = 0
        for i in postings_dict[d]["posting_list"].keys():
            total_count += postings_dict[d]["posting_list"][i]["term_freq"]
        postings_dict[d]["term_freq"] = total_count
        postings_dict[d]["document_freq"] = doc_freq

    return OrderedDict(sorted(postings_dict.items()))


# Function for getting the postings and documents dictionary by calling above functions
def get_postings_documents_dict(lemmas, Doc_IDs, stopwords_list, file_name, f):
    document_dict = create_doc_dict(lemmas,stopwords_list)
#     print("==========doc===================", doc)
    posting = get_postings_dict(lemmas, stopwords_list)
#     print("==========posting================", posting)
    Posting_dict = create_Postings(lemmas, posting, Doc_IDs, stopwords_list, document_dict)
#     print("==========create_Postings===============", posting)
    if f == "lemma":
        pass
        #uncompressed_posting_file(posting, file_name+".uncompress")
    return Posting_dict, document_dict

# Function for lemmatizing the tokens in the documents
def lemmatize_tokens(tokens):
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmas = []
    for i in range(len(tokens)):
        count = 0
        lem = []
        for ind in range(len(tokens[i])):
            lem.append(wordnet_lemmatizer.lemmatize(tokens[i][ind]))
        lemmas.append(lem)	
        count += 1
    return lemmas



# Function for generating the dictionary of the queries for storing terms information
def calculate_docfreq_query(query_dict):
    doc_freq_query_dict = {}
    for q in query_dict.keys():
        q_dic = {}
        query_data = Counter(query_dict[q])
        for q_value in query_dict[q]:
            count = 0
            for V in query_dict.values():
                if q_value in V:
                    count += 1
            term_freq = query_data[q_value]
            q_dic.update({q_value : {"document_freq" : count,
                                    "tf" : term_freq,
                                    "collectionsize": len(query_dict),
                                    "document_length" : len(query_dict[q]),
                                    "max_term_freq": query_data.most_common()[0][1]}})
        doc_freq_query_dict[q] = q_dic                
    return doc_freq_query_dict

# Function for calculating the weights(both versions)
def calculate_weights(tokenized_queries, posting_dict, lemma_result, document_dict, queries_doc_freq):
    cranfield_collection_size = 1400
    total_queries = len(tokenized_queries)
    # len_func = lambda x :  len(x)
    mean_doc_len = sum([len(x) for x in lemma_result]) / cranfield_collection_size
    query_mean_doclen = sum([len(x) for x in tokenized_queries.values()]) / total_queries
#     print("mean_doc_len, query_mean_doclen", mean_doc_len, query_mean_doclen)
    ranking = {}
    queries_vector = {}
    
    for key in tokenized_queries.keys():    
        weights_dict = {"weight1": {}, "weight2": {}}
        queries_vector.update({key : {}}) 
        wt = {"weight1" : {}, "weight2" : {}}   
        for query_tokens in tokenized_queries[key]: 
            if query_tokens in posting_dict.keys():
                
                term_freq = queries_doc_freq[key][query_tokens]["tf"]
                doc_freq = queries_doc_freq[key][query_tokens]["document_freq"]
                max_term_freq = queries_doc_freq[key][query_tokens]["max_term_freq"]
                doc_length =  queries_doc_freq[key][query_tokens]["document_length"]
                cs = queries_doc_freq[key][query_tokens]["collectionsize"]
                # print("------------------doc_freq, cs-----------", doc_freq, cs)
                weights1_query = (0.4 + 0.6 * math.log10(term_freq + 0.5) / math.log10(max_term_freq + 1.0)) * (math.log10(cs / doc_freq) / math.log10(cs))
                weights2_query = (0.4 + 0.6 * (term_freq / (term_freq + 0.5 + 1.5 * (doc_length / query_mean_doclen))) * math.log10(cs / doc_freq)/ math.log10(cs)) 
                wt["weight1"].update({query_tokens : weights1_query/doc_length })
                wt["weight2"].update({query_tokens : weights2_query/doc_length })

                for doc_no in posting_dict[query_tokens]["posting_list"].keys():
                    if doc_no not in weights_dict["weight1"].keys():
                        weights_dict["weight1"].update({doc_no: 0})
                        weights_dict["weight2"].update({doc_no: 0})
                    term_freq = posting_dict[query_tokens]["term_freq"]
                    doc_freq = posting_dict[query_tokens]["document_freq"]
                    max_term_freq = posting_dict[query_tokens]["posting_list"][doc_no]["most_common_term_freq"]
                    doc_length = document_dict[doc_no]["document_length"]
                    weights1_doc = (0.4 + 0.6 * math.log10(term_freq + 0.5) / math.log10(max_term_freq + 1.0)) * (math.log10(cranfield_collection_size / doc_freq) / math.log10(cranfield_collection_size)) 
                    weights2_doc = (0.4 + 0.6 * (term_freq / (term_freq + 0.5 + 1.5 * (doc_length / mean_doc_len))) * math.log10(cranfield_collection_size / doc_freq)/ math.log10(cranfield_collection_size))
                    
                    #  Calculating the cosine similarity
                    weight1 = (weights1_doc * weights1_query) / doc_length
                    weight2 = (weights2_doc * weights2_query) / doc_length
                    
                    weights_dict["weight1"][doc_no] += weight1
                    weights_dict["weight2"][doc_no] += weight2        
        ranking.update({key : weights_dict})
        queries_vector[key].update({"weight1": wt["weight1"], "weight2": wt["weight2"]})
        
    return ranking, queries_vector  

# Function for calculating the Documents weights Vector representation
def calculate_document_vetor_representation(Doc_ID, posting_dict, cranfield_collection_size, mean_doc_len, weight_scheme):
    
    Dict_Weight_Vector = {}
    for words, postings_list in posting_dict.items():
        # count+=1
        if Doc_ID in list(postings_list["posting_list"].keys()):
            DID = postings_list["posting_list"].keys()
            doc_freq = len(postings_list["posting_list"])
            term_freq = postings_list["posting_list"][Doc_ID]['term_freq']
            max_term_freq = postings_list["posting_list"][Doc_ID]['most_common_term_freq']
            doc_length =  postings_list["posting_list"][Doc_ID]['document_length']
            if weight_scheme == "S1":
                weights_doc = (0.4 + 0.6 * math.log10(term_freq + 0.5) / math.log10(max_term_freq + 1.0)) * (math.log10(cranfield_collection_size / doc_freq) / math.log10(cranfield_collection_size)) 
            elif weight_scheme == "S2":
                weights_doc = (0.4 + 0.6 * (term_freq / (term_freq + 0.5 + 1.5 * (doc_length / mean_doc_len))) * math.log10(cranfield_collection_size / doc_freq)/ math.log10(cranfield_collection_size))
            Dict_Weight_Vector[words] = weights_doc

    return Dict_Weight_Vector

start_time_rel_model =datetime.now()
docs_tokens, Document_IDs, titles = extract_cranfield_info(cranfield_files)

lemma_result = lemmatize_tokens(docs_tokens)
posting_dict, document_dict = get_postings_documents_dict(lemma_result, Document_IDs, stopwords, "Index_Version1", "lemma")

query_dict = extract_queries(queries_file)
# print("-------   query_dict  -------",query_dict)
query_dict
tokenized_queries = extract_tokens_queries(query_dict ,stopwords)
# tokenized_queries
queries_doc_freq = calculate_docfreq_query(tokenized_queries)
# queries_doc_freq

rankings, queries_vector = calculate_weights(tokenized_queries, posting_dict, lemma_result, document_dict, queries_doc_freq)
# print(rankings)
# print("=======================================================================")
# print(queries_vector)

# for i, j in tokenized_queries.items():
#     print(i, j)

print("A Statistical Relevance model in retrieval system based on the vector relevance model:")
cranfield_collection_size = 1400
mean_doc_len = sum([len(x) for x in lemma_result]) / cranfield_collection_size
print("\n")
for query_rank in rankings.keys():
    q_rank_wt1 = rankings[query_rank]["weight1"]
    top5_wt1 = sorted(q_rank_wt1.items(), key=lambda lam: lam[1])[-5: ][:: -1]
    print("Query No: %d" %query_rank)
    print("\nQuery Vector for weight (Version 1) are: ")
    pprint.pprint(sorted(queries_vector[query_rank]["weight1"].items()))
    print("\nQuery Vector for weight (Version 2) are: ")
    pprint.pprint(sorted(queries_vector[query_rank]["weight2"].items()))
    print("\nRanks ", "Document Number ", " Scores",                                "Titles")
    print("\n")
    count = 0
    for values in top5_wt1:
        # print(values[0], end=', ')
        count += 1
        print(count, "   ", values[0], "     ", values[1], " ", titles[values[0]])
        Dict_Weight_Vector = calculate_document_vetor_representation(values[0], posting_dict, cranfield_collection_size, mean_doc_len, "S1")
        print("\n")
        print("Vector Representation for the Rank", count, "With Document ID", values[0] )
        print("\n")
        print(Dict_Weight_Vector)
        print("="*70)
    print("\n")
    q_rank_wt2 = rankings[query_rank]["weight2"]
    top5_wt2 = sorted(q_rank_wt2.items(), key=lambda lam: lam[1])[-5: ][:: -1]
    print("Rankings ", "Doc No ", " Score",                                          "Titles")
    print("="*168)
    count = 0
    for values in top5_wt2:
        # print(values[0], end=', ')
        count += 1
        print(count, "   ", values[0], "     ", values[1], " ", titles[values[0]])
        Dict_Weight_Vector = calculate_document_vetor_representation(values[0], posting_dict, cranfield_collection_size, mean_doc_len, "S2")
        print("\n")
        print("Vector Representation for the Rank", count, "With Document ID", values[0] )
        print("\n")
        print(Dict_Weight_Vector)
        print("="*70)
    print("="*168)
    print("\n")

end_time_rel_model =datetime.now()
print("Time (in sec) to build Relevance Model is: ",str(end_time_rel_model-start_time_rel_model).split(":")[-1], "seconds")