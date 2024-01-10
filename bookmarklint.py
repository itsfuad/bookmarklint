"""Audit exported bookmark URL lists for duplicates and invalid schemes."""

def analyze(text):
    from urllib.parse import urlsplit
    seen=set();duplicate=[];invalid=[];valid=0
    for line in text.splitlines():
        raw=line.strip()
        if not raw:continue
        try: parts=urlsplit(raw)
        except ValueError:invalid.append(raw);continue
        if parts.scheme not in ('https','http') or not parts.netloc:invalid.append(raw);continue
        canonical=(parts.scheme.lower(),parts.netloc.lower(),parts.path,parts.query)
        if canonical in seen:duplicate.append(raw)
        else:seen.add(canonical);valid+=1
    return {'valid_unique':valid,'duplicates':duplicate,'invalid':invalid}
