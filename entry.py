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
}


def solve(package_name: str, versions: List[int]) -> str:
    repo_url = _repo_url_link_map.get(package_name)
    if repo_url:
        return repo_url
    raise NotImplementedError(
        "package {} is not supported by this mirror".format(package_name)
    )
