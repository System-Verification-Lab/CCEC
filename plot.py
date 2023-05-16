import matplotlib.pyplot as plt

def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = []
    for line in lines:
        line = line.strip()
        if ' ' in line:
            x, y = line.split(' ')
            data.append((float(x), float(y)))
        else:
            data.append(float(line))

    return data

def plot_graphs(*data_sets):
    plt.figure()
    markers = ['o', 'o', '<', '<'] 
    colors = ['green', 'blue', 'green', 'blue']  


    for i, data in enumerate(data_sets):

        x = []
        y = []
        for j, item in enumerate(data):
            if isinstance(item, tuple):
               # if j % 2 != 0:  # Skip every second data point
               #     continue
                x.append(item[0])
                y.append(item[1])
            else:
              #  if j % 2 != 0:  # Skip every second data point
               #     continue
                y.append(item)                
        

            

        if len(x) == 0:
            x = range(1, len(y) + 1)

        plt.scatter(x, y, marker=markers[i % len(markers)], facecolors='none', edgecolors=colors[i % len(colors)])

    #plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Depth', fontsize=17)  
    plt.ylabel('Time (ms)', fontsize=17)  
    plt.xticks(fontsize=17)  
    plt.yticks(fontsize=17)
    #plt.title('titlos')
    legends = ['nq=50, This work', 'nq=250, This work', 'nq=50, QuSAT', 'nq=250, QuSAT']  
    plt.legend(legends, fontsize=12)
    plt.savefig('/Users/thanosd/Downloads/data/d.pdf',dpi=300,format='pdf',bbox_inches='tight')
   # plt.ylim(1, 10000000000) 
    plt.show()
    
# Example usage:
data1 = read_data('stim_times_50.txt')
data2 = read_data('stim_times_250.txt')
data3 = read_data('qusat_times_50.txt')
data4 = read_data('qusat_times_250.txt')

plot_graphs(data1, data2, data3, data4)
