class Value:

    def __init__ (self, data):
        self.__source_ip, self.__target_ip, self.__ttl, self.__packet_data, self.__summa = data
        self.__source_ip = list(map(int, self.__source_ip.split(sep='.')))
        self.__target_ip = list(map(int, self.__target_ip.split(sep='.')))
        self.__ttl = int(self.__ttl)
        self.__packet_data = int(self.__packet_data)
        self.__summa = int(self.__summa)

    def get_all (self):
        return self.__source_ip, self.__target_ip, self.__ttl, self.__packet_data, self.__summa

    def encode (self, flag=1):

        source_ip = Value.formate(int(self.__source_ip[0]), 1)

        for i in range(1, 4):
            source_ip += Value.formate(int(self.__source_ip[i]), 1)

        target_ip = Value.formate(int(self.__target_ip[0]), 1)

        for i in range(1, 4):
            target_ip += Value.formate(int(self.__target_ip[i]), 1)

        ttl = Value.formate(int(self.__ttl), 1)
        data = Value.formate(int(self.__packet_data), 8)
        summa = Value.formate(int(self.__summa), 3)

        out = source_ip + target_ip + ttl + data + summa

        if flag == -1:

            a = bytes([out[19]])

            for i in range(1, 20):
                s = [out[19-i]]
                a += bytes(s)
            
            return a + bytes([1])

        return out + bytes([0])

    def decode (data):
        
        flag = data[20]

        if flag == 1:

            out = bytes([data[19]])
            
            for i in range(1, 20):
                s = [data[19-i]]
                out += bytes(s)

            data = out

        source_ip = []
        target_ip = []

        for i in range(0, 4):
            source_ip.append(Value.deformate(data[i], 1))
        
        for i in range(4, 8):
            target_ip.append(Value.deformate(data[i], 1))

        ttl = Value.deformate(data[8], 1)
        packet_data = Value.deformate(data[9:17], 8)
        summa = Value.deformate(data[17::], 3)

        return source_ip, target_ip, ttl, packet_data, summa

    def formate (data, bits):

        out = []

        if bits == 1:
            out.append(data)
            out = bytes(out)
            return out

        for i in range(bits-1, -1, -1):
            out.append((data>>(8*i)) & 255)

        out = bytes(out)
        
        return out

    def deformate (data, bits):

        if bits == 1:
            return data

        out = 0
        c = 0

        for i in range(bits-1, -1, -1):

            out = out | (data[c]<<(i*8))
            c += 1

        return out



data = '127.0.0.1 192.168.0.1 100 1337228 84672'
value1 = Value(data.split())
print(value1.get_all())
print(Value.decode(value1.encode(-1)))