def perevod_from_a_to_b (number, pos, target_pos):
        out = ''
        num = ''

        for i in number:
            num += str(i)

        num = int(num, pos)

        while num > 0:
            out = str(num%target_pos) + out
            num = num // target_pos

        return out

print(perevod_from_a_to_b('123', 4, 2))