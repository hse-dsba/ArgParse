# -*- coding utf8 -*-
from bs4 import BeautifulSoup
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,

    Doc
)
import requests
import json
from collections import defaultdict
from tqdm import tqdm
import re


def preprocess(textt: str) -> str:
    if textt:
        textt = textt.lower()
        return re.sub(r"[/\'\(\)\"-\-;\@.,!:;?\+\-\n]", ' ', textt)


def Natan(text):
    segmenter = Segmenter()

    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    syntax_parser = NewsSyntaxParser(emb)
    doc = Doc(text)

    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)
    doc.parse_syntax(syntax_parser)
    morph_vocab = MorphVocab()
    words = []
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    for k, v in {_.text: _.lemma for _ in doc.tokens}.items():
        words.append(v)
    return words


pages = 1
d = defaultdict(list)
params = {'page': 1}
url = 'https://career.habr.com/vacancies?type=all'
links = []
while params['page'] <= pages:
    req = requests.get(url, params=params)
    src = req.text

    soup = BeautifulSoup(src, 'html.parser')
    all_cards = soup.find_all(class_="vacancy-card__title-link")
    for item in all_cards:
        item_text = item.text
        item_href = 'https://career.habr.com' + item.get("href")
        d[item_href] = [item_text]
        links.append(item_href)
    for link in tqdm(links):
        reqq = requests.get(link)
        srcc = reqq.text
        soupp = BeautifulSoup(srcc, 'html.parser')
        for i in soupp.find_all("div", "job_show_description__body"):
            if Natan(preprocess(i.text)) not in d[link]:
                d[link].append(Natan(preprocess(i.text)))

    with open('all_vacancies_dict.json', 'w', encoding='utf8') as file:
        json.dump(d, file, indent=4, ensure_ascii=False)
    params['page'] += 1
need = input()
enter = Natan(preprocess(need))
cnt = 0
ll = []
viv = {}
for k, v in d.items():
    keys = set(v[1])
    if len(keys.intersection(enter)) >= len(enter) * 0.5:
        if len(ll) < 5:
            ll.append(k)
print(*ll, sep='\n')