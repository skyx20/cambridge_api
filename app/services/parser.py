from bs4 import BeautifulSoup, Tag, ResultSet
from bs4.element import NavigableString
from app.models.word import Word
from typing import Literal

class Parser(BeautifulSoup):


    def __init__(self, word_page: str):
        super().__init__()
        self.sp_page = BeautifulSoup(word_page, "html.parser")
        self.dict_variant = None


    def parse_meanings(self) -> Word | None:
        """
        It iteraits through the html page to find every concept by part of speech
        and guide words
        returns: Word object or None
        """
        if self.dict_variant is not None:
            word = Word(self._extract_word())
            "A word can be owned by differents pos, need to get all of them"
            all_pos_block = self._extract_pos_blocks()
            for pos_block in all_pos_block:
                "Each pos has its definitions by a guide word"
                pos = word.add_part_of_speech(self._extract_POS(pos_block))

                defs_by_gw = self._find_def_by_gw(pos_block)

                for def_by_gw in defs_by_gw:
                    "Each guide_word may have several meanings too"
                    guide_word = self._extract_guide_word(def_by_gw)
                    def_blocks  = self.get_all_def_blocks(def_by_gw)
                    gw = pos.add_guide_word(label=guide_word)
                    for current_block in def_blocks:
                        """
                        each block has a cerf level, a subcategory of a part of speech,
                        a definition and examples.
                        """
                        cerf_level = self._extract_cerf_level(current_block)
                        definition = self._extract_def(current_block)
                        examples = self._extract_examples(current_block)
                        gw.add_meaning(cerf_level, definition, examples)
            return word
        else: 
            raise ValueError("You need to select a dict variant befor parsing the meanings")
        return None
    
    
    def get_all_def_blocks(self, def_by_wg:Tag) -> ResultSet[Tag | NavigableString] | list:
        every_def = def_by_wg.find_all('div', class_="def-block ddef_block")
        return every_def
    

    def select_dictionary(self, dict_type:Literal["uk", "us", "be"]) -> None:
        """
        Get the requested dict from the options list
        params:
            dict_type (str) :
                uk = United Kingdom,
                us = United States,
                be = Business
        """
        if dict_type == "uk":
            self.dict_variant = self.sp_page.find('div', {'data-id': 'cald4'})
        elif dict_type == "us":
            self.dict_variant = self.sp_page.find('div', {'data-id': 'cacd'})
        elif dict_type == "be":
            self.dict_variant = self.sp_page.find('div', {'data-id': 'cbed'})

        if not self.dict_variant:
            raise ValueError("The selected dictionary variant is not available for this word")
        return 


    def _extract_def(self, def_block:Tag) -> str | None:
        definition = def_block.find("div", class_='def ddef_d db')
        f_definition = definition.text.strip()[:-1]
        return f_definition if definition else definition


    def _extract_pos_blocks(self,) -> ResultSet[Tag] | list:
        every_pos = self.dict_variant.find('div', class_=['entry-body']).find_all('div', class_='pr entry-body__el')
        return every_pos


    def _find_def_by_gw(self, pos_block:Tag) -> ResultSet[Tag] | list: 
        "it extracts all definitions by guide word"
        "A word may not have a guide word, so the dsens-noh is used to get those words"
        defs_by_gw = pos_block.find('div', class_=['pos-body']).find_all('div', class_=['pr dsense', 'dsense-noh'])
        return defs_by_gw if defs_by_gw else defs_by_gw


    def _extract_word(self) -> str | None:
        "get the word title"
        word = self.sp_page.find('span', class_='hw dhw')
        return word.text.strip().lower() if word else word
        
    def _extract_audio_pronunciation(
        self,
    ):
        "get audio pronuncation from US or UK"
        ...

    def _extract_examples(self, def_block:Tag)-> list[str]: 
        "get every single example in the definition block"
        " iterates every example tag found and get the text from them"
        examples = [
            example.text.strip()
            for example in def_block.find_all('span', class_=["eg", "deg"])
            if example
            ]
        return examples

    def _extract_POS(self, pos_block:Tag)-> str | None:
        pos = pos_block.find("div", class_="pos-header dpos-h").find('span', class_='pos dpos')
        return pos.text.strip() if pos else pos

    def _extract_guide_word(self, pos_block:ResultSet) -> str | None:
        # Guide word: helps you find the right meaning when a word has more than one meaning
        guide_word = pos_block.find("span", class_="guideword dsense_gw")
        if guide_word:
            "A word may not have a word guide and got only the meaning"
            guide_word = guide_word.find("span")
        return guide_word.text if guide_word else guide_word

    def _extract_related_words(
        self,
    ): ...
    def _extract_synonyms(
        self,
    ): ...
    def _extract_translation(
        self,
    ): ...
    def _extract_cerf_level(self,def_block: Tag,)-> str | None:
        "CEFR or difficulty level (e.g. A2, B1, C1)."
        cerf_level = def_block.find("span", class_=['epp-xref', 'dxref'])
        return cerf_level.string.strip() if cerf_level else cerf_level

