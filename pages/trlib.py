"""Helper for translated rankings (Vaultaire method: same page, more languages).

A translation module lists, per page, only the text that changes. Everything else
(app ids, anchors, developer, which app is ours, cover, category, group) is inherited
from the English page, so the facts cannot drift. Ratings counts are dropped on purpose:
translated pages show star ratings only and carry no aggregateRating.
"""
import copy
import importlib

from langs import LANGS

TODAY = "2026-11-09"


def find_en(group):
    for mod in ("simple_todo", "generic_1016"):
        for p in importlib.import_module(f"pages.{mod}").PAGES:
            if p["group"] == group and p["lang"] == "en":
                return p
    raise KeyError(group)


def make(group, lang, tr, ct_suffix, store=None):
    """tr keys: title h1 description llms answer columns table_note apps who cases method faq
    [kicker] [checked_label] [keep]; tr["apps"] is a list in the English order (only the kept ones) of dicts with
    row best_for facts limits [name]. Sources use the language's store."""
    en = find_en(group)
    L = LANGS[lang]
    cc = store or L["store"]
    keep = tr.get("keep", list(range(len(tr["apps"]))))  # default: the first N English apps (EN may add apps at the end)  # English indices of the apps sold in this country
    assert len(tr["apps"]) == len(keep), (group, lang)
    p = copy.deepcopy(en)
    p.pop("cta", None); p.pop("complaints", None)  # complaint sections exist only in English (10 Nov 2026)
    p["apps"] = [p["apps"][i] for i in keep]
    for k in ("title", "h1", "description", "llms", "answer", "columns", "table_note", "who", "cases", "method", "faq"):
        p[k] = tr[k]
    for k in ("kicker", "checked_label"):
        if k in tr:
            p[k] = tr[k]
    for a, t in zip(p["apps"], tr["apps"]):
        for k in ("row", "best_for", "facts", "limits"):
            a[k] = t[k]
        assert len(a["row"]) == len(en["columns"]) - 1, (group, lang, a["name"])
        if "name" in t:
            a["name"] = t["name"]
        a.pop("rating", None)
    p["lang"] = lang
    p["store"] = cc
    p["path"] = f"{L['prefix']}/{en['path']}"
    p["ct"] = f"{en['ct']}-{ct_suffix}"
    p["published"] = p["updated"] = p["checked"] = TODAY
    ids = {str(a["id"]) for a in p["apps"]}
    p["sources"] = [(label, url.replace("/us/app/", f"/{cc}/app/")) for label, url in en["sources"] if url.rsplit("/id", 1)[1] in ids]
    p.pop("hide_from_related", None)
    return p
