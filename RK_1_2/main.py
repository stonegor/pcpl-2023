import unittest
import data
from typing import List, Tuple
from entities import Orchestra, Musician, MusicianOrchestra


def get_musicians_with_orchestras(
    orchestras: List[Orchestra], musicians: List[Musician]
) -> List[Tuple[str, str]]:
    return sorted(
        [
            (musician.name, orchestra.name)
            for musician in musicians
            for orchestra in orchestras
            if orchestra.id == musician.orchestra_id
        ]
    )


def get_orchestras_with_musicians_count(
    orchestras: List[Orchestra], musicians: List[Musician]
) -> List[Tuple[str, int]]:
    return sorted(
        [
            (orchestra.name, musicians_count)
            for orchestra in orchestras
            for musicians_count in [
                len(
                    [
                        musician
                        for musician in musicians
                        if musician.orchestra_id == orchestra.id
                    ]
                )
            ]
        ],
        key=lambda item: item[1],
        reverse=True,
    )


def get_musicians_orhestras_by_ending_substring(
    orechestras: List[Orchestra],
    musicians: List[Musician],
    musicians_orchestras: List[MusicianOrchestra],
    substring: str,
) -> List[Tuple[str, List[str]]]:
    return [
        (musician.name, orchestras_of_musician)
        for musician in musicians
        for orchestras_of_musician in [
            [
                orchestra.name
                for orchestra in orechestras
                for musician_orchestra in musicians_orchestras
                if orchestra.id == musician_orchestra.orchestra_id
                and musician.id == musician_orchestra.musician_id
            ]
        ]
        if musician.name.endswith(substring)
    ]


def main():
    print("Запрос Б1")
    print(get_musicians_with_orchestras(data.orchestras, data.musicians))

    print("Запрос Б2")
    print(get_orchestras_with_musicians_count(data.orchestras, data.musicians))

    print("Запрос Б3")
    print(
        get_musicians_orhestras_by_ending_substring(
            orechestras=data.orchestras,
            musicians=data.musicians,
            musicians_orchestras=data.musicians_orchestras,
            substring="ov",
        )
    )


if __name__ == "__main__":
    main()
# %%
