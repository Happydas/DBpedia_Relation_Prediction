import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim, re
class Word2VecDBpedia():
    def saveWord(self, lines):
        f1 = open("Spouse_filteredWords.txt", 'w', encoding="utf-8")
        for line in lines:
            f1.write(line + '\n')

    def loadFiles(self):
        f1 = open("Spouse_filteredWords.txt", 'w', encoding="utf-8")
        model = gensim.models.KeyedVectors.load_word2vec_format(
            'D:/dl4j-files/GoogleNews-vectors-negative300.bin/GoogleNews-vectors-negative300.bin', binary=True)

        f = open("Spouse_output.txt", 'r', encoding="utf-8")
        lines = f.readlines()
        linesNew = []
        #for line in lines.split('\n'):
        for line in lines:
            Type = line.split("    ")
            if len(Type)> 1:
                print(Type[0], Type[1])
            if Type[0] in model.vocab and Type[1] in model.vocab:
                f1.write(Type[0]+" "+Type[1]+"\n")

            #line = re.sub(' +', ' ', line)
            #for word in Type:
            '''  
              print(word)
                if word in model.vocab:
                  print("Vocab ", word)
                  f1.write(word+"\n")
                  linesNew.append(Type)
                  '''
        #self.saveWord(linesNew)



w = Word2VecDBpedia()
w.loadFiles()
