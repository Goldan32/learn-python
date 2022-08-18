def make_link(title: str, level: int, num: int) -> str:
    return f'{" " * 4 * level}{num}. [{title.strip()}](#{"-".join(title.lower().strip().split(" "))})'


def main():
    fname = "README_raw.md"
    mod_fname = "README.md"
    toc_placeholder = "\\\\insert_toc\\\\"

    # Make table of contents
    toc = []
    lines = []
    linenum = 0
    toc_placeholder_line = -1
    with open(fname, "r") as f:
        lines = f.readlines()
        in_code_block = False
        numbering = {0: 1, 1: 1, 2: 1}


        for line in lines:
            if line.strip() == toc_placeholder:
                toc_placeholder_line = linenum
            linenum = linenum + 1

            # Detect code block ending
            if in_code_block:
                if line[0:3] == "```":
                    in_code_block = False
                continue
            
            # Detect code block beginning
            if line[0:3] == "```":
                in_code_block = True
                continue

            if line[0:3] == "## ":
                toc.append(make_link(line[3:], 0, numbering[0]))
                numbering[0] = numbering[0] + 1
                numbering[1] = 1
                continue

            if line[0:4] == "### ":
                toc.append(make_link(line[4:], 1, numbering[1]))
                numbering[1] = numbering[1] + 1
                numbering[2] = 1
                continue

            if line[0:5] == "#### ":
                toc.append(make_link(line[5:], 2, numbering[2]))
                numbering[2] = numbering[2] + 1
                continue


    # Replace toc placeholder with toc string
    toc_string = "\n".join(toc)
    lines[toc_placeholder_line] = toc_string + "\n"

    with open(mod_fname, "w") as f:
        for line in lines:
            f.write(line)

if __name__ == "__main__":
    main()
