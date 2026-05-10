from mrjob.job import MRJob

class WordCount(MRJob):

    def mapper(self, _, line):
        words = line.strip().split()

        for word in words:
            word = word.lower().strip('.,!?";:')

            if word:
                yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    WordCount.run()