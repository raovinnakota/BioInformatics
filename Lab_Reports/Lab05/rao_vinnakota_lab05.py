"""
Lab 05 - Sequence Alignment
Rao Vinnakota

"""

class SequenceVariation:
    def __init__(self, input_seq):
        self.input_seq = input_seq
        self.validate()

    def get_input_seq(self):
        return (self.input_seq)

    def validate(self):
        input_seq = self.get_input_seq()
        valid = ['A', 'G', 'T', 'C', 'N']

        for i in input_seq:
            if i not in valid:
                raise Exception("Not a valid input sequence")
        return (1)


Seq = SequenceVariation("GNGTCANTGCG")
