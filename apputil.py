from collections import defaultdict


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None  # you'll need to build this

    def get_term_dict(self):
        # Tokenize corpus into words
        tokens = self.corpus.split()  # simple whitespace split
        
        # Initialize defaultdict of lists
        term_dict = defaultdict(list)

        # Build dictionary of transitions
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            next_word = tokens[i + 1]
            term_dict[current_word].append(next_word)

        # Convert defaultdict to a normal dict (optional)
        self.term_dict = dict(term_dict)
        return None
    
    def generate(self, seed_term=None, term_count=15):
        if self.term_dict is None:
            raise ValueError("You must call get_term_dict() first.")

        if seed_term:
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not found in corpus.")
            current_word = seed_term
        else:
            current_word = random.choice(list(self.term_dict.keys()))

        words = [current_word]

        for _ in range(term_count - 1):
            followers = self.term_dict.get(current_word, [])
            if not followers:
                break
            next_word = np.random.choice(followers)
            words.append(next_word)
            current_word = next_word

        # THIS is what should make it return text instead of None
        return ' '.join(words)
        