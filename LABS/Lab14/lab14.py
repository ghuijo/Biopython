# Biopython
# L14. Automata


from Automata import Automata

def test():
    auto = Automata("ACGT", "ACA")
    auto.print_automata()
    print(auto.apply_seq("CACAACAA"))
    print(auto.occurences_pattern("CACAACAA"))

test()
