from collections import defaultdict
import random
import numpy as np
import pandas as pd

class MarkovText(object):

    def __init__(self, corpus):
        """
        This function initializes the later functions

        Args:
            corpus (str): A string containing the text corpus that we build the chain with

        Returns:
            None
        """
        self.corpus = corpus
        self.term_dict = None  

    def get_term_dict(self):
        """
        This function builds the Markov transition dictionary from corpus.
        The dictionary keys are unique tokens in the corpus, and each value
        is a list of words that directly follow the key in the corpus.
        This function updates the instance variable self.term_dict

        Args:
            None

        Returns:
            None
        """
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
        """
        Generate text using the Markov property based on the term dictionary.

        Args:
            seed_term (str, optional): The starting word for generation.
                                       If None, a random word is chosen
                                       from the term dictionary. Defaults to None.
            term_count (int, optional): Number of words to generate. Defaults to 15.

        Raises:
            ValueError: If `get_term_dict()` has not been called first.
            ValueError: If `seed_term` is provided but not found in the corpus.

        Returns:
            str: A string of generated text containing `term_count` words
                 or fewer if the last word has no followers in the corpus.
        """

        # Error if get_term_dict() hasn't been called yet
        if self.term_dict is None:
            raise ValueError("You must call get_term_dict() first.")

        # Choose the starting word, with error handling
        if seed_term:
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not found in corpus.")
            current_word = seed_term
        else:
            current_word = random.choice(list(self.term_dict.keys()))

        words = [current_word]

        # Generate next set of words
        for _ in range(term_count - 1):
            followers = self.term_dict.get(current_word, [])
            if not followers:
                break
            next_word = np.random.choice(followers)
            words.append(next_word)
            current_word = next_word

        # Return the word list
        return ' '.join(words)
        