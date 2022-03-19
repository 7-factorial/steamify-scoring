with open("rubric_proc_in.txt") as f:
    txt = f.read()

# pieces = txt.split("\no ")
replaa = txt.replace("\no ", "%@#&*@&(#$&@").replace("\n○ ", "%@#&*@&(#$&@")

def _rp(x: str):
    return x.replace("\n", " ").strip()

# proc1 = list(map(_rp, pieces))
proc1 = _rp(replaa)

donnn = proc1.replace("%@#&*@&(#$&@", "\n").lstrip()

with open("rubric_proc_out.txt", "w") as f:
    f.write(donnn)
    # f.write("\n".join(proc1))


