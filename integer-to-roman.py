class Solution:
    def getNearestMinimal(self,input,numbers):
        z=0
        for i in numbers:
            if input>=i:
                z = i
        return z
    def getNearestMaximal(self,input,numbers):
        for i in numbers:
            if input<i:
                return i
    global roman
    roman = list()
    global inputValue

    
    def subsctructive(self,input,numbers):
        str_input = str(input)
        if str_input[0]=='4' or str_input[0]=='9':
            self.less_substructive(input,numbers)
        else:
            self.more_substructive(input,numbers)
        return roman
    def intToRoman(self, num: int) -> str:
        global roman
        roman = list()
        global inputValue
        inputValue = num
        numerals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        numbers = list(numerals.values())
        self.subsctructive(inputValue,numbers)
        key_list = list(numerals.keys())
        val_list = list(numerals.values())
        new_dict = [key_list[val_list.index(k)] for k in roman if k in val_list]
        return "".join(new_dict)

    def less_substructive(self,input,numbers):
        global inputValue
        if input>10:
            power = pow(10,len(str(input))-1)
            z=int(input/power)*power
            maximal_no = self.getNearestMaximal(z,numbers)
            diff = maximal_no - z
            roman.extend([diff,maximal_no])
            extended_diff = input - z
            inputValue = extended_diff
        else:
            maximal_no = self.getNearestMaximal(input,numbers)
            extended_diff = maximal_no - input
            inputValue = inputValue - input
            roman.extend([extended_diff,maximal_no])
        if inputValue == 0:
            return roman
        self.subsctructive(extended_diff,numbers)

    def more_substructive(self,input,numbers):
        global inputValue
        minimal_no = self.getNearestMinimal(input,numbers)
        diff = input-minimal_no
        inputValue = diff
        roman.append(minimal_no)
        if diff == 0:
            return roman
        if diff>0:
            self.subsctructive(diff,numbers)
        
