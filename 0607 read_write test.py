__author__ = 'lena'
import binascii
import struct

tmpl_chnk_dic = {}

for i in range(2, 9):
    f_prfx = "/Users/lena/PycharmProjects/SC-chunk-offsets2/chunk_templates/"
    f_name = "chunk" + str(i) + ".dat"
    path = f_prfx + f_name
    md = "rb"
    chnk = open(path, md)
    chnk = binascii.hexlify(chnk.read())
    tmpl_chnk_dic["chunk"+str(i)] = chnk
    print(f_name)

print(len(tmpl_chnk_dic))
print()

outfile = open("Chunk_out.dat", "wb")


with open("chunks.dat", "rb") as f:
    # Read the complete chunk directory
    complete_directory_of_chunks = f.read(786444)

    # Create an array of chunks as recorded in the chunk bodies
    chunk_body_coords_final = []
    one_chunk = binascii.hexlify(f.read(66576))
    for num in range(1000):
        header = one_chunk[:32]
        blcks_sp = one_chunk[32:133152]
        xz = [[]]
        x = header[16:24]
        z = header[24:32]
        xz[0].append(x)
        xz[0].append(z)
        xz.append(blcks_sp)
        chunk_body_coords_final.append(xz)
        one_chunk = binascii.hexlify(f.read(66576))
    print(len(chunk_body_coords_final[0][0][1]))

    count = 0
    for i in range(len(chunk_body_coords_final)):
        current_chunk_body = chunk_body_coords_final[i][1]
        if current_chunk_body.count(b'44004400440044004400440044004400') > 0:
            count += 1
            current_chunk_body = tmpl_chnk_dic['chunk8']
            chunk_body_coords_final[i][1] = current_chunk_body

    bytes_again = b''
    for i in range((1000)):
        bytes_again += b'efbeaddeffffffff'
        bytes_again += chunk_body_coords_final[i][0][0]
        bytes_again += chunk_body_coords_final[i][0][1]
        bytes_again += chunk_body_coords_final[i][1]

        # print(bytes_again)
    bytes_again = binascii.unhexlify(bytes_again)

    print(type(chunk_body_coords_final[0][0][0]))
    print(count)
    outfile.write(complete_directory_of_chunks)
    outfile.write(bytes_again)
    outfile.close()
    f.close()

    print("done")



