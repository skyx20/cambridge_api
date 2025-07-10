from email.mime import audio
import json
from typing import Literal


class Meaning:
    """
    Meaning represents the data block of each meaning, each one has a cerf level,
    a meaning and one example or more
    """
    def __init__(self, meaning: str, cerf_level:str, examples: list) -> None:
        self._cerf_level = cerf_level
        self._meaning = meaning
        self._examples = examples

    def to_dict(self):
        return {
            "definition": self._meaning,
            "cerfLevel": self._cerf_level,
            "examples": self._examples
        }
    
    def __str__(self):
        return f'({self._meaning}) example: {self._examples[0] if self._examples else ""}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self._meaning})'

class GuideWord():
    """
    Guide words help you find the explanation you are looking 
    for when a word has more than one main meaning. 
    Each One has a list of Meanings objects
    """
    def __init__(self, label: str):
        self.label = label
        self.meanings:list[Meaning] = []
    
    def add_meaning(self, cerf_level, definition, examples):
        m = Meaning(
            meaning= definition,
            cerf_level= cerf_level,
            examples=examples
            )
        self.meanings.append(m)

    def to_dict(self):
        return {
            "guideWord": self.label,
            "meanings": [m.to_dict() for m in self.meanings]
        }
    def __str__(self):
        return f'{self.label} {self.meanings[0].__str__() if self.meanings else "meaning"}'
        
    def __repr__(self):
        return f'{self.__class__.__name__}({self.label}) \n{" "*8}' \
                f'{self.meanings[0].__repr__() if self.meanings else "None"}'


class PartOfSpeech():
    """
    One of the grammatical groups, such as noun, verb, and adjective, 
    into which words are divided depending on their use.
    Each One has a list of word guide Objects
    """

    def __init__(self, pos:str) -> None:
        self.pos = pos
        self.guide_words:list[GuideWord] = []

    def add_guide_word(self, label:str,) -> GuideWord:
        gw = GuideWord(label)
        self.guide_words.append(gw)
        return gw

    def to_dict(self):
        return {
            "posType": self.pos,
            "guideWordDefs": [gw.to_dict() for gw in self.guide_words]
        }
    def __str__(self):
        return f'{self.pos} {self.guide_words[0].__str__() if self.guide_words else "guide_word"}'
        
    def __repr__(self):
        return f'{self.__class__.__name__}({self.pos})\n{" "*4}{self.guide_words[0].__repr__() if self.guide_words else "[]"}'

class Word:
    """
    Word object immitates the structure of a word like in Cambridge dictionary
    Each one has a list of PartOfSpeech objects
    """
    def __init__(self, word: str):
        self.word = word if word else ""
        self._origin = ""
        self.meanings:list[PartOfSpeech] = []
        self._audios:dict = {}
        self._related_words = None
        self._synonyms = None
        # self._translation = None
        self._tenses = None
        self._sense_domain = None
        self._IPAS:dict = {}
    
        

    def get_meanings(self) -> list:
        return self.meanings

    def get_related_words(self) -> str | None:
        return self._related_words

    def get_synonyms(self) -> str | None:
        return self._synonyms

    def get_IPAS(self) -> dict:
        return self._IPAS

    def to_dict(self) -> dict:
        return {
            "word": self.word,
            "ipas": self._IPAS,
            "audio_links": self._audios,
            "origin": self._origin,
            "meanings": [pos.to_dict() for pos in self.meanings]
        }
    
    def to_json(self) -> str:
        json_data = json.dumps(self.to_dict())
        return json_data
    
    def add_part_of_speech(self, name:str) -> PartOfSpeech:
        new_pos = PartOfSpeech(name)
        self.meanings.append(new_pos)
        return new_pos
    
    def add_audio_link(self, country:Literal['uk', 'us'], audio_link:str):
        self._audios.setdefault(country, country) 
        self._audios[country] = audio_link
        return self._audios
    
    def add_IPA(self, country:Literal['uk', 'us'], ipa:str):
        self._IPAS.setdefault(country, country) 
        self._IPAS[country] = ipa
        return self._IPAS

    def add_origin(self, origin:Literal['uk', 'us', 'be']):
        self._origin = origin if not origin == 'be' else 'business'

    def __str__(self):
        return f'{self.word} {self.meanings[0].__str__() if self.meanings else "PartOfSpeech"}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.word}) \n{" "*2}{self.meanings[0].__repr__() if self.meanings else "[]"}'

