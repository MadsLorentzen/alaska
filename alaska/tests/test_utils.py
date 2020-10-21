"""
Tests for alaska/utils.py
"""
import pytest
from ..utils import Vocab


def test_vocab_add_words():
    """
   Test that we can instantiate the Vocab class and add words
   """
    vc = Vocab()
    vc.add_words(["mwd", "lwd", "lwd"])
    assert vc.word2index == {"mwd": 4, "lwd": 5}
    assert vc.word2count["lwd"] == 2
    assert vc.index2word == ["<PAD>", "<SOS>", "<EOS>", "<UNK>", "mwd", "lwd"]


def test_vocab_trim_by_frequency():
    """
   Test that the vocab class trim method works with min frequency of 2
   """
    vc = Vocab()
    vc.add_words(["mwd", "lwd", "lwd"])
    vc.trim(min_freq=2, vocab_size=None)
    assert vc.word2index == {"lwd": 4}
    assert vc.word2count["lwd"] == 2
    assert vc.index2word == ["<PAD>", "<SOS>", "<EOS>", "<UNK>", "lwd"]


def test_vocab_trim_by_size():
    """
   Test that the vocab class trim method works with min vocab size of 2
   """
    vc = Vocab()
    vc.add_words(["mwd", "lwd", "lwd"])
    vc.trim(min_freq=1, vocab_size=2)
    assert vc.word2index == {"mwd": 4, "lwd": 5}
    assert vc.word2count["lwd"] == 2
    assert vc.index2word == ["<PAD>", "<SOS>", "<EOS>", "<UNK>", "mwd", "lwd"]


def test_vocab_embeddings():
    """
   Test that the vocab class embeddings are equal to None at instantiation
   """
    vc = Vocab()
    assert vc.embeddings is None


def test_vocab_getitem():
    """
   Test that the vocab class can get items
   """
    vc = Vocab()
    vc.add_words(["mwd", "lwd", "lwd"])
    assert vc.__getitem__(5) == "lwd"


def test_vocab_len():
    """
   Test that the vocab class can return its length
   """
    vc = Vocab()
    vc.add_words(["mwd", "lwd", "lwd"])
    assert vc.__len__() == 6


def test_vocab_words():
    """
   Test that the vocab class can return words and punctuation
   """
    vc = Vocab()
    vc.add_words(["mwd", "lwd", "lwd"])
    assert vc.is_word(token_id=3) is not True
    assert vc.is_word(token_id=7) is True
    assert vc.is_word(True) is not True