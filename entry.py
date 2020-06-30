from typing import List

_repo_url_link_map = {
    "prelude": r"https://github.com/purescript-python/purescript-prelude.py",
    "effect": r"https://github.com/purescript-python/purescript-effect.py",
    "console": r"https://github.com/purescript-python/purescript-console.py",
    "control": r"https://github.com/purescript-python/purescript-control.py",
    "enums": r"https://github.com/purescript-python/purescript-enums.py",
    "foldable-traversable": r"https://github.com/purescript-python/purescript-foldable-traversable.py",
    "partial": r"https://github.com/purescript-python/purescript-partial.py",
    "show-python": r"https://github.com/purescript-python/purescript-show-python",
    "functions": r"https://github.com/purescript-python/purescript-functions.py",
    "nullable": r"https://github.com/purescript-python/purescript-nullable.py",
    "refs": r"https://github.com/purescript-python/purescript-refs.py",
    "assert": r"https://github.com/purescript-python/purescript-assert.py",
    "st": r"https://github.com/purescript-python/purescript-st.py",
    "unsafe-coerce": r"https://github.com/purescript-python/purescript-unsafe-coerce.py",
    "unfoldable": r"https://github.com/purescript-python/purescript-unfoldable.py",
    "arrays": r"https://github.com/purescript-python/purescript-arrays.py",
    "exceptions": r"https://github.com/purescript-python/purescript-exceptions.py",
    "globals": r"https://github.com/purescript-python/purescript-globals.py",
    "integers": r"https://github.com/purescript-python/purescript-integers.py",
    "math": r"https://github.com/purescript-python/purescript-math.py",
    "lazy": r"https://github.com/purescript-python/purescript-lazy.py",
    "strings": r"https://github.com/purescript-python//purescript-strings.py",
    "random": r"https://github.com/purescript-python/purescript-random.py",
    "quickcheck": r"https://github.com/purescript-python/purescript-quickcheck.py",
    "record": r"https://github.com/purescript-python/purescript-record.py",
    "aff": r"https://github.com/purescript-python/purescript-aff.py",
    "affjax": r"https://github.com/purescript-python/purescript-affjax.py",
    "argonaut-core": r"https://github.com/purescript-python/purescript-argonaut-core.py",
    "datetime": r"https://github.com/purescript-python/purescript-datetime.py",
    "foreign-object": r"https://github.com/purescript-python/purescript-foreign-object.py",
    "foreign": r"https://github.com/purescript-python/purescript-foreign.py",
    "web-dom": r"https://github.com/purescript-python/purescript-web-dom.py",
    "web-events": r"https://github.com/purescript-python/purescript-web-events.py",
    "web-file": r"https://github.com/purescript-python/purescript-web-file.py",
    "web-xhr": r"https://github.com/purescript-python/purescript-web-xhr.py",
}


def solve(package_name: str, versions: List[int]) -> str:
    repo_url = _repo_url_link_map.get(package_name)
    if repo_url:
        return repo_url
    raise NotImplementedError(
        "package {} is not supported by this mirror".format(package_name)
    )
