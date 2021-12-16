import copy

def read_file(day):
    with open(f"data/day-{day}.txt", 'rt') as fin:
        aux = fin.read().rstrip()
        data = str(bin(int(aux, 16))[2:])
        if int(aux[0], 16) < 8:
            data = '0' + data
            if int(aux[0]) < 4:
                data = '0' + data
    return data


def get_versions_1(packet):
    versions = [int(packet[:3], 2)]
    packet_id = int(packet[3:6], 2)
    #print(f"packet: {packet} | version: {versions} | packet_id: {packet_id} | packet_6: {packet[6]} | len: {len(packet)}") 
    if packet_id == 4: # literal value
        len_packet = 3 + 3
        i = 0
        while packet[len_packet+i] != '0':
            i += 5
        len_packet += i + 5
    else: # operator value
        if packet[6] == '1':
            bits_len_subpackets = 11
            total_number_subpackets = int(packet[7:7+bits_len_subpackets], 2)
            #print(f"bits_len_subpackets: {bits_len_subpackets} | total_length_subpackets: {total_length_subpackets} | packet_bits_len: {packet[7:7+bits_len_subpackets]}")
            len_packet = 3 + 3 + 1 + bits_len_subpackets
            i = 0
            for n in range(total_number_subpackets):
                versions_subpacket, len_subpacket = get_versions_1(packet[7+bits_len_subpackets+i:])
                i += len_subpacket
                versions += versions_subpacket
                len_packet += len_subpacket
        else:
            bits_len_subpackets = 15
            total_length_subpackets = int(packet[7:7+bits_len_subpackets], 2)
            #print(f"bits_len_subpackets: {bits_len_subpackets} | total_length_subpackets: {total_length_subpackets} | packet_bits_len: {packet[7:7+bits_len_subpackets]}")
            len_packet = 3 + 3 + 1 + bits_len_subpackets + total_length_subpackets
            i = 0
            while i < total_length_subpackets:
                versions_subpacket, len_subpacket = get_versions_1(packet[7+bits_len_subpackets+i:])
                i += len_subpacket
                versions += versions_subpacket
    return versions, len_packet

def get_versions_2(packet):
    versions = [int(packet[:3], 2)]
    packet_id = int(packet[3:6], 2)
    #print(f"packet: {packet} | version: {versions} | packet_id: {packet_id} | packet_6: {packet[6]} | len: {len(packet)}") 
    if packet_id == 4: # literal value
        len_packet = 3 + 3
        i = 0
        value_packet = ''
        while packet[len_packet+i] != '0':
            value_packet += packet[len_packet+i+1:len_packet+i+1+4]
            i += 5
        value_packet += packet[len_packet+i+1:len_packet+i+1+4]
        value_packet = int(value_packet, 2)
        len_packet += i + 5
    else: # operator value
        values_subpackets = []
        if packet[6] == '1':
            bits_len_subpackets = 11
            total_number_subpackets = int(packet[7:7+bits_len_subpackets], 2)
            #print(f"bits_len_subpackets: {bits_len_subpackets} | total_length_subpackets: {total_length_subpackets} | packet_bits_len: {packet[7:7+bits_len_subpackets]}")
            len_packet = 3 + 3 + 1 + bits_len_subpackets
            i = 0
            for n in range(total_number_subpackets):
                versions_subpacket, len_subpacket, value_subpacket = get_versions_2(packet[7+bits_len_subpackets+i:])
                i += len_subpacket
                versions += versions_subpacket
                len_packet += len_subpacket
                values_subpackets.append(value_subpacket)
        else:
            bits_len_subpackets = 15
            total_length_subpackets = int(packet[7:7+bits_len_subpackets], 2)
            #print(f"bits_len_subpackets: {bits_len_subpackets} | total_length_subpackets: {total_length_subpackets} | packet_bits_len: {packet[7:7+bits_len_subpackets]}")
            len_packet = 3 + 3 + 1 + bits_len_subpackets + total_length_subpackets
            i = 0
            while i < total_length_subpackets:
                versions_subpacket, len_subpacket, value_subpacket = get_versions_2(packet[7+bits_len_subpackets+i:])
                i += len_subpacket
                versions += versions_subpacket
                values_subpackets.append(value_subpacket)
        if packet_id == 0:
            value_packet = sum(values_subpackets)
        elif packet_id == 1:
            value_packet = 1
            for i in values_subpackets:
                value_packet *= i
        elif packet_id == 2:
            value_packet = min(values_subpackets)
        elif packet_id == 3:
            value_packet = max(values_subpackets)
        elif packet_id == 5:
            if values_subpackets[0] > values_subpackets[1]:
                value_packet = 1
            else:
                value_packet = 0
        elif packet_id == 6:
            if values_subpackets[0] < values_subpackets[1]:
                value_packet = 1
            else:
                value_packet = 0
        elif packet_id == 7:
            if values_subpackets[0] == values_subpackets[1]:
                value_packet = 1
            else:
                value_packet = 0

    return versions, len_packet, value_packet

def process_data_1(data):
    versions, len_packet = get_versions_1(data)
    #print(versions)
    return sum(versions)

def process_data_2(data):
    versions, len_packet, value_packet = get_versions_2(data)
    #print(versions)
    return value_packet


if __name__ == "__main__":
    day = "16"
    data = read_file(day)
    print(data)
    result_1 = process_data_1(copy.deepcopy(data))
    print(f"result 1: {result_1}")
    result_2 = process_data_2(data)
    print(f"result 2: {result_2}")
