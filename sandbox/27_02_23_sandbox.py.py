import os
#os.listdir(PATH)

print(os.listdir(r'C:\Users\anast\OneDrive\Документи\python_study\sandbox\01'))

class ReadTest:
    def __init__(self, way):
        self.way = os.listdir(way)
        self.dir = way
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        #print(self.way[self.index])
        if self.index >= len(self.way):
            raise StopIteration
        file_path = os.path.join(self.dir, self.way[self.index])    
        with open(file_path, 'r') as f:
            self.index += 1
            return f.read()
        
            
            

        

    def read_file(self):
        pass


if __name__ == '__main__':
    my_way = r'C:\Users\anast\OneDrive\Документи\python_study\sandbox\01'
    iter_file = ReadTest(my_way)
    #print(iter_file.next())
    print(iter_file.way)

    for i in iter_file:
        print(i)
