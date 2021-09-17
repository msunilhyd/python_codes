
def write_fun():
    data = 'This is sample text'
    with open('sample.txt', 'w') as f:
        f.write(data)

def read_fun():
    with open('sample.txt', 'r') as f:
        read_text = f.read()
        print(read_text)

if __name__ ==  '__main__':
    write_fun()
    read_fun()