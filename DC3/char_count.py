from mrjob.job import MRJob

class CharacterCount(MRJob):

    def mapper(self, _, line):
        for char in line:
            if char != ' ':  # skip spaces (remove this line to count spaces too)
                yield char.lower(), 1

    def reducer(self, char, counts):
        yield char, sum(counts)

if __name__ == '__main__':
    CharacterCount.run()