from pathlib import Path
from dataclasses import dataclass, field
from typing import Iterator

import pandas as pd

@dataclass(kw_only=True)
class Table:
    name: str
    header_comments: list[str] = field(default_factory=list)
    table_comments: dict[int, str] = field(default_factory=dict)
    dataframe: pd.DataFrame

    def to_file(self, dst: Path):
        with open(dst, 'w') as DST:
            for comment in self.header_comments:
                DST.write(f"! {comment}\n")
            DST.write(f"{self.name}\n")
            table = self.dataframe.to_string(justify='left', index=False).split('\n')

            for i, line in enumerate(table, start=-1):
                DST.write(line)
                if (i) in self.table_comments:
                    DST.write(f" ! {self.table_comments[i]}")
                DST.write('\n')


    @classmethod
    def from_file(cls, path: Path):
        header_comments = list()
        table_comments = dict()
        columns = list()
        data = list()
        with open(path, 'r', encoding="UTF-8", errors="ignore") as PATH:
            name_line = None
            for i, line in enumerate(PATH):
                line = line.strip()
                # Consume the header lines first
                if line.startswith('!'):
                    header_comments.append(line.lstrip('!').strip())
                # Then consume a single line with the name of the table
                elif name_line is None:
                    name_line = i
                    name = line.split("!", maxsplit=1)[0].strip()
                # Then consume header
                elif (i - 1) == name_line:
                    columns = line.split("!",maxsplit=1)[0].split()
                # Then consume the remainder of the file
                else:
                    line_data, *comments = line.split('!', maxsplit=1)
                    if comments:
                        table_comments[i - name_line - 2] = comments[0].strip()
                    data.append(line_data.split())
        try:
            dataframe = pd.DataFrame(columns=columns, data=data)
        except ValueError as e:
            print(name)
            print(columns)
            print(data)
            raise e

        return Table(
            name=name, 
            header_comments=header_comments,
            table_comments=table_comments,
            dataframe=dataframe)

def walk_for_table_files(top: Path) -> Iterator[Path]:
    for obj in top.iterdir():
        if obj.is_file() and (obj.suffix == ".table"):
            yield obj
        elif obj.is_dir() and (obj.name != "gen"):  # Don't look at dynamic tables
            yield from walk_for_table_files(obj)

def tables_in_dir(top: Path) -> list[Table]:
    return [Table.from_file(f) for f in walk_for_table_files(top)]

def main(table_dir: Path, dst: Path = None):
    if dst is None:
        dst = Path('./docs/auto/')
    if not dst.exists():
        raise FileNotFoundError("output directory does not exist")
    tables = tables_in_dir(table_dir)
    for table in tables:
        md_file = dst / f"{table.name}.md"
        with open(md_file, "w") as MD_FILE:
            MD_FILE.write(f"## {table.name}\n")
            for header in table.header_comments:
                MD_FILE.write(f"{header}\n\n")
            rows = len(table.dataframe)
            if rows > 10:
                rows = 10
            MD_FILE.write(f"### First {rows} Rows of the Table\n")
            df_sample = table.dataframe.head(rows)
            MD_FILE.write(df_sample.to_markdown(index=False))


if __name__ == '__main__':
    main(Path(r"C:\Users\zroy\Documents\_Modeling\_2023DCR\calsim3-dcr\Run\Lookup"))
    
