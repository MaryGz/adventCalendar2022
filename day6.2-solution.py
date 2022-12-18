packet = []
index = 0
PACKET_LENGTH = 14
with open("day6-input.txt", "r") as f:
    line = f.readline()
    s = list(line)

    for i in range(0, len(s)):
        packet.append(s[i])
        index += 1
        if len(packet) == PACKET_LENGTH:
            c = []
            for j in range(0, PACKET_LENGTH):
                x = packet.count(packet[j])
                c.append(x)

            if sum(c) == PACKET_LENGTH:
                print(index)
                break
            packet.pop(0)