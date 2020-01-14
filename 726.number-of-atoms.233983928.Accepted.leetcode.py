from collections import defaultdict
class Solution(object):
    def countOfAtoms(self, formula):
        def count_atoms(start):
            counts = defaultdict(int)
            element = None
            element_count = 0
            i = start
            while i < len(formula):
                c = formula[i]
                if "A" <= c <= "Z":
                    if element:
                        counts[element] += element_count if element_count != 0 else 1
                        element_count = 0
                    element = c
                elif "a" <= c <= "z":
                    element += c
                elif "0" <= c <= "9":
                    element_count = int(c) + (element_count * 10 if element_count != 0 else 0)
                elif c == "(":
                    bracket_count, i = count_atoms(i + 1)
                    bracket_multiplier = 0
                    while i + 1 < len(formula) and "0" <= formula[i + 1] <= "9":
                        bracket_multiplier = bracket_multiplier * 10 + int(formula[i + 1])
                        i += 1
                    for el, num in bracket_count.items():
                        counts[el] += num * (bracket_multiplier if bracket_multiplier > 0 else 1)
                else:
                    if element:
                        counts[element] += element_count if element_count != 0 else 1
                    return [counts, i]
                i += 1
            return [counts, i]
        formula = "(" + formula + ")"
        counts = count_atoms(0)[0]
        return "".join([atom + (str(count) if count > 1 else "") for atom, count in sorted(counts.items())])
