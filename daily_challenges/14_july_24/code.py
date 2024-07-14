# https://leetcode.com/problems/number-of-atoms/description/
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        element_count_map = self.return_map(formula)
        print(element_count_map)
        sorted_keys = element_count_map.keys()
        list(sorted_keys).sort()
        return_string = ""
        for i in sorted(sorted_keys):
            count = element_count_map[i]
            if count ==1:
                return_string += i
            else:
                return_string += i+str(count)
        return return_string

    
    def return_map(self, formula):
        original_map = {}
        i = 0
        def add_in_map(key, value, original_map):
            if key in original_map.keys():
                print('printing in add in map', key, original_map[key], value)
                original_map[key] =  original_map[key] + value
            else:
                original_map[key] = value
            return original_map
        def add_maps(original_map, new_map, times):
            for key in new_map.keys():
                original_map = add_in_map(key, times*new_map[key], original_map)
            return original_map
        def find_number(string):
            number_string = ""
            count = 0
            for i in string:
                if i.isnumeric():
                    number_string += i
                else:
                    break
                count += 1
            if number_string =="":
                number_string = "1"
            return int(number_string), count

        while i < len(formula):
            bracket_open_count = 0
            if formula[i]=='(':
                new_str = ""
                bracket_open_count = 0
                for j in range(i+1, len(formula)):
                    if formula[j]=='(':
                        new_str += formula[j]
                        bracket_open_count += 1
                    elif formula[j]==')':
                        if bracket_open_count == 0:
                            i = j + 1
                            break
                        else:
                            new_str += formula[j]
                            bracket_open_count -= 1
                    else:
                        new_str += formula[j]
                
                times,index = find_number(formula[i:])
                print('new_str', new_str)
                original_map = add_maps(original_map, self.return_map(new_str), times)
                i = i + index
            elif formula[i].isupper():
                if i==len(formula)-1 or formula[i+1].isupper():
                    original_map = add_in_map(formula[i], 1, original_map)
                    i = i + 1
                elif formula[i+1].isnumeric():
                    number, count = find_number(formula[i+1:])
                    original_map = add_in_map(formula[i], number, original_map)
                    i += count
                elif formula[i+1].islower():
                    if i+2>=len(formula):
                        original_map = add_in_map(formula[i:i+2], 1, original_map)
                        i = i + 2
                    elif formula[i+2].isnumeric():
                        number, count = find_number(formula[i+2:])
                        original_map = add_in_map(formula[i:i+2], number, original_map)
                        i += count + 1
                    elif formula[i+2].isupper():
                        original_map = add_in_map(formula[i:i+2], 1, original_map)
                        i += 2
                    else:
                        original_map = add_in_map(formula[i:i+2], 1, original_map)
                        i += 2
                else:
                    original_map = add_in_map(formula[i], 1, original_map)
                    i += 1

            else:
                print("ooh no.....", formula[i])
                i = i+1
        return original_map

