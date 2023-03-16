import codecs
import os
import binascii
import struct
import math
import time

# Binary segmentation
def read_by_str(path, segment_length):
    f = codecs.open(path, 'rb')
    size = os.path.getsize(path)
    binary_list = []
    with f:
        fileText = f.read()
        hexstr = binascii.hexlify(fileText)
        bsstr = bin(int(hexstr, 16))[2:]
        str_binary = bsstr
        binary_length = len(bsstr)
    pos = 0
    i = 0
    while pos < binary_length:
        binary_list.append(str_binary[pos:pos+segment_length])
        pos += segment_length
        i+=1
    last_len = len(binary_list[-1])
    if last_len != segment_length:
        while last_len !=segment_length:
            binary_list[-1] += '0'
            last_len +=1
    return binary_list,size

# read file
def load_file_to_BinaryMatrix(path, segment_length):
    with open(path, mode="rb") as file:
        size = os.path.getsize(path)
        matrix = [['0' for _ in range(segment_length)] for _ in range(math.ceil(size * 8 / segment_length))]
        row = 0
        col = 0
        for byte_index in range(size):
            # Read a file as bytes
            one_byte = file.read(1)
            element = list(str(bin(struct.unpack("B", one_byte)[0]))[2:].zfill(8))
            for bit_index in range(8):
                matrix[row][col] = element[bit_index]
                col += 1
                if col == segment_length:
                    col = 0
                    row += 1
    return matrix, size

B_set = [ [{'AA':['5','2','0','3'],'TT':['2','5','0','3'],'CC':['0','2','5','3'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['2','5','3','0'],'CC':['2','0','5','3'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['2','5','0','3'],'CC':['0','2','5','3'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['2','5','3','0'],'CC':['3','0','5','2'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['2','5','0','3'],'CC':['0','3','5','2'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['2','5','3','0'],'CC':['2','0','5','3'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['2','5','0','3'],'CC':['0','3','5','2'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['2','5','3','0'],'CC':['3','0','5','2'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['2','5','0','3'],'CC':['0','2','5','3'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['3','5','2','0'],'CC':['2','0','5','3'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['2','5','0','3'],'CC':['0','2','5','3'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['3','5','2','0'],'CC':['3','0','5','2'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['2','5','0','3'],'CC':['0','3','5','2'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['3','5','2','0'],'CC':['2','0','5','3'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['2','5','0','3'],'CC':['0','3','5','2'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['3','5','2','0'],'CC':['3','0','5','2'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['3','5','0','2'],'CC':['0','2','5','3'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['2','5','3','0'],'CC':['2','0','5','3'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['3','5','0','2'],'CC':['0','2','5','3'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['2','5','3','0'],'CC':['3','0','5','2'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['3','5','0','2'],'CC':['0','3','5','2'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['2','5','3','0'],'CC':['2','0','5','3'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['3','5','0','2'],'CC':['0','3','5','2'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['2','5','3','0'],'CC':['3','0','5','2'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['3','5','0','2'],'CC':['0','2','5','3'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['3','5','2','0'],'CC':['2','0','5','3'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['3','5','0','2'],'CC':['0','2','5','3'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['3','5','2','0'],'CC':['3','0','5','2'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['3','5','0','2'],'CC':['0','3','5','2'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['3','5','2','0'],'CC':['2','0','5','3'],'GG':['3','0','2','5']}],
                [{'AA':['5','2','0','3'],'TT':['3','5','0','2'],'CC':['0','3','5','2'],'GG':['0','3','2','5']},{'AA':['5','2','3','0'],'TT':['3','5','2','0'],'CC':['3','0','5','2'],'GG':['3','0','2','5']}] ]
E_set = {'AA':{'0': 'TC', '1': 'TG', '00': 'CA', '01': 'CT', '10': 'GA', '11': 'GT'},
             'TT':{'0': 'AC', '1': 'AG', '00': 'CA', '01': 'CT', '10': 'GA', '11': 'GT'},
             'CC':{'0': 'AC', '1': 'AG', '00': 'TC', '01': 'TG', '10': 'GA', '11': 'GT'},
             'GG':{'0': 'AC', '1': 'AG', '00': 'TC', '01': 'TG', '10': 'CA', '11': 'CT'}}
# return GC ratio
def check_gc(sequence):
    return float(sequence.count("C") + sequence.count("G")) / float(len(sequence))

# last 1 or 2 bits convert rule
def solve_end(input_str, E_set, bin_str):
    bases = input_str[-2:]
    if bases in E_set.keys():
        end = E_set[bases]
    else:
        end = {'0': 'AC', '1': 'TC', '00': 'CA', '01': 'GT', '10': 'AG', '11': 'TG'}
    return end[bin_str]

# new Quaternary-like code
def n_Q_like(input_str, B_set):
    dna_str = ""
    end = {'0': 'AC', '1': 'TC', '00': 'CG', '01': 'CA', '10': 'GT', '11': 'GC'}
    rule = 'ATCG'
    A_extra = {'00': 'A', '01': 'T', '10': 'C', '11': 'G'}
    B_extra = {'00': 'G', '01': 'C', '10': 'T', '11': 'A'}
    # first two bases
    dna_str += A_extra[input_str[0:2]] + A_extra[input_str[2:4]]
    p1 = 4
    p2 = 0
    flag1 = 1
    flag2 = 1
    str_len = len(input_str)
    while p1 < str_len:
        if p1 == str_len - 2:
            # dna_str += end[input_str[p1:]]
            dna_str += solve_end(input_str=dna_str,E_set=E_set, bin_str=input_str[p1:])
            break
        elif p1 == str_len - 1:
            # dna_str += end[input_str[p1]]
            dna_str += solve_end(input_str=dna_str,E_set=E_set, bin_str=input_str[p1])
            break
        else:
            pre_two = dna_str[p2] + dna_str[p2 + 1]
            if flag2 % 2 !=0:
                current_set = B_set[0]
            else:
                current_set = B_set[1]
            if pre_two in current_set.keys():
                if input_str[p1] == '0':
                    zero_index = current_set[pre_two].index('0')
                    dna_str += rule[zero_index]
                    p1 += 1
                    p2 += 1
                    flag1 = -flag1
                    flag2+=1
                else:
                    if p1 == str_len - 1:
                        # dna_str += end[input_str[p1]]
                        dna_str += solve_end(input_str=dna_str, E_set=E_set, bin_str=input_str[p1])
                    else:
                        for index, value in enumerate(current_set[pre_two]):
                            temp = 2 ** 1 * int(input_str[p1]) + 2 ** 0 * int(input_str[p1 + 1])
                            if value == str(temp):
                                dna_str += rule[index]
                                p2 += 1
                        p1 += 2
                        flag1 = -flag1
                        flag2 += 1
            else:
                if p1 != str_len - 1:
                    ss = input_str[p1:p1 + 2]
                    if flag1 == -1:
                        dna_str += B_extra[ss]
                    else:
                        dna_str += A_extra[ss]
                    p2 += 1
                    p1 += 2
                else:
                    # dna_str += end[input_str[p1]]
                    dna_str += solve_end(input_str=dna_str, E_set=E_set, bin_str=input_str[p1])
                    p1 += 1
    return dna_str

# choose best rule id
def best_rule(input_str,rule_set):
    record = []
    for i in range(16):
        set = rule_set[i]
        result = n_Q_like(input_str, set)
        result_len = len(result)
        gc_ratio = float(result.count("C") + result.count("G")) / float(result_len)
        info_dict = dict.fromkeys(['result_len', 'gc_ratio', 'dna_sequence'])
        info_dict['result_len'] = result_len
        info_dict['gc_ratio'] = gc_ratio
        info_dict['dna_sequence'] = result
        record.append(info_dict)
    candicate_id = 0
    min_bases = 200
    for j in range(16):
        if record[j]['gc_ratio'] >= 0.4 and record[j]['gc_ratio'] <= 0.6:
            if record[j]['result_len'] <= min_bases:
                candicate_id = j
                min_bases = record[j]['result_len']
    return candicate_id, record[candicate_id]['dna_sequence']

# 4 bases connect index and data
def rule_encode(rule):
    result = ""
    encode_rule = [{'0':'A','1':'T'},{'0':'C','1':'G'},{'0':'A','1':'T'},{'0':'C','1':'G'}]
    binary = str(bin(rule))[2:].zfill(4)
    for i in range(4):
        result += encode_rule[i][binary[i]]
    return result

def encode(binary_data,Rule_set):
    seg_num = len(binary_data)
    print('Original binary segment total',seg_num)
    sequence_record = []
    density_record = []
    low_record = []
    gc_record = []
    dna_record = []
    maxlen = 0
    minlen = 1000
    maxgc = 0.01
    mingc = 0.99
    total_gc = 0
    total_Density = 0
    for i in range(seg_num):
        if i %1000 ==0:
            print(i)
        best_id, best = best_rule(binary_data[i], Rule_set)
        if len(best) > maxlen:
            maxlen = len(best)
        if len(best) < minlen:
            minlen = len(best)
        sequence = rule_encode(best_id) + best
        sequence_record.append(sequence)
        total_Density += len(best)+4
        density = 180/(len(best)+4)
        density_record.append(density)
        if density <1.6:
            low_record.append(binary_data[i])
        gc_ratio = check_gc(best)
        total_gc += gc_ratio
        if gc_ratio > maxgc:
            maxgc = gc_ratio
        if gc_ratio < mingc:
            mingc = gc_ratio
        if gc_ratio <0.4 or gc_ratio >0.6:
            gc_record.append(gc_ratio)
            dna_record.append(binary_data[i])
    print('Max GC',maxgc)
    print('Min GC',mingc)
    print('Max length', maxlen)
    print('Min length', minlen)
    print('total GC',total_gc/seg_num)
    print('density:', seg_num * 180/ total_Density)
    print('avg length',total_Density/seg_num)
    return density_record,low_record,gc_record,sequence_record,total_Density

# write sequences to text file
def write_dna_file(path, dna_sequences):
    with open(path, "w") as file:
        for index, dna_sequence in enumerate(dna_sequences):
            str = "".join(dna_sequence)
            file.write(str + "\n")
    return True

# read DNA file
def read_dna_file(path):
    dna_sequences = []
    with open(path, "r") as file:
        # 逐行读取
        lines = file.readlines()
        for  index, line in enumerate(lines):
            dna_sequences.append(list(line.replace("\n", "")))
    return dna_sequences

# decode rule ID
def rule_decode(bases):
    binary_str = ""
    decode_rule = [{'A':'0','T':'1'},{'C':'0','G':'1'},{'A':'0','T':'1'},{'C':'0','G':'1'}]
    for i in range(4):
        binary_str += decode_rule[i][bases[i]]
    rule = int(binary_str,2)
    return rule

# decode Q-like (payload)
def q_like_decode(input_dna, B_set, rule_index, E_set):
    binary_str = ''
    rule = B_set[rule_index]
    base_to_bin_A = {'A':'00','T':'01','C':'10','G':'11'}
    base_to_bin_B = {'G':'00','C':'01','T':'10','A':'11'}
    base_rule = ['A','T','C','G']
    dec_to_bin = {'0':'0','2':'10','3':'11'}
    binary_str += base_to_bin_A[input_dna[0]] + base_to_bin_A[input_dna[1]]
    base_len = len(input_dna)
    flag1 = 1
    flag2 = 1
    pos = 2
    pre = input_dna[0]+input_dna[1]
    while pos != base_len-2:
        if pre not in rule[0].keys():
            if flag2 %2 == 1:
                binary_str += base_to_bin_A[input_dna[pos]]
            else:
                binary_str += base_to_bin_B[input_dna[pos]]
            pre = input_dna[pos-1]+input_dna[pos]
            pos += 1
        else:
            if flag1 == 1:
                binary_str += dec_to_bin[rule[0][pre][base_rule.index(input_dna[pos])]]
            else:
                binary_str += dec_to_bin[rule[1][pre][base_rule.index(input_dna[pos])]]
            pre = input_dna[pos-1]+input_dna[pos]
            flag1 = -flag1
            flag2 += 1
            pos += 1
    if pre in E_set.keys():
        end = E_set[pre]
    else:
        end = {'0': 'AC', '1': 'TC', '00': 'CA', '01': 'GT', '10': 'AG', '11': 'TG'}
    end_two = input_dna[-2]+input_dna[-1]
    for key,value in end.items():
        if end_two == value:
            binary_str += key
    return binary_str

# Decode
def decode(dna_sequences, B_set, E_set):
    seg_num = len(dna_sequences)
    matrix = []
    # each DNA segment
    for sequence in dna_sequences:
        rule_index = rule_decode(sequence[:4])
        binary_data = q_like_decode(sequence[4:],B_set=B_set,rule_index = rule_index,E_set=E_set)
        matrix.append(list(map(int,binary_data)))
    return matrix

# To get orignal file
def write_BinaryMatrix_to_file(path, matrix, size):
    with open(path, "wb+") as file:
        # Change bit to byte (8 -> 1), and write a file as bytes
        bit_index = 0
        temp_byte = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                bit_index += 1
                temp_byte *= 2
                temp_byte += matrix[row][col]
                if bit_index == 8:
                    if size > 0:
                        file.write(struct.pack("B", int(temp_byte)))
                        bit_index = 0
                        temp_byte = 0
                        size -= 1
    return True

def Encode_file(file_path,out_path,segment_length,B_set):
    data, size = load_file_to_BinaryMatrix(file_path, segment_length)
    length = len(data)
    for i in range(length):
        data[i] = "".join(data[i])
    print("Original size = "+str(size) + "Bytes")
    density_r, low, gc, sequences,nico = encode(data, B_set)
    print("No. of nucleotides",nico)
    write_dna_file(out_path, sequences)

def Decode_file(dna_path,out_path,origin_size,B_set,E_set):
    dna = read_dna_file(dna_path)
    matrix = decode(dna, B_set=B_set, E_set=E_set)
    write_BinaryMatrix_to_file(out_path, matrix, origin_size)
    print('Decode Success!')

if __name__ == '__main__':
    # Encode
    start = time.time()
    Encode_file('A:/~.jpg','A:/~.txt',segment_length=180,B_set=B_set)
    end = time.time()
    print('It take times', end - start)
    # Decode

    #Decode_file('A:/~.txt','A:/~.jpg',origin_size=112620,B_set=B_set,E_set=E_set)