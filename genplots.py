import matplotlib.pyplot as plt

def plot_graphs(LRU, MRU, CLOCK , frames,x_label, y_label, title,min_y,max_y):

    # Even if they overlap, the marker should be visible
    plt.plot(frames, LRU, label='LRU', color='red')
    plt.plot(frames, MRU, label='MRU', color='blue')
    plt.plot(frames, CLOCK, label='CLOCK', color='green')
    
    #  Now plot the markers
    plt.plot(frames, LRU, 'ro')
    plt.plot(frames, MRU, 'bo')
    plt.plot(frames, CLOCK, 'go')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    plt.savefig(title + '.png')



# pg_hit_LRU = [0, 0, 0, 0, 0, 0,0,0]
# pg_hit_MRU = [0, 0, 0, 0, 0, 0,0,0]
# pg_hit_CLOCK = [0, 0, 0, 0, 0, 0, 0, 0]
# frames = [2, 4, 6, 8, 10, 12, 14, 16]

# plot_graphs(pg_hit_LRU, pg_hit_MRU, pg_hit_CLOCK, frames, 'Number of Frames', 'Page Hits', 'Select page hits', 0, 10)


# pg_access_LRU = [26, 24, 22, 20, 18, 16, 14, 14]
# pg_access_MRU = [14, 14, 14, 14, 14, 14, 14, 14]
# pg_access_CLOCK = [14, 14, 14, 14, 14, 14, 14, 14]
# frames = [2, 4, 6, 8, 10, 12, 14, 16]

# plot_graphs(pg_access_LRU, pg_access_MRU, pg_access_CLOCK, frames, 'Number of Frames', 'Page Accesses', 'Select page accesses', 0, 20)



# # Join page hits and page accesses
# pg_hit_MRU = [0,8,10,25,48,54,77,90,100]
# pg_hit_LRU = [0,0,0,0,0,0,0,182,182]
# pg_hit_CLOCK = [0,0,0,0,0,0,0,120,120]
# frames = [2, 4, 6, 8, 10, 12, 14, 16, 18]

# plot_graphs(pg_hit_LRU, pg_hit_MRU, pg_hit_CLOCK, frames, 'Number of Frames', 'Page Hits', 'Join page hits', 0, 200)


# pg_access_MRU = [210, 210, 210, 210, 210, 210, 210, 210, 210]
# pg_access_LRU = [210, 210, 210, 210, 210, 210, 210, 210, 210]
# pg_access_CLOCK = [210, 210, 210, 210, 210, 210, 210, 210, 210]

# frames = [2, 4, 6, 8, 10, 12, 14, 16, 18]

# plot_graphs(pg_access_LRU, pg_access_MRU, pg_access_CLOCK, frames, 'Number of Frames', 'Page Accesses', 'Join page accesses', 0, 220)


disk_reads_MRU = [210,207,200,189,174,156,135,135,135]
disk_reads_LRU = [210,210,210,210,210,210,28,28,28]
disk_reads_CLOCK = [418,416,414,412,410,408,406,404,402]

frames = [2, 4, 6, 8, 10, 12, 14, 16, 18]

plot_graphs(disk_reads_LRU, disk_reads_MRU, disk_reads_CLOCK, frames, 'Number of Frames', 'Disk Reads', 'Join Disk Reads', 0, 420)